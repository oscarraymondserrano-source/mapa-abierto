"""Produce los 10 vídeos: locución guía, subtítulos, imágenes de escena, prompts Pika, línea de tiempo, SEO, miniaturas y MP4."""
import os, sys, csv, json, re, subprocess, wave, shutil
sys.path.insert(0, os.path.dirname(__file__))
from gfx import *
import audio
from content.common import LOOKS, STYLE, NEGATIVE
from content import v01, v03, shorts, post, shorts2, shorts3
from content import final_overrides as FO
import copy

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE = "/tmp/claude-0/tts_cache"
FPS = 30
ID_DIR = os.path.join(ROOT, "01_IDENTIDAD_VISUAL")
AUD_DIR = os.path.join(ROOT, "05_RECURSOS_AUDIO")

VIDEOS = [v01.VIDEO, shorts.V02, v03.VIDEO, shorts.V04, shorts.V05, shorts.V06, shorts.V07, post.V08, post.V09, shorts.V10] + shorts2.SHORTS2 + shorts3.SHORTS3
# Tandas diarias: cualquier content/tanda_*.py que defina SHORTS (lista) y SCHED (calendario)
import importlib as _il, glob as _glob
for _f in sorted(_glob.glob(os.path.join(os.path.dirname(__file__), "content", "tanda_*.py"))):
    _m = _il.import_module("content." + os.path.basename(_f)[:-3])
    VIDEOS += list(getattr(_m, "SHORTS", []))
VOICE = os.environ.get("MA_VOICE", "piper")  # 'eleven' = ElevenLabs (Nico)
ONLY = sys.argv[1:]  # p.ej. V02 V04

TIPO_TXT = {
    "GRAFICO": "Motion graphics propio (marca)",
    "OFICIAL": "Material OFICIAL Rockstar (tráiler / captura / arte)",
    "IA": "Clip IA (Pika) – rotular 'Recreación'",
    "GAMEPLAY": "GAMEPLAY PROPIO (grabar tras el desbloqueo)",
}
ANIM_TXT = {
    "GRAFICO": "Rótulo entra con escala 90→100 % y desenfoque de movimiento (8 fotogramas); ítems escalonados cada 0,3 s; palabras clave en amarillo",
    "OFICIAL": "Ken Burns 100→108 %; marco neón 4 px; crédito 'Fuente: Rockstar Games' abajo a la izquierda durante toda la escena",
    "IA": "Clip Pika de 3-4 s (encadenar variaciones si la escena es más larga); etiqueta 'Recreación IA' arriba a la izquierda",
    "GAMEPLAY": "Captura propia; zoom de énfasis (100→115 %) sobre el detalle comentado; etiqueta 'Gameplay propio · [plataforma]'",
}
LUZ_MARCA = "Paleta de marca: degradado noche-púrpura-magenta, acentos neón cian/magenta, sol de atardecer naranja"
MOVES = ["slow push-in", "slow lateral slide left to right", "slow tilt up", "slow pull-out", "slow orbit"]


def mmss(t):
    m = int(t // 60); s = t - m * 60
    return f"{m:02d}:{s:06.3f}"


def srt_t(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = int(t % 60); ms = int(round((t - int(t)) * 1000))
    if ms == 1000:
        s += 1; ms = 0
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def ass_t(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = t % 60
    return f"{h:d}:{m:02d}:{s:05.2f}"


def tokens(text):
    out, emph = [], False
    for w in text.split():
        start = w.startswith("*") or ("*" in w[:2])
        if start:
            emph = True
        clean = w.replace("*", "")
        out.append((clean, emph))
        if w.rstrip(".,:;!?¿¡)").endswith("*") or w.endswith("*"):
            emph = False
    return out


def _partition(words, nL, maxc, llen):
    """Reparte las palabras en exactamente nL líneas equilibradas (DP), cada una <= maxc. None si no es posible."""
    n = len(words)
    if nL > n:
        nL = n
    target = llen(words) / nL
    INF = float("inf")
    best = [[INF] * (n + 1) for _ in range(nL + 1)]
    prev = [[-1] * (n + 1) for _ in range(nL + 1)]
    best[0][0] = 0
    for k in range(1, nL + 1):
        for j in range(1, n + 1):
            for i in range(k - 1, j):
                if best[k - 1][i] == INF:
                    continue
                L = llen(words[i:j])
                if L > maxc and j - i > 1:
                    continue
                c = best[k - 1][i] + (L - target) ** 2
                if c < best[k][j]:
                    best[k][j] = c; prev[k][j] = i
    if best[nL][n] == INF:
        return None
    out, j = [], n
    for k in range(nL, 0, -1):
        i = prev[k][j]; out.append(words[i:j]); j = i
    return out[::-1]


def sub_chunks(text, maxc):
    """Bloques de máx. 2 líneas que nunca cruzan el final de una frase."""
    toks = tokens(text)
    sents, cur = [], []
    for tk in toks:
        cur.append(tk)
        if tk[0][-1:] in ".?!:":
            sents.append(cur); cur = []
    if cur:
        sents.append(cur)

    def llen(l):
        return len(" ".join(w for w, _ in l))

    chunks = []
    for sent in sents:
        import math
        nL = max(1, math.ceil(llen(sent) / maxc))
        if nL > 1 and nL % 2 == 1:
            nL += 1
        lines = None
        while lines is None:
            lines = _partition(sent, nL, maxc, llen)
            nL += 1 if lines is None else 0
        # reequilibrar: si la última línea es una sola palabra corta, pasarle una palabra de la anterior
        if len(lines) >= 2 and len(lines[-1]) == 1 and len(lines[-2]) > 2:
            lines[-1].insert(0, lines[-2].pop())
        for k in range(0, len(lines), 2):
            chunks.append(lines[k:k + 2])
    # si un bloque queda con 1 línea muy corta y el anterior también es de 1 línea, unirlos
    out = []
    for c in chunks:
        if out and len(c) == 1 and len(out[-1]) == 1 and llen(c[0]) < maxc * 0.5 and llen(out[-1][0]) <= maxc:
            out[-1].append(c[0])
        else:
            out.append(c)
    return out


def chunk_plain(c):
    return "\n".join(" ".join(w for w, _ in l) for l in c)


def chunk_ass(c):
    lines = []
    for l in c:
        parts = []
        for w, e in l:
            parts.append("{\\c&H33D6FF&}" + w + "{\\c&HFFFFFF&}" if e else w)
        lines.append(" ".join(parts))
    return "\\N".join(lines)


def pika_prompt(v, sc, idx):
    ar = "9:16" if v["formato"] == "short" else "16:9"
    if sc["look"]:
        L = LOOKS[sc["look"]]
        subj = (sc["extra"] + ", " if sc["extra"] else "") + L["subject"]
        p = (f"{subj}. Environment: {L['env']}. Camera: {L['angle']}, {L['move']}. Lighting: {L['light']}. "
             f"Atmosphere: {L['atmo']}. Composition: {L['comp']}"
             f"{'; vertical framing with the subject centered and empty space in the upper third for titles' if ar == '9:16' else '; leave clean negative space in the upper left for titles'}. "
             f"Animation: {L['anim']}. {STYLE} Aspect ratio {ar}.")
        uso = "Clip principal de la escena" if sc["tipo"] == "IA" else ("Fondo / B-roll de apoyo (solo si falta material oficial o gameplay; rotular 'Recreación IA')" if sc["tipo"] in ("OFICIAL", "GAMEPLAY") else "Fondo animado bajo el gráfico (opacidad 60 %)")
    else:
        mv = MOVES[idx % len(MOVES)]
        theme = sc["rotulo"].lower()
        p = (f"Abstract retro-futuristic background for a motion graphics title about '{theme}' (do not render any text): a huge striped sunset sun over a calm "
             f"ocean horizon, glowing magenta neon grid floor, silhouettes of palm trees at the edges, distant city skyline. Camera: frontal "
             f"eye-level, {mv}. Lighting: magenta and cyan neon glow, orange sun haze. Atmosphere: cinematic, nostalgic, premium. Composition: "
             f"{'centered vertical composition, calm areas in the middle third for text' if ar == '9:16' else 'symmetrical, calm dark area in the center for text overlays'}. "
             f"Animation: subtle grid scrolling toward camera, gentle sun shimmer, soft particles floating, seamless loop. "
             f"Stylized 3D render, clean, high detail. No text, no letters, no logos. Aspect ratio {ar}.")
        uso = "Fondo animado de marca bajo el gráfico (opacidad 70 %)"
    params = f"-ar {ar} -motion 2 -gs 12 -neg \"{NEGATIVE}\""
    return p, params, uso


# ---------------- IMÁGENES DE ESCENA ----------------
_BG = {}


def tech_bg(W, H, seed):
    img = vgradient(W, H, [(0, NAVY), (0.6, NIGHT), (1, (45, 15, 80))]).convert("RGBA")
    d = ImageDraw.Draw(img)
    step = 64
    for x in range(0, W, step):
        d.line([(x, 0), (x, H)], fill=(38, 40, 95))
    for y in range(0, H, step):
        d.line([(0, y), (W, y)], fill=(38, 40, 95))
    rnd = random.Random(seed)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lay)
    for _ in range(3):
        r = rnd.randint(int(min(W, H) * 0.2), int(min(W, H) * 0.45))
        cx, cy = rnd.randint(0, W), rnd.randint(0, H)
        ld.ellipse([cx - r, cy - r, cx + r, cy + r], fill=rnd.choice([MAGENTA, CYAN, PURPLE]) + (60,))
    img.alpha_composite(lay.filter(ImageFilter.GaussianBlur(min(W, H) * 0.12)))
    return img


def brand_bg(W, H, seed, style=0):
    k = (W, H, seed % 4, style)
    if k not in _BG:
        if style == 1:
            img = sunset_scene(W, H, seed=seed % 4 + 41, sun=False, horizon=0.74 if W > H else 0.66)
        elif style == 2:
            img = tech_bg(W, H, seed)
        else:
            img = sunset_scene(W, H, seed=seed % 4 + 21, horizon=0.68 if W > H else 0.6, sun_r=int(min(W, H) * (0.26 if W > H else 0.3)))
        _BG[k] = img
    return _BG[k].copy()


def esquema_regiones(W=1920, H=1080, highlight=None):
    img = vgradient(W, H, [(0, NAVY), (1, NIGHT)]).convert("RGBA")
    d = ImageDraw.Draw(img)
    for x in range(0, W, 60):
        d.line([(x, 0), (x, H)], fill=(40, 40, 90))
    for y in range(0, H, 60):
        d.line([(0, y), (W, y)], fill=(40, 40, 90))
    # silueta muy simplificada (orientativa) de península + franja norte
    land = [(300, 140), (1500, 140), (1520, 260), (1180, 280), (1130, 360), (1180, 520), (1260, 700), (1300, 860), (1240, 930),
            (1150, 900), (1050, 760), (980, 640), (930, 520), (880, 380), (760, 330), (560, 330), (420, 290), (300, 280)]
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(layer).polygon(land, fill=(60, 30, 110, 255), outline=CYAN + (255,))
    ImageDraw.Draw(layer).line(land + [land[0]], fill=CYAN + (255,), width=5)
    img.alpha_composite(glow(layer, 8, 1))
    d = ImageDraw.Draw(img)
    for i in range(7):  # cayos
        x, y = 1130 - i * 42, 960 + i * 12
        d.ellipse([x - 14, y - 7, x + 14, y + 7], fill=(60, 30, 110), outline=CYAN, width=3)
    pins = [("PORT GELLHORN", 470, 230), ("MOUNT KALAGA", 870, 200), ("AMBROSIA", 1080, 440), ("GRASSRIVERS", 1060, 720),
            ("VICE CITY", 1270, 790), ("CAYOS DE LEONIDA", 930, 990)]
    pm = pin_mark(90)
    f = font(F_BLACK, 34)
    for name, x, y in pins:
        if highlight and highlight != "ALL" and name != highlight:
            dim = pm.copy(); dim.putalpha(dim.getchannel("A").point(lambda a: a // 3))
            img.alpha_composite(dim, (x - 45, y - 85))
            ImageDraw.Draw(img).text((x + 50, y - 60), name, font=f, fill=(150, 150, 190))
    for name, x, y in pins:
        if highlight and highlight != "ALL" and name != highlight:
            continue
        if highlight and highlight != "ALL":
            ring = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(ring).ellipse([x - 120, y - 140, x + 120, y + 100], outline=YELLOW + (255,), width=8)
            img.alpha_composite(glow(ring, 10, 2))
            big = pin_mark(150)
            img.alpha_composite(big, (x - 75, y - 140))
            draw_text_outline(img, (x + 80, y - 80), name, font(F_BLACK, 52), fill=YELLOW, ow=6)
        else:
            img.alpha_composite(pm, (x - 45, y - 85))
            draw_text_outline(img, (x + 50, y - 60), name, f, ow=4)
    rounded_box(img, (40, 40, 40 + text_size(font(F_BLACK, 40), "ESQUEMA ORIENTATIVO · NO OFICIAL")[0] + 50, 120), 18, (255, 214, 102, 235))
    ImageDraw.Draw(img).text((64, 56), "ESQUEMA ORIENTATIVO · NO OFICIAL", font=font(F_BLACK, 40), fill=NAVY)
    ImageDraw.Draw(img).text((44, H - 60), "Posiciones aproximadas basadas en la geografía de Florida. Rockstar no ha publicado el mapa completo.",
                             font=font(F_SEMI, 28), fill=(220, 220, 255))
    return img


GREEN = (74, 222, 128)
RED = (255, 77, 77)


def draw_stamp(img, text, color, cx, cy, size):
    """Sello rotado tipo tampón (MITO / VERDAD)."""
    f = font(F_BLACK, size)
    tw, th, _ = text_size(f, text)
    pad = int(size * 0.35)
    layer = Image.new("RGBA", (tw + pad * 2 + 20, th + pad * 2 + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((10, 10, layer.width - 10, layer.height - 10), int(size * 0.18), outline=color + (255,), width=max(6, size // 10))
    d.text((layer.width // 2, layer.height // 2), text, font=f, fill=color + (255,), anchor="mm")
    layer = glow(layer, max(4, size // 14), 1).rotate(-12, expand=True, resample=Image.BICUBIC)
    img.alpha_composite(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)))


def draw_options(img, opts, y, W, short, shown=None, correct=None, reveal=False):
    s = W / 1080 if short else W / 1920
    fo = font(F_BLACK if short else F_BOLD, 64 if short else int(54 * s))
    bw = int(W * (0.82 if short else 0.5)); x0 = (W - bw) // 2
    bh = 120 if short else int(96 * s)
    for k, o in enumerate(opts):
        if shown is not None and k >= shown:
            break
        ok = reveal and k == correct
        dim = reveal and k != correct
        fill = (12, 40, 30, 230) if ok else (10, 10, 40, 210 if not dim else 120)
        out = (GREEN if ok else (CYAN if not dim else (70, 75, 120))) + (255,)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).rounded_rectangle((x0, y, x0 + bw, y + bh), 22, fill=fill, outline=out, width=6 if ok else 4)
        img.alpha_composite(glow(lay, 10, 1) if ok else lay)
        d = ImageDraw.Draw(img)
        r = bh // 2 - 18
        cx, cy = x0 + 30 + r, y + bh // 2
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(GREEN if ok else (MAGENTA if not dim else (90, 60, 110))))
        d.text((cx, cy), "✓" if ok else "ABCD"[k], font=font(F_BLACK, int(r * 1.3)), fill=NAVY if ok else WHITE, anchor="mm")
        d.text((cx + r + 28, cy), o, font=fo, fill=(WHITE if not dim else (150, 150, 185)), anchor="lm")
        y += bh + (26 if short else int(20 * s))
    return y


INITIALS = {"LUCIA CAMINOS": "LC", "JASON DUVAL": "JD", "JASON & LUCIA": "J+L", "JASON & LUCIA · LEONIDA": "J+L"}


RK_DIR = os.environ.get("MA_RK", "/tmp/claude-0/rk_dl")


def official_photo(rel, W, H, fx=0.5):
    """Captura oficial de Rockstar recortada a W×H (cover) con foco horizontal fx."""
    im = Image.open(os.path.join(RK_DIR, "x_GTAVI_Screenshots", rel)).convert("RGB")
    sc_ = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * sc_ + 1), int(im.height * sc_ + 1)), Image.LANCZOS)
    x = int((im.width - W) * fx); y = (im.height - H) // 2
    return im.crop((x, y, x + W, y + H)).convert("RGBA")


def credit_chip(img, W, H, short, text):
    f = font(F_MONO, 30 if short else 24)
    tw = text_size(f, text)[0]
    x, y = (40, 300) if short else (W - tw - 70, 30)
    rounded_box(img, (x, y, x + tw + 30, y + (50 if short else 42)), 10, (0, 0, 0, 170))
    ImageDraw.Draw(img).text((x + 15, y + (9 if short else 7)), text, font=f, fill=(235, 235, 245))


def scene_image(v, sc, idx, W, H, final, n_items=None, last=False, countdown=None, stamp_on=True, clip_overlay=False):
    short = H > W
    seed = idx + (7 if short else 0)
    if final and last and not short:
        img = sunset_scene(W, H, seed=13, horizon=0.72)
        vignette(img, 0.6)
        wordmark(img, W // 2, 90, 90, anchor_center=True)
        for (x, y, w, h) in [(150, 270, 720, 405), (1050, 270, 720, 405)]:
            lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(lay).rounded_rectangle((x, y, x + w, y + h), 24, fill=(5, 5, 25, 200), outline=CYAN + (255,), width=5)
            img.alpha_composite(glow(lay, 10, 1))
        neon_text(img, (W // 2, 740), sc["rotulo"], font(F_BLACK_IT, 72), color=MAGENTA, core=WHITE, radius=12, anchor="ma")
        return img
    style = (idx % 3) if final else 0
    if final and (sc.get("esquema") or sc["rotulo"] in ("MAPA ABIERTO", "SÍGUEME", "GUÁRDALO")):
        style = 0
    if clip_overlay or sc.get("foto"):
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0)) if clip_overlay else official_photo(sc["foto"], W, H, sc.get("fx", 0.5))
        grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(grad)
        for yy in range(H):  # oscurecer arriba (rótulos) y abajo (subtítulos), dejar el centro limpio
            t = yy / H
            a = int(185 * max(0, 1 - t / 0.42) ** 1.4 + 200 * max(0, (t - 0.55) / 0.45) ** 1.6) if short else int(170 * max(0, 1 - t / 0.35) ** 1.5 + 190 * max(0, (t - 0.7) / 0.3) ** 1.5)
            gd.line([(0, yy), (W, yy)], fill=(5, 5, 20, min(220, a)))
        img.alpha_composite(grad)
        credit_chip(img, W, H, short, "Vídeo: Rockstar Games" if clip_overlay else "Imagen: Rockstar Games")
    else:
        img = brand_bg(W, H, seed, style)
        dark = Image.new("RGBA", (W, H), (5, 5, 20, 120 if sc["tipo"] == "GRAFICO" else 150))
        img.alpha_composite(dark)
        vignette(img, 0.45)
    d = ImageDraw.Draw(img)
    s = W / 1920 if not short else W / 1080
    tag_f = font(F_MONO, int(26 * s))
    # etiquetas de producción (solo en animatic)
    if not final:
        label = {"GRAFICO": "GRÁFICO DE MARCA", "OFICIAL": "INSERTAR MATERIAL OFICIAL · © ROCKSTAR GAMES",
                 "IA": "CLIP IA PIKA · RECREACIÓN", "GAMEPLAY": "GRABAR GAMEPLAY PROPIO"}[sc["tipo"]]
        rounded_box(img, (int(30 * s), int(30 * s), int(30 * s) + int(len(label) * 16.5 * s) + int(40 * s), int(80 * s)), int(10 * s),
                    (0, 0, 0, 170), outline=(MAGENTA if sc["tipo"] in ("OFICIAL", "GAMEPLAY") else CYAN) + (255,), width=3)
        d.text((int(50 * s), int(40 * s)), label, font=tag_f, fill=WHITE)
        d.text((W - int(30 * s), int(40 * s)), f"{v['id']} · ESCENA {idx + 1:02d}", font=tag_f, fill=(200, 200, 230), anchor="ra")
    # panel de marcador de posición
    if (sc["tipo"] in ("OFICIAL", "GAMEPLAY")) and not final:
        if short:
            box = (70, 760, W - 70, 1180)
        else:
            box = (300, 300, W - 300, 760)
        rounded_box(img, box, int(26 * s), (0, 0, 0, 165), outline=MAGENTA + (255,), width=5)
        fp = font(F_SEMI, int(32 * s))
        lines = wrap("INSERTAR: " + sc["visual"], fp, box[2] - box[0] - int(60 * s))[:6]
        y = box[1] + int(30 * s)
        for ln in lines:
            d.text((box[0] + int(30 * s), y), ln, font=fp, fill=(240, 240, 255))
            y += int(44 * s)
    esq = sc.get("esquema") or ("ALL" if (v["id"] == "V03" and "esquema" in sc["visual"].lower()) else None)
    if esq:
        e = esquema_regiones(highlight=esq)
        sc_ = (0.66 if esq == "ALL" else 0.56) if final else 0.8
        e = e.resize((int(W * sc_), int(W * sc_ * 1080 / 1920)))
        img.alpha_composite(e, ((W - e.width) // 2, int(H * (0.15 if esq == "ALL" else 0.24))))
    if final and sc["rotulo"] in INITIALS:
        cx, cy, r = (W // 2, 330, 170) if short else (300, 560, 190)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(lay).ellipse([cx - r, cy - r, cx + r, cy + r], fill=(10, 10, 40, 220), outline=MAGENTA + (255,), width=10)
        img.alpha_composite(glow(lay, 14, 2))
        neon_text(img, (cx, cy), INITIALS[sc["rotulo"]], font(F_BLACK_IT, int(r * 0.95)), color=CYAN, core=WHITE, radius=14, anchor="mm")
    # rótulo
    rot = sc["rotulo"]
    if rot:
        maxw = W - int(160 * s)
        size = int((92 if sc["tipo"] == "GRAFICO" else 70) * s) if not short else int(112 if sc["tipo"] == "GRAFICO" else 84)
        fr = font(F_BLACK_IT, size)
        while text_size(fr, rot)[0] > maxw and size > 30:
            # permitir dos líneas antes de reducir
            if len(wrap(rot, fr, maxw)) <= 2:
                break
            size -= 4; fr = font(F_BLACK_IT, size)
        lines = wrap(rot, fr, maxw)
        if short:
            y = (560 if final else 400) if sc["tipo"] == "GRAFICO" else 420
            if final and sc["rotulo"] in INITIALS:
                y = 640
            if final and sc.get("quiz"):
                y = 330
            if final and sc.get("stamp"):
                y = 660
        else:
            y = int(150 * s) if sc["tipo"] == "GRAFICO" else int(110 * s)
            if esq:
                y = int(60 * s) + (0 if final else int(40 * s))
        for ln in lines:
            if sc["tipo"] == "GRAFICO":
                neon_text(img, (W // 2, y), ln, fr, color=MAGENTA, core=WHITE, radius=int(12 * s), anchor="ma")
            else:
                draw_text_outline(img, (W // 2, y), ln, fr, ow=max(3, int(6 * s)), anchor="ma")
            y += int(size * 1.12)
        if sc.get("chip"):
            fc = font(F_MONO, int(30 * s) if not short else 36)
            tw = text_size(fc, sc["chip"])[0]
            x0 = (W - tw) // 2 - int(24 * s)
            rounded_box(img, (x0, y + int(6 * s), x0 + tw + int(48 * s), y + int(60 * s if not short else 66)), int(12 * s), YELLOW + (240,))
            ImageDraw.Draw(img).text((W // 2, y + int(16 * s)), sc["chip"], font=fc, fill=NAVY, anchor="ma")
            y += int(80 * s if not short else 90)
        # ítems
        if sc["items"] and n_items != 0:
            fi = font(F_BOLD, int((54 if final else 44) * s) if not short else (66 if final else 58))
            y += int(30 * s)
            for it in (sc["items"] if n_items is None else sc["items"][:n_items]):
                tw = text_size(fi, it)[0]
                bw = tw + int(90 * s)
                x0 = (W - bw) // 2
                bh = int((84 if final else 70) * s) if not short else (96 if final else 86)
                rounded_box(img, (x0, y, x0 + bw, y + bh), int(16 * s), (10, 10, 40, 200), outline=CYAN + (255,), width=3)
                ImageDraw.Draw(img).ellipse([x0 + int(22 * s), y + bh // 2 - int(9 * s), x0 + int(40 * s), y + bh // 2 + int(9 * s)], fill=MAGENTA)
                ImageDraw.Draw(img).text((x0 + int(60 * s), y + bh // 2), it, font=fi, fill=WHITE, anchor="lm")
                y += bh + (int(16 * s) if not short else 18)
                if (not short and y > H - 260) or (short and y > 1220):
                    break
    if sc.get("quiz"):
        q = sc["quiz"]
        yq = 740 if short else int(H * 0.42)
        draw_options(img, q["options"], yq, W, short, shown=(n_items if n_items is not None else len(q["options"])),
                     correct=q["correct"], reveal=q.get("reveal", False))
    if countdown is not None:
        cx, cy, r = (W // 2, 1300, 120) if short else (W - 220, H // 2, 120)
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).ellipse((cx - r, cy - r, cx + r, cy + r), fill=(10, 10, 40, 230), outline=YELLOW + (255,), width=10)
        img.alpha_composite(glow(lay, 14, 2))
        neon_text(img, (cx, cy), str(countdown), font(F_BLACK, int(r * 1.3)), color=YELLOW, core=WHITE, radius=10, anchor="mm")
    if sc.get("stamp") and stamp_on:
        col = RED if sc["stamp"] == "MITO" else GREEN
        draw_stamp(img, sc["stamp"], col, W // 2, (440 if short else int(H * 0.55)), 150 if short else 150)
    if final and short and v.get("serie"):
        fs_ = font(F_MONO, 34)
        lab = v["serie"]
        tw = text_size(fs_, lab)[0]
        x0 = (W - tw) // 2 - 26
        rounded_box(img, (x0, 210, x0 + tw + 52, 274), 32, MAGENTA + (235,))
        ImageDraw.Draw(img).text((W // 2, 222), lab, font=fs_, fill=WHITE, anchor="ma")
    if sc["rotulo"] in ("MAPA ABIERTO", "SÍGUEME", "GUÁRDALO") or "Sting" in sc["visual"] or "Logotipo" in sc["visual"]:
        m = pin_mark(int(300 * s) if not short else 380)
        img.alpha_composite(m, ((W - m.width) // 2, int(H * (0.42 if not short else 0.42))))
    return img


# ---------------- MINIATURAS ----------------
def thumb(spec, W, H, idx_seed=0, final_placeholder=True):
    short = H > W
    img = brand_bg(W, H, 3 + idx_seed)
    vignette(img, 0.5)
    d = ImageDraw.Draw(img)
    st = spec["estilo"]
    needs_real = st in ("oficial", "gameplay")
    cx_focal = int(W * 0.72) if not short else W // 2
    cy_focal = int(H * 0.5) if not short else int(H * 0.68)
    if needs_real and final_placeholder:
        box = (int(W * 0.47), int(H * 0.06), int(W * 0.97), int(H * 0.94)) if not short else (60, 900, W - 60, 1700)
        rounded_box(img, box, 22, (0, 0, 0, 170), outline=MAGENTA + (255,), width=6)
        fp = font(F_BOLD, 30 if not short else 44)
        ImageDraw.Draw(img).multiline_text(((box[0] + box[2]) // 2, (box[1] + box[3]) // 2),
                                           "INSERTAR CAPTURA REAL\n" + ("(oficial Rockstar)" if st == "oficial" else "(gameplay propio)"),
                                           font=fp, fill=(255, 255, 255), anchor="mm", align="center")
    elif st == "checklist":
        x0, y0 = (int(W * 0.58), int(H * 0.16)) if not short else (200, 980)
        fb = font(F_BLACK, int(H * 0.09) if not short else 90)
        for i in range(3):
            y = y0 + i * int(H * 0.24 if not short else 230)
            rounded_box(img, (x0, y, x0 + int(W * 0.36 if not short else 680), y + int(H * 0.18 if not short else 180)), 20, (10, 10, 40, 220), outline=CYAN + (255,), width=6)
            lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
            ld = ImageDraw.Draw(lay)
            bx = x0 + int(30 if not short else 40); by = y + int(H * 0.04 if not short else 40)
            sz = int(H * 0.1 if not short else 100)
            ld.line([(bx, by + sz * 0.5), (bx + sz * 0.35, by + sz * 0.85), (bx + sz, by)], fill=(80, 255, 140, 255), width=int(sz * 0.18), joint="curve")
            img.alpha_composite(glow(lay, 6, 2))
            ImageDraw.Draw(img).rounded_rectangle([bx + sz * 1.4, by + sz * 0.3, x0 + int(W * 0.33 if not short else 640), by + sz * 0.62], 10, fill=(255, 255, 255, 230))
    elif st == "reloj":
        sz = int(H * 0.36) if not short else 300
        fc = font(F_MONO, sz)
        while text_size(fc, "00:00")[0] > (W * 0.42 if not short else W * 0.85):
            sz -= 6; fc = font(F_MONO, sz)
        neon_text(img, (cx_focal, cy_focal), "00:00", fc, color=CYAN, core=WHITE, radius=18, anchor="mm")
    elif st == "mapa":
        e = esquema_regiones()
        ew = int(W * 0.55)
        e = e.resize((ew, int(ew * 1080 / 1920)))
        img.alpha_composite(e, (W - ew - int(W * 0.03), (H - e.height) // 2))
    elif st == "paisaje":
        for (x, y) in [(0.62, 0.45), (0.78, 0.3), (0.88, 0.55)]:
            m = pin_mark(int(H * 0.26))
            img.alpha_composite(m, (int(W * x), int(H * y)))
    elif st == "almacen":
        bx = (120, 1000, W - 120, 1130)
        rounded_box(img, bx, 30, (0, 0, 0, 200), outline=CYAN + (255,), width=6)
        rounded_box(img, (bx[0] + 12, bx[1] + 12, bx[0] + 12 + int((bx[2] - bx[0] - 24) * 0.84), bx[3] - 12), 22, MAGENTA + (255,))
        neon_text(img, (W // 2, 1250), "≈210 GB", font(F_BLACK, 130), color=CYAN, anchor="ma")
    elif st == "stamp":
        draw_stamp(img, "¿MITO?", RED, W // 2 if short else int(W * 0.74), 1250 if short else int(H * 0.52), 190 if short else 120)
    elif st == "quiz":
        draw_options(img, ["?", "?", "?"], 980 if short else int(H * 0.25), W, short)
    elif st == "lupa":
        lay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(lay)
        ld.ellipse([W // 2 - 260, 950, W // 2 + 260, 1470], outline=CYAN + (255,), width=40)
        ld.line([(W // 2 + 190, 1400), (W // 2 + 380, 1640)], fill=CYAN + (255,), width=60)
        img.alpha_composite(glow(lay, 10, 2))
    # texto principal
    t1, t2 = spec["texto"]
    if not short:
        size = int(H * 0.2)
        f = font(F_BLACK_IT, size)
        while max(text_size(f, t1)[0], text_size(f, t2)[0]) > W * 0.5 and size > 60:
            size -= 4; f = font(F_BLACK_IT, size)
        x = int(W * 0.04)
        y = int(H * 0.2)
        draw_text_outline(img, (x, y), t1, f, fill=WHITE, ow=10)
        draw_text_outline(img, (x, y + int(size * 1.05)), t2, f, fill=YELLOW, ow=10)
        # insignia
        fb = font(F_BLACK, int(H * 0.08))
        tw = text_size(fb, spec["sub"])[0]
        rounded_box(img, (x, int(H * 0.07), x + tw + 40, int(H * 0.07) + int(H * 0.11)), 14, MAGENTA + (255,))
        ImageDraw.Draw(img).text((x + 20, int(H * 0.075)), spec["sub"], font=fb, fill=WHITE)
    else:
        size = 150
        f = font(F_BLACK_IT, size)
        while max(text_size(f, t1)[0], text_size(f, t2)[0]) > W * 0.88:
            size -= 6; f = font(F_BLACK_IT, size)
        draw_text_outline(img, (W // 2, 330), t1, f, fill=WHITE, ow=10, anchor="ma")
        draw_text_outline(img, (W // 2, 330 + int(size * 1.05)), t2, f, fill=YELLOW, ow=10, anchor="ma")
        fb = font(F_BLACK, 64)
        tw = text_size(fb, spec["sub"])[0]
        rounded_box(img, ((W - tw) // 2 - 30, 190, (W + tw) // 2 + 30, 290), 16, MAGENTA + (255,))
        ImageDraw.Draw(img).text((W // 2, 202), spec["sub"], font=fb, fill=WHITE, anchor="ma")
    # isotipo esquina
    m = pin_mark(int(H * 0.13) if not short else 140)
    img.alpha_composite(m, (W - m.width - 14, H - m.height - 10) if short else (int(W * 0.04), H - m.height - 14))
    return img.convert("RGB")


def text_layer(spec, W=1280, H=720):
    """Capa de texto transparente para superponer sobre una captura real."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    for x in range(int(W * 0.6)):
        gd.line([(x, 0), (x, H)], fill=(11, 15, 42, int(220 * (1 - x / (W * 0.6)))))
    img.alpha_composite(grad)
    t1, t2 = spec["texto"]
    size = int(H * 0.2); f = font(F_BLACK_IT, size)
    while max(text_size(f, t1)[0], text_size(f, t2)[0]) > W * 0.5 and size > 60:
        size -= 4; f = font(F_BLACK_IT, size)
    draw_text_outline(img, (int(W * 0.04), int(H * 0.2)), t1, f, ow=10)
    draw_text_outline(img, (int(W * 0.04), int(H * 0.2) + int(size * 1.05)), t2, f, fill=YELLOW, ow=10)
    fb = font(F_BLACK, int(H * 0.08)); tw = text_size(fb, spec["sub"])[0]
    rounded_box(img, (int(W * 0.04), int(H * 0.07), int(W * 0.04) + tw + 40, int(H * 0.18)), 14, MAGENTA + (255,))
    ImageDraw.Draw(img).text((int(W * 0.04) + 20, int(H * 0.075)), spec["sub"], font=fb, fill=WHITE)
    return img


# ---------------- RENDER ----------------
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2000:]); raise SystemExit(1)


def apply_final(v):
    """Convierte un vídeo en versión FINAL resuelta solo con gráficos propios."""
    import re as _re
    v["modo"] = "final"
    ov = FO.OV.get(v["id"], {})
    for sc in v["escenas"]:
        o = ov.get(sc["rotulo"], {})
        if "items" in o:
            sc["items"] = o["items"]
        if "chip" in o:
            sc["chip"] = o["chip"]
        if "esquema" in o:
            sc["esquema"] = o["esquema"]
        if sc["tipo"] != "GRAFICO":
            sc["visual"] = ("Gráfico animado propio (sustituye a: " + sc["visual"].rstrip(".") + "). "
                            + ("Esquema de regiones con " + sc["esquema"] + " resaltada. " if sc.get("esquema") and sc["esquema"] != "ALL" else "")
                            + ("Ítems que aparecen uno a uno: " + " / ".join(sc["items"]) if sc["items"] else "Rótulo animado"))
            sc["tipo"] = "GRAFICO"
            sc["nota"] = ""
    d = v["seo"]["descripcion"]
    if v.get("oficial"):
        d = d  # lleva material oficial: se respeta su pie de créditos
    else:
        d = _re.sub(r"Imágenes del juego:.*?no son imágenes del juego\.", FO.PIE_FINAL, d, flags=_re.S)
    d = _re.sub(r"Grabado en partida propia.*?no son imágenes del juego\.", FO.PIE_FINAL, d, flags=_re.S)
    if v["id"] in FO.SEO_EXTRA:
        a, b = FO.SEO_EXTRA[v["id"]]
        d = d.replace(a, b)
    v["seo"]["descripcion"] = d
    for k, st in FO.THUMB_FIX.get(v["id"], {}).items():
        v["miniaturas"][k]["estilo"] = st
        v["miniaturas"][k]["concepto"] = "Versión con gráficos de marca (sin imágenes del juego): " + v["miniaturas"][k]["concepto"]
    v.pop("grabacion", None)


def build(v):
    if v["id"] in FO.FINAL_IDS:
        apply_final(v)
    short = v["formato"] == "short"
    W, H = (1080, 1920) if short else (1920, 1080)
    final = v["modo"] == "final"
    base = os.path.join(ROOT, v["carpeta"])
    dirs = {k: os.path.join(base, k) for k in ["Guion", "Locucion", "Imagenes", "Prompts_Pika", "Subtitulos", "Miniatura", "Montaje", "SEO", "Video_Final"]}
    for p in dirs.values():
        os.makedirs(p, exist_ok=True)
    work = os.path.join("/tmp/claude-0/work", v["id"])
    shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
    vid = v["id"]
    print(f"== {vid} ({'Short' if short else 'Largo'}, {'final' if final else 'animatic'})")

    # 1. Locución guía por escena y tiempos
    pad = 0.30 if short else 0.45
    t = 0.0
    scene_wavs = []
    for i, sc in enumerate(v["escenas"]):
        wf = os.path.join(work, f"s{i:02d}.wav")
        if VOICE == "eleven":
            import eleven
            esc = v["escenas"]
            dur = eleven.synth(sc["texto"], wf, prev_text=esc[i - 1]["texto"] if i > 0 else None,
                               next_text=esc[i + 1]["texto"] if i + 1 < len(esc) else None)
        else:
            dur = audio.synth(sc["texto"], wf, CACHE)
        sc["voz_dur"] = dur
        sc["ini"] = t
        sc["dur"] = round(max(dur + pad, 2.0) + sc.get("hold", 0), 3)
        if final and not short and i == len(v["escenas"]) - 1:
            sc["dur"] = round(max(sc["dur"], 15.0), 3)
        sc["fin"] = t + sc["dur"]
        t = sc["fin"]
        scene_wavs.append(wf)
    total = t
    # concatenar voz con silencios
    lst = os.path.join(work, "voz.txt")
    with open(lst, "w") as fh:
        for i, sc in enumerate(v["escenas"]):
            sil = os.path.join(work, f"sil{i:02d}.wav")
            run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono", "-t", f"{sc['dur'] - sc['voz_dur']:.3f}", sil])
            fh.write(f"file '{scene_wavs[i]}'\nfile '{sil}'\n")
    voz = os.path.join(work, "voz.wav")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c:a", "pcm_s16le", voz])
    if VOICE == "eleven":
        for old in ("_locucion_guia_TTS.wav",):
            op = os.path.join(dirs["Locucion"], vid + old)
            if os.path.exists(op):
                os.remove(op)
        shutil.copy(voz, os.path.join(dirs["Locucion"], f"{vid}_locucion_final_Nico_ElevenLabs.wav"))
    else:
        shutil.copy(voz, os.path.join(dirs["Locucion"], f"{vid}_locucion_guia_TTS.wav"))

    # 2. Subtítulos
    maxc = 25 if short else 42
    subs = []
    for sc in v["escenas"]:
        chs = sub_chunks(sc["texto"], maxc)
        weights = [len(chunk_plain(c)) + 4 for c in chs]
        tot = sum(weights)
        st = sc["ini"] + 0.05
        speech = sc["voz_dur"] - 0.05
        sc["subs"] = []
        for c, wgt in zip(chs, weights):
            en = st + speech * wgt / tot
            subs.append((st, en, c))
            sc["subs"].append(chunk_plain(c).replace("\n", " / "))
            st = en
    with open(os.path.join(dirs["Subtitulos"], f"{vid}_subtitulos.srt"), "w", encoding="utf-8") as fh:
        for n, (a, b, c) in enumerate(subs, 1):
            fh.write(f"{n}\n{srt_t(a)} --> {srt_t(b - 0.02)}\n{chunk_plain(c)}\n\n")
    fs, mv = (78, 560) if short else (54, 60)
    ass = os.path.join(dirs["Subtitulos"], f"{vid}_subtitulos_estilo.ass")
    with open(ass, "w", encoding="utf-8") as fh:
        fh.write(f"""[Script Info]
Title: {vid} subtítulos Mapa Abierto
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Marca,Inter Display,{fs},&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,{5 if short else 4},{3 if short else 2},2,80,80,{mv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""")
        for a, b, c in subs:
            fh.write(f"Dialogue: 0,{ass_t(a)},{ass_t(b - 0.02)},Marca,,0,0,0,,{{\\fad(60,40)}}{chunk_ass(c)}\n")

    # 3. Imágenes de escena + clips
    concat = os.path.join(work, "clips.txt")
    img_dir = os.path.join(dirs["Imagenes"], "escenas")
    os.makedirs(img_dir, exist_ok=True)
    with open(concat, "w") as fh:
        for i, sc in enumerate(v["escenas"]):
            last = i == len(v["escenas"]) - 1
            im = scene_image(v, sc, i, W, H, final, last=last)
            p = os.path.join(img_dir, f"{vid}_escena_{i + 1:02d}.png")
            im.convert("RGB").save(p)
            total_frames = int(round(sc["dur"] * FPS))
            n = len(sc["items"]) if (final and sc["items"] and not last) else 0
            q = sc.get("quiz")
            if final and q and not q.get("reveal"):
                no = len(q["options"])
                hold_f = int(round(sc.get("hold", 0) * FPS))
                speak_f = total_frames - hold_f
                first = min(int(1.0 * FPS), speak_f // (no + 2))
                per = (speak_f - first) // no
                stage_frames = [first] + [per] * no
                stage_frames[-1] += speak_f - sum(stage_frames)
                stage_imgs = [scene_image(v, sc, i, W, H, final, n_items=k) for k in range(no + 1)]
                secs = int(round(sc.get("hold", 0)))
                for c in range(secs, 0, -1):
                    stage_frames.append(FPS)
                    stage_imgs.append(scene_image(v, sc, i, W, H, final, countdown=c))
                stage_frames[-1] += total_frames - sum(stage_frames)
            elif final and sc.get("stamp"):
                first = int(0.35 * FPS)
                stage_frames = [first, total_frames - first]
                stage_imgs = [scene_image(v, sc, i, W, H, final, stamp_on=False), im]
            elif n:
                first = min(int(0.9 * FPS), total_frames // (n + 2))
                rest = total_frames - first
                stage_frames = [first] + [rest // n] * n
                stage_frames[-1] += total_frames - sum(stage_frames)
                stage_imgs = [scene_image(v, sc, i, W, H, final, n_items=k) for k in range(n + 1)]
            else:
                stage_frames = [total_frames]; stage_imgs = [im]
            zin = i % 2 == 0
            off = 0
            if final and sc.get("clip"):
                src, start = sc["clip"][:2]
                vel = sc["clip"][2] if len(sc["clip"]) > 2 else 1.0
                fxc = sc.get("fx", 0.5)
                srcpath = (os.environ.get("MA_RK_RELAY", "http://127.0.0.1:8765") + "/GTAVI_An_Extended_Look/GTAVI_An_Extended_Look.mp4") if src == "EL" else os.path.join(RK_DIR, src)
                ov = os.path.join(work, f"ov{i:02d}.png")
                scene_image(v, sc, i, W, H, final, clip_overlay=True).save(ov)
                scale = (f"crop=iw:iw/2,scale=-2:{H},crop={W}:{H}:(iw-{W})*{fxc}:0" if short else f"crop=iw:iw/2,scale={W}:-2,pad={W}:{H}:0:(oh-ih)/2") if "Trailer" in src else (f"scale=-2:{H},crop={W}:{H}:(iw-{W})*{fxc}:0" if short else f"scale={W}:{H}")
                scale += f",setpts={vel}*PTS,tpad=stop_mode=clone:stop_duration={sc['dur']:.3f}"
                clip = os.path.join(work, f"c{i:02d}_clip.mp4")
                run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(start), "-t", f"{sc['dur']/vel:.3f}", "-i", srcpath,
                     "-loop", "1", "-i", ov, "-filter_complex", f"[0:v]{scale},fps={FPS},setsar=1[b];[b][1:v]overlay=0:0:shortest=1,format=yuv420p",
                     "-frames:v", str(total_frames), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), clip])
                fh.write(f"file '{clip}'\n")
                continue
            for k, (fr_n, simg) in enumerate(zip(stage_frames, stage_imgs)):
                big = os.path.join(work, f"big{i:02d}_{k}.png")
                simg.convert("RGB").resize((int(W * 1.2), int(H * 1.2)), Image.LANCZOS).save(big)
                z = f"min(1+0.0009*(on+{off}),1.12)" if zin else f"max(1.12-0.0009*(on+{off}),1.0)"
                clip = os.path.join(work, f"c{i:02d}_{k}.mp4")
                run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", big, "-frames:v", str(fr_n), "-vf",
                     f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={fr_n}:s={W}x{H}:fps={FPS},format=yuv420p",
                     "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", str(FPS), clip])
                fh.write(f"file '{clip}'\n")
                off += fr_n
    if vid == "V03":
        esquema_regiones().convert("RGB").save(os.path.join(dirs["Imagenes"], "V03_esquema_regiones_NO_OFICIAL.png"))
    silent = os.path.join(work, "silent.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", concat, "-c", "copy", silent])

    # 4. Mezcla de audio: voz + música (-22 dB aprox) + whoosh en cambios de escena
    music = os.path.join(AUD_DIR, "Musica", "MapaAbierto_synthwave_bed.wav")
    if final:
        music = os.path.join(work, "music.wav")
        audio.music_bed(total + 1.0, music)
    wh = os.path.join(AUD_DIR, "SFX", "whoosh.wav")
    delays = [int(sc["ini"] * 1000) for sc in v["escenas"][1:]]
    inputs = ["-i", voz, "-stream_loop", "-1", "-i", music]
    flt = ["[0:a]aformat=channel_layouts=stereo,volume=1.0[v]", f"[1:a]atrim=0:{total:.3f},volume=0.10[m]"]
    mix = "[v][m]"
    n_in = 2
    for k, dl in enumerate(delays[:60]):
        inputs += ["-i", wh]
        flt.append(f"[{n_in}:a]adelay={dl}|{dl},volume=0.25[w{k}]")
        mix += f"[w{k}]"
        n_in += 1
    flt.append(f"{mix}amix=inputs={n_in}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
    mixwav = os.path.join(work, "mix.wav")
    run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(flt), "-map", "[a]", "-ar", "48000", mixwav])

    # 5. Exportación final
    name = f"{vid}_{'FINAL' if final else 'ANIMATIC_borrador'}_{'1080x1920' if short else '1920x1080'}.mp4"
    out = os.path.join(dirs["Video_Final"], name)
    assp = ass.replace("\\", "/").replace(":", "\\:")
    if v.get("barra"):
        vf = ["-f", "lavfi", "-i", f"color=c=0xFF2E88:s={W}x12:r={FPS}:d={total + 1:.2f}",
              "-filter_complex", f"[0:v]ass='{assp}'[b];[b][2:v]overlay=x='-W+W*t/{total:.3f}':y=0:eval=frame:shortest=1[vo]",
              "-map", "[vo]", "-map", "1:a"]
    else:
        vf = ["-vf", f"ass='{assp}'"]
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", mixwav] + vf + ["-c:v", "libx264", "-preset", "medium",
         "-crf", "19", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
         "-shortest", out])
    v["_out"] = out
    v["_total"] = total

    # 6. Miniaturas
    if short:
        th = thumb(v["miniaturas"][0], 1080, 1920, idx_seed=2)
        th.save(os.path.join(dirs["Miniatura"], f"{vid}_portada_short_1080x1920.png"))
    else:
        for k, spec in enumerate(v["miniaturas"]):
            tag = "ABC"[k]
            el = "_ELEGIDA" if k == v["mini_elegida"] else ""
            thumb(spec, 1280, 720, idx_seed=k).save(os.path.join(dirs["Miniatura"], f"{vid}_miniatura_{tag}{el}_1280x720.png"))
            if spec["estilo"] in ("oficial", "gameplay"):
                text_layer(spec).save(os.path.join(dirs["Miniatura"], f"{vid}_miniatura_{tag}_capa_texto_transparente.png"))
    write_docs(v, dirs, W, H, total, subs, final)
    return v


def write_docs(v, dirs, W, H, total, subs, final):
    vid = v["id"]; short = v["formato"] == "short"
    ar = "9:16" if short else "16:9"
    c = v["concepto"]
    words = sum(len(sc["texto"].replace("*", "").split()) for sc in v["escenas"])
    # GUION
    g = [f"# {vid} · {v['tema']}\n", f"**Formato:** {'YouTube Short' if short else 'Vídeo largo'} · {ar} · duración de la locución guía: **{mmss(total)}** ({words} palabras)\n",
         "## A. Concepto\n", f"- **Temática:** {c['tematica']}", f"- **Público objetivo:** {c['publico']}", f"- **Intención de búsqueda:** {c['intencion']}",
         f"- **Por qué haría clic:** {c['clic']}", f"- **Duración recomendada:** {c['duracion']}", f"- **Objetivo:** {c['objetivo']}\n",
         "## B. Títulos\n", "| # | Título | Caract. |", "|---|---|---|"]
    for k, tt in enumerate(v["titulos"]):
        g.append(f"| {k + 1}{' ✅' if k == v['elegido'] else ''} | {tt} | {len(tt)} |")
    g += [f"\n**Elegido:** {v['titulos'][v['elegido']]}\n", f"**Por qué:** {v['justificacion']}\n", "## C. Guion completo (narración palabra por palabra)\n",
          "> Las *palabras entre asteriscos* se enfatizan en voz y se destacan en amarillo en los subtítulos. Los textos entre [CORCHETES] son huecos que SOLO pueden rellenarse tras jugar: no publicar con ellos.\n"]
    cap_n = 0
    for i, sc in enumerate(v["escenas"]):
        if sc["cap"]:
            g.append(f"\n### {sc['cap']}\n")
        g.append(f"**[{mmss(sc['ini'])}] Escena {i + 1} · {TIPO_TXT[sc['tipo']]}**  ")
        g.append(f"{sc['texto']}\n")
        if sc["nota"]:
            g.append(f"> ⚠️ Nota de producción: {sc['nota']}\n")
    open(os.path.join(dirs["Guion"], f"{vid}_guion_completo.md"), "w").write("\n".join(g))

    # LOCUCIÓN
    clean = "\n\n".join(sc["texto"].replace("*", "") for sc in v["escenas"])
    open(os.path.join(dirs["Locucion"], f"{vid}_locucion_texto_limpio.txt"), "w").write(clean + "\n")
    ssml = []
    for sc in v["escenas"]:
        tx = re.sub(r"\*([^*]+)\*", lambda m: m.group(1).upper() if len(m.group(1)) < 30 else m.group(1), sc["texto"])
        ssml.append(tx + ' <break time="0.4s" />')
    open(os.path.join(dirs["Locucion"], f"{vid}_locucion_ElevenLabs.txt"), "w").write(
        "# Pegar en ElevenLabs (modelo multilingüe). Las MAYÚSCULAS marcan énfasis; <break> son pausas.\n"
        "# Ajustes: Stability 45 · Similarity 80 · Style 20 · Speaker boost ON. Velocidad 1.05.\n\n" + "\n\n".join(ssml) + "\n")
    # FICHA DE VOZ
    open(os.path.join(dirs["Locucion"], f"{vid}_ficha_de_voz.md"), "w").write(f"""# Ficha de voz · {vid}

Identidad de narrador común a los 10 vídeos: **"La voz de Mapa Abierto"** (ver `01_IDENTIDAD_VISUAL/guia_de_marca.md`).

| Parámetro | Indicación |
|---|---|
| Tipo de voz | Masculina o femenina adulta (25-35 años), timbre medio-grave, cálida. Elegir UNA y mantenerla en todo el canal |
| Acento | Castellano de España (peninsular, neutro, sin seseo) |
| Tono | Cercano y seguro, de presentador de noticias de videojuegos; entusiasmo contenido, nunca gritón |
| Velocidad | {'165-175 ppm (Short: ritmo alto, sin respirar en los 2 primeros segundos)' if short else '150-160 ppm; bajar a 140 ppm en datos clave (horas, cifras)'} |
| Entonación | Frases afirmativas que caen al final; preguntas retóricas con subida clara; evitar el "tonito" de anuncio |
| Pausas | 0,3 s entre frases; 0,6 s antes de cada cambio de bloque/capítulo; pausa de 0,4 s DESPUÉS de cada cifra importante |
| Énfasis | Palabras marcadas con *asteriscos* en el guion (en MAYÚSCULAS en el archivo para ElevenLabs) |
| Cifras | Leer "79,99" como "setenta y nueve con noventa y nueve"; "210 GB" como "doscientos diez gigas" |
| Nombres | Jason = "Yéison"; Lucia = "Lucía"; Vice City = "Vais Síti"; Grassrivers = "Gras-ríver"; Mount Kalaga = "Maunt Kalága" |

## Archivos
- `{vid}_locucion_texto_limpio.txt` → texto íntegro, sin marcas.
- `{vid}_locucion_ElevenLabs.txt` → texto con énfasis y pausas para ElevenLabs.
{('- `' + vid + '_locucion_final_Nico_ElevenLabs.wav` → **locución final** generada con ElevenLabs (voz Nico - History & Documentary, castellano peninsular, modelo eleven_v4). Es la pista que lleva el MP4.') if VOICE == 'eleven' else ('- `' + vid + '_locucion_guia_TTS.wav` → locución guía (Piper, voz carlfm, dominio público): solo para cuadrar tiempos; sustituir por la voz final.')}
""")

    # PROMPTS PIKA
    pk = [f"# Prompts Pika · {vid} ({ar})\n", f"Estilo global obligatorio (ya incluido en cada prompt): _{STYLE}_\n",
          "**Cómo usar:** generar cada escena por separado, clips de 3-4 s, 2-3 variaciones (seeds distintas) y elegir la mejor. Si la escena dura más, encadenar variaciones con fundido de 6 fotogramas.",
          "**Regla:** todo clip IA se rotula 'Recreación IA' en pantalla y NUNCA se presenta como imagen del juego. Revisar manos, caras y coches deformados antes de usar.\n"]
    txt = []
    for i, sc in enumerate(v["escenas"]):
        p, params, uso = pika_prompt(v, sc, i)
        sc["pika"] = p
        n_clips = max(1, int(round(sc["dur"] / 3.5)))
        pk += [f"## Escena {i + 1} · {mmss(sc['ini'])}–{mmss(sc['fin'])} ({sc['dur']:.1f} s) · {TIPO_TXT[sc['tipo']]}",
               f"- **Uso:** {uso}", f"- **Clips a generar:** {n_clips} × 3-4 s", "```", p, "```", f"Parámetros: `{params}`\n"]
        txt.append(f"[{vid} E{i + 1:02d}] {p} {params}")
    open(os.path.join(dirs["Prompts_Pika"], f"{vid}_prompts_pika.md"), "w").write("\n".join(pk))
    open(os.path.join(dirs["Prompts_Pika"], f"{vid}_prompts_pika_copiar_pegar.txt"), "w").write("\n\n".join(txt) + "\n")

    # LÍNEA DE TIEMPO (CSV + MD)
    cols = ["Escena", "Inicio_s", "Fin_s", "Duracion_s", "Inicio_mmss", "Fuente", "Contenido_visual", "Movimiento_camara", "Iluminacion", "Animaciones",
            "Transicion", "Efectos_sonido", "Narracion", "Subtitulos", "Rotulo_en_pantalla", "Nota"]
    with open(os.path.join(dirs["Montaje"], f"{vid}_timeline_edicion.csv"), "w", newline="", encoding="utf-8") as fh:
        wcsv = csv.writer(fh)
        wcsv.writerow(cols)
        for i, sc in enumerate(v["escenas"]):
            luz = LOOKS[sc["look"]]["light"] if sc["look"] else LUZ_MARCA
            wcsv.writerow([i + 1, f"{sc['ini']:.2f}", f"{sc['fin']:.2f}", f"{sc['dur']:.2f}", mmss(sc["ini"]), TIPO_TXT[sc["tipo"]], sc["visual"],
                           sc["cam"], luz, ANIM_TXT[sc["tipo"]], sc["trans"], sc["sfx"], sc["texto"].replace("*", ""), " | ".join(sc["subs"]), sc["rotulo"], sc["nota"]])
    md = [f"# Línea de tiempo de edición · {vid} · {v['titulos'][v['elegido']]}\n",
          f"**Proyecto:** {W}×{H} · {FPS} fps · duración total {mmss(total)} · {'Short 9:16' if short else '16:9'}\n",
          "## Pistas (de arriba abajo)",
          "| Pista | Contenido |", "|---|---|",
          "| V4 | Rótulos y textos en movimiento (plantillas de marca) |",
          "| V3 | Subtítulos (importar `.ass` en DaVinci/Premiere o `.srt` + estilo en CapCut) |",
          "| V2 | Gráficos / etiquetas ('Fuente: Rockstar Games', 'Recreación IA', 'Gameplay propio') |",
          "| V1 | Imagen principal: material oficial, gameplay, clips Pika o gráficos (PNG en `Imagenes/escenas/`) |",
          "| A1 | Locución (final; la guía TTS sirve de referencia de tiempos) |",
          "| A2 | Música de marca `05_RECURSOS_AUDIO/Musica/` a −22 dB bajo voz (ducking automático −6 dB) |",
          "| A3 | Efectos de sonido (`05_RECURSOS_AUDIO/SFX/`) a −18 dB |\n",
          "## Reglas de estilo de montaje",
          "- Cambio visual cada 3-5 s como máximo (en Shorts, cada 1,5-3 s): alternar plano, zoom de énfasis o rótulo.",
          "- Zoom cinematográfico: 100→108 % en planos estáticos; zoom de énfasis 100→115 % en 6 fotogramas sobre el detalle comentado.",
          "- Transiciones: corte seco por defecto; whip pan solo en cambios de bloque; nada de transiciones 3D ni efectos de estrellas.",
          "- Texto en pantalla: InterDisplay Black Italic, blanco con contorno negro; palabra clave en amarillo #FFD666.",
          "- Material oficial: crédito 'Fuente: Rockstar Games' visible; fragmentos breves y siempre con comentario encima (uso informativo).",
          f"- Marca de agua: se configura en YouTube Studio (no incrustar). Pantalla final: {'—' if short else 'últimos 20 s con `01_IDENTIDAD_VISUAL/Intro_Outro/pantalla_final_1920x1080.png`'}.\n",
          "## Escenas\n"]
    for i, sc in enumerate(v["escenas"]):
        luz = LOOKS[sc["look"]]["light"] if sc["look"] else LUZ_MARCA
        md += [f"### Escena {i + 1} · {sc['ini']:.2f} s → {sc['fin']:.2f} s ({sc['dur']:.2f} s) · `{mmss(sc['ini'])}`",
               f"| Campo | Detalle |", "|---|---|",
               f"| Fuente | {TIPO_TXT[sc['tipo']]} |", f"| Contenido visual | {sc['visual']} |", f"| Cámara | {sc['cam']} |",
               f"| Iluminación | {luz} |", f"| Animaciones | {ANIM_TXT[sc['tipo']]} |", f"| Transición de salida | {sc['trans']} |",
               f"| Efectos de sonido | {sc['sfx']} |", f"| Rótulo | **{sc['rotulo']}** |", f"| Narración | {sc['texto'].replace('*', '')} |",
               f"| Subtítulos | {' · '.join(sc['subs'])} |", f"| Imagen de referencia | `Imagenes/escenas/{vid}_escena_{i + 1:02d}.png` |",
               f"| Prompt Pika | ver `Prompts_Pika/{vid}_prompts_pika.md` · escena {i + 1} |"]
        if sc["nota"]:
            md.append(f"| ⚠️ Nota | {sc['nota']} |")
        md.append("")
    md += ["## Instrucciones por programa",
           "**DaVinci Resolve:** Proyecto " + f"{W}×{H} {FPS} fps → importar PNG de escenas y la locución → colocar según la tabla (Inicio_s) → Fusion: título 'Text+' con la fuente de marca → Fairlight: ducking con 'Sidechain' de A1 a A2 → File › Import › Subtitle (`.srt`) o usar el `.ass` quemado vía Fusion → Deliver: H.264, {W}×{H}, {FPS} fps, 16-20 Mbps (largo) / 12 Mbps (Short), AAC 320 kbps.",
           "**Premiere Pro:** Secuencia personalizada " + f"{W}×{H} {FPS} fps → Archivo › Importar el CSV como referencia de marcadores (copiar Inicio_mmss) → Gráficos esenciales para rótulos → Subtítulos: importar `.srt` y aplicar estilo de marca → Audio esencial: Música con 'Atenuación' automática → Exportar H.264 'Coincidir con origen - Alta velocidad de bits'.",
           f"**CapCut:** Lienzo {ar} → añadir PNG/clips en el orden de la tabla ajustando duraciones → Texto › Subtítulos automáticos (revisar con el `.srt`) o importar `.srt` → estilo: blanco, contorno negro 8, sombra → Audio: música −22 dB → Exportar 1080p, {FPS} fps, alta calidad.\n"]
    open(os.path.join(dirs["Montaje"], f"{vid}_timeline_edicion.md"), "w").write("\n".join(md))
    if v.get("grabacion"):
        open(os.path.join(dirs["Montaje"], f"{vid}_lista_de_grabacion.md"), "w").write(
            f"# Lista de grabación · {vid}\n\nGrabar tras el desbloqueo (19/11, 00:00). Capturadora o grabación de la consola a máxima calidad, 60 fps si es posible, HUD visible salvo en planos de ambiente.\n\n"
            + "\n".join(f"- [ ] {x}" for x in v["grabacion"]) + "\n\n**Prohibido:** usar clips IA o capturas de terceros como si fueran gameplay propio. Si un plano no se consigue, sustituir por gráfico de marca.\n")
    caps = [(sc["ini"], sc["cap"]) for sc in v["escenas"] if sc["cap"]]
    if not short:
        caps = [(0.0, "Introducción")] + [c for c in caps if c[0] > 0]
        open(os.path.join(dirs["Montaje"], f"{vid}_capitulos.txt"), "w").write("\n".join(f"{int(a // 60)}:{int(a % 60):02d} {b}" for a, b in caps) + "\n")

    # SEO
    s = v["seo"]
    caps_txt = ""
    if not short:
        caps_txt = "\n\n⏱️ Capítulos\n" + "\n".join(f"{int(a // 60)}:{int(a % 60):02d} {b}" for a, b in caps)
    desc = s["descripcion"] + caps_txt + "\n\n" + " ".join(s["hashtags"])
    open(os.path.join(dirs["SEO"], f"{vid}_descripcion_youtube.txt"), "w").write(desc + "\n")
    seo_md = [f"# SEO y publicación · {vid}\n", f"**Título definitivo:** {v['titulos'][v['elegido']]}\n",
              f"**Fecha y hora recomendadas:** {s['fecha']}\n", f"**Categoría:** {s['categoria']}  ", f"**Lista de reproducción:** {s['playlist']}  ",
              f"**Formato:** {'Short (vertical, ≤60 s)' if short else 'Vídeo largo'}  ", "**Idioma del vídeo / subtítulos:** Español (España) · subir el `.srt` como 'Español (España)'\n",
              "## Descripción (copiar y pegar)\n", "```", desc, "```\n", "## Palabras clave principales", ", ".join(s["keywords"]) + "\n",
              "## Etiquetas", ", ".join(s["tags"]) + f"\n\n({len(', '.join(s['tags']))} caracteres; límite 500)\n", "## Hashtags", " ".join(s["hashtags"]) + "\n",
              "## Comentario fijado", s["comentario"] + "\n",
              "## Ajustes de subida", "- Contenido alterado o sintético: **Sí** si se usan clips IA realistas (casilla de divulgación de YouTube).",
              "- Público: no creado para niños. Restricción de edad: no (sin violencia explícita en miniatura).",
              "- Tarjetas: en el 60 % del vídeo, tarjeta al vídeo relacionado de la misma lista.", "- Licencia: estándar de YouTube."]
    if not short:
        seo_md.insert(7, "## Capítulos\n```\n" + "\n".join(f"{int(a // 60)}:{int(a % 60):02d} {b}" for a, b in caps) + "\n```\n")
    open(os.path.join(dirs["SEO"], f"{vid}_seo.md"), "w").write("\n".join(seo_md))

    # MINIATURAS
    mm = [f"# Miniaturas · {vid}\n"]
    for k, spec in enumerate(v["miniaturas"]):
        mm += [f"## Propuesta {'ABC'[k]}{' ✅ ELEGIDA' if k == v['mini_elegida'] else ''}", f"- Texto: **{' '.join(spec['texto'])}** + insignia '{spec['sub']}'",
               f"- Concepto: {spec['concepto']}", f"- Requiere captura real: {'Sí (usar la capa de texto transparente sobre la captura)' if spec['estilo'] in ('oficial', 'gameplay') else 'No, lista para subir'}\n"]
    mm.append(f"**Motivo de la elección:** {v['mini_motivo']}\n\nTodas: 1280×720 (Short: 1080×1920), texto 2-5 palabras, contraste alto, legible a 120 px de ancho. Comprobar en `04_CONTROL_CALIDAD/` la vista reducida.")
    open(os.path.join(dirs["Miniatura"], f"{vid}_miniaturas_propuestas.md"), "w").write("\n".join(mm))

    # LEEME del vídeo final
    open(os.path.join(dirs["Video_Final"], "LEEME.md"), "w").write(
        f"# {vid} · Vídeo\n\n" + (
            f"`{os.path.basename(v['_out'])}` es la **versión FINAL publicable** en formato motion graphics: todos los elementos visuales son gráficos propios de la marca (sin imágenes del juego ni IA), música original y subtítulos incrustados.\n\n"
            + ("Voz final: Nico (ElevenLabs). Listo para publicar.\n" if VOICE == "eleven" else "⚠️ La voz es la **locución guía TTS** (calidad limitada): sustituir por la voz final antes de publicar.\n")
            if final else
            f"`{os.path.basename(v['_out'])}` es un **ANIMATIC / BORRADOR DE MONTAJE**, no el vídeo final. Contiene los tiempos exactos, la locución guía, la música, los subtítulos y una tarjeta por escena que indica qué va en cada hueco (material oficial, clip Pika o gameplay propio).\n\n"
            "Para terminarlo: sustituir cada tarjeta por el material indicado siguiendo `Montaje/{vid}_timeline_edicion.md`, sustituir la locución guía por la voz final y exportar con los ajustes de `04_CONTROL_CALIDAD/`.\n"))


def prepare_audio_assets():
    os.makedirs(os.path.join(AUD_DIR, "Musica"), exist_ok=True)
    os.makedirs(os.path.join(AUD_DIR, "SFX"), exist_ok=True)
    m = os.path.join(AUD_DIR, "Musica", "MapaAbierto_synthwave_bed.wav")
    if not os.path.exists(m):
        audio.music_bed(80, m)
    w = os.path.join(AUD_DIR, "SFX", "whoosh.wav")
    if not os.path.exists(w):
        audio.whoosh(w)
    s = os.path.join(AUD_DIR, "SFX", "sting_marca.wav")
    if not os.path.exists(s):
        audio.sting(s)


if __name__ == "__main__":
    prepare_audio_assets()
    meta = []
    for v in VIDEOS:
        if ONLY and v["id"] not in ONLY:
            continue
        build(v)
        meta.append(dict(id=v["id"], titulo=v["titulos"][v["elegido"]], formato=v["formato"], modo=v["modo"], dur=round(v["_total"], 2),
                         out=os.path.relpath(v["_out"], ROOT), fecha=v["seo"]["fecha"], carpeta=v["carpeta"]))
    mp = os.path.join(ROOT, "_build", "meta.json")
    old = json.load(open(mp)) if os.path.exists(mp) else []
    ids = {m["id"] for m in meta}
    allm = sorted([m for m in old if m["id"] not in ids] + meta, key=lambda m: m["id"])
    json.dump(allm, open(mp, "w"), ensure_ascii=False, indent=1)
    print("OK", [m["id"] for m in meta])
