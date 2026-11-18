"""Librería gráfica común de la marca MAPA ABIERTO (paleta, tipografías y elementos)."""
import math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

# ---------- PALETA ----------
NAVY = (11, 15, 42)
NIGHT = (20, 16, 58)
PURPLE = (88, 28, 160)
MAGENTA = (255, 46, 136)
CYAN = (34, 211, 238)
ORANGE = (255, 138, 61)
YELLOW = (255, 214, 102)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FD = "/usr/share/fonts/opentype/inter/"
F_BLACK = FD + "InterDisplay-Black.otf"
F_BLACK_IT = FD + "InterDisplay-BlackItalic.otf"
F_XBOLD = FD + "InterDisplay-ExtraBold.otf"
F_BOLD = FD + "InterDisplay-Bold.otf"
F_SEMI = FD + "InterDisplay-SemiBold.otf"
F_MED = FD + "InterDisplay-Medium.otf"
F_MONO = "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-ExtraBold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(len(a)))


def vgradient(w, h, stops):
    """stops: lista de (pos 0..1, color)."""
    img = Image.new("RGB", (w, h))
    px = img.load()
    col = []
    for y in range(h):
        t = y / max(1, h - 1)
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]
            p1, c1 = stops[i + 1]
            if p0 <= t <= p1:
                col.append(lerp(c0, c1, (t - p0) / max(1e-6, p1 - p0)))
                break
        else:
            col.append(stops[-1][1])
    d = ImageDraw.Draw(img)
    for y, c in enumerate(col):
        d.line([(0, y), (w, y)], fill=c)
    return img


def glow(layer, radius, strength=2):
    """Devuelve el layer RGBA con resplandor añadido."""
    g = layer.filter(ImageFilter.GaussianBlur(radius))
    out = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    for _ in range(strength):
        out = Image.alpha_composite(out, g)
    return Image.alpha_composite(out, layer)


def striped_sun(d_img, cx, cy, r, top=YELLOW, bottom=MAGENTA, stripes=6):
    """Sol de atardecer con franjas horizontales (motivo retro genérico)."""
    w, h = d_img.size
    sun = vgradient(2 * r, 2 * r, [(0, top), (0.55, ORANGE), (1, bottom)]).convert("RGBA")
    mask = Image.new("L", (2 * r, 2 * r), 0)
    md = ImageDraw.Draw(mask)
    md.ellipse([0, 0, 2 * r - 1, 2 * r - 1], fill=255)
    for i in range(stripes):
        y0 = int(r * 1.05 + i * (r * 0.95 / stripes))
        th = max(2, int(r * 0.025 * (i + 1)))
        md.rectangle([0, y0, 2 * r, y0 + th], fill=0)
    sun.putalpha(mask)
    halo = Image.new("RGBA", d_img.size, (0, 0, 0, 0))
    hd = ImageDraw.Draw(halo)
    hd.ellipse([cx - r * 1.35, cy - r * 1.35, cx + r * 1.35, cy + r * 1.35], fill=MAGENTA + (90,))
    halo = halo.filter(ImageFilter.GaussianBlur(r * 0.35))
    d_img.alpha_composite(halo)
    d_img.alpha_composite(sun, (cx - r, cy - r))


def palm(draw, x, base_y, height, color=(8, 6, 22), lean=0.15, scale=1.0):
    """Silueta de palmera simple."""
    pts = []
    seg = 24
    for i in range(seg + 1):
        t = i / seg
        px = x + math.sin(t * 1.4) * height * lean
        py = base_y - t * height
        pts.append((px, py))
    for i in range(seg):
        wdt = int((10 - 5 * i / seg) * scale)
        draw.line([pts[i], pts[i + 1]], fill=color, width=max(2, wdt))
    tx, ty = pts[-1]
    for ang in [-170, -140, -110, -70, -40, -10, 20, 200]:
        a = math.radians(ang)
        L = height * 0.42
        fr = []
        for j in range(16):
            t = j / 15
            fx = tx + math.cos(a) * L * t
            fy = ty + math.sin(a) * L * t + (L * 0.45) * t * t
            fr.append((fx, fy))
        for j in range(15):
            draw.line([fr[j], fr[j + 1]], fill=color, width=max(2, int((9 - 7 * j / 15) * scale)))


def skyline(draw, w, base_y, maxh, color=(10, 8, 30), seed=3, windows=True):
    rnd = random.Random(seed)
    x = 0
    while x < w:
        bw = rnd.randint(int(w * 0.02), int(w * 0.06))
        bh = rnd.randint(int(maxh * 0.25), maxh)
        draw.rectangle([x, base_y - bh, x + bw, base_y], fill=color)
        if rnd.random() < 0.25:
            draw.rectangle([x + bw * 0.4, base_y - bh - maxh * 0.12, x + bw * 0.55, base_y - bh], fill=color)
        if windows:
            for wy in range(int(base_y - bh + 8), int(base_y - 6), 14):
                for wx in range(int(x + 5), int(x + bw - 5), 11):
                    if rnd.random() < 0.18:
                        c = rnd.choice([(255, 200, 120), (255, 120, 200), (120, 230, 255)])
                        draw.rectangle([wx, wy, wx + 4, wy + 5], fill=c)
        x += bw + rnd.randint(0, 6)


def neon_grid(img, horizon_y, color=MAGENTA, alpha=110):
    w, h = img.size
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    cx = w / 2
    for i in range(-24, 25):
        d.line([(cx + i * w * 0.012, horizon_y), (cx + i * w * 0.12, h)], fill=color + (alpha,), width=2)
    y = horizon_y
    step = 4
    while y < h:
        d.line([(0, y), (w, y)], fill=color + (alpha,), width=2)
        y += step
        step *= 1.32
    img.alpha_composite(glow(layer, 4, 1))


def sunset_scene(w, h, seed=1, sun=True, grid=True, palms=True, city=True, horizon=0.66, sun_r=None):
    img = vgradient(w, h, [(0, NAVY), (0.32, NIGHT), (0.52, PURPLE), (horizon - 0.02, MAGENTA), (horizon, ORANGE), (1, NAVY)]).convert("RGBA")
    hy = int(h * horizon)
    # estrellas
    rnd = random.Random(seed)
    d = ImageDraw.Draw(img)
    for _ in range(int(w * h / 9000)):
        sx, sy = rnd.randint(0, w), rnd.randint(0, int(h * 0.4))
        a = rnd.randint(80, 220)
        d.point((sx, sy), fill=(255, 255, 255, a))
    if sun:
        r = sun_r or int(min(w, h) * 0.24)
        striped_sun(img, int(w * 0.5), hy - int(r * 0.55), r)
    # suelo
    ground = vgradient(w, h - hy, [(0, (40, 10, 60)), (1, NAVY)]).convert("RGBA")
    img.alpha_composite(ground, (0, hy))
    if city:
        d = ImageDraw.Draw(img)
        skyline(d, w, hy, int(h * 0.2), seed=seed)
    if grid:
        neon_grid(img, hy)
    if palms:
        d = ImageDraw.Draw(img)
        palm(d, int(w * 0.07), h + 10, int(h * 0.75), lean=0.12, scale=max(1, w / 1280))
        palm(d, int(w * 0.93), h + 10, int(h * 0.68), lean=-0.14, scale=max(1, w / 1280))
    return img


def text_size(fnt, text):
    b = fnt.getbbox(text)
    return b[2] - b[0], b[3] - b[1], b


def draw_text_outline(img, xy, text, fnt, fill=WHITE, outline=BLACK, ow=6, shadow=True, anchor="la"):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    if shadow:
        sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).text((xy[0] + ow, xy[1] + ow * 1.3), text, font=fnt, fill=(0, 0, 0, 200), anchor=anchor,
                                 stroke_width=ow, stroke_fill=(0, 0, 0, 200))
        img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(ow)))
    d.text(xy, text, font=fnt, fill=fill, stroke_width=ow, stroke_fill=outline, anchor=anchor)
    img.alpha_composite(layer)


def neon_text(img, xy, text, fnt, color=CYAN, core=WHITE, radius=10, anchor="la", stroke=0):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text(xy, text, font=fnt, fill=color + (255,), anchor=anchor, stroke_width=stroke + 3, stroke_fill=color + (255,))
    g = layer.filter(ImageFilter.GaussianBlur(radius))
    img.alpha_composite(g)
    img.alpha_composite(g)
    d2 = ImageDraw.Draw(img)
    d2.text(xy, text, font=fnt, fill=core, anchor=anchor, stroke_width=stroke, stroke_fill=color)


def pin_mark(size, stroke=None):
    """Isotipo: chincheta de mapa con atardecer interior y contorno neón. RGBA cuadrado."""
    S = size * 4  # supersampling
    stroke = stroke or int(S * 0.045)
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    cx, cy, r = S / 2, S * 0.40, S * 0.30
    tip = (cx, S * 0.93)

    def pin_poly(rr, c_y, tip_y):
        pts = []
        ang0 = math.degrees(math.asin(rr / (tip_y - c_y)))
        for a in range(int(90 + ang0), int(450 - ang0) + 1, 2):
            pts.append((cx + rr * math.cos(math.radians(a)) * -1, c_y - rr * math.sin(math.radians(a)) * -1))
        pts.append((cx, tip_y))
        return pts

    poly = pin_poly(r, cy, tip[1])
    # relleno: atardecer
    fill = vgradient(S, S, [(0, NIGHT), (0.25, PURPLE), (0.45, MAGENTA), (0.6, ORANGE), (1, NAVY)]).convert("RGBA")
    m = Image.new("L", (S, S), 0)
    ImageDraw.Draw(m).polygon(poly, fill=255)
    inner = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    inner.paste(fill, (0, 0), m)
    # sol con franjas dentro
    sunl = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    striped_sun(sunl, int(cx), int(cy + r * 0.25), int(r * 0.62), stripes=4)
    sm = ImageChops.multiply(sunl.getchannel("A"), m)
    sunl.putalpha(sm)
    inner.alpha_composite(sunl)
    # horizonte y rejilla
    hz = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    hd = ImageDraw.Draw(hz)
    hy = cy + r * 0.32
    hd.rectangle([0, hy, S, S], fill=NAVY + (255,))
    for i in range(-8, 9):
        hd.line([(cx + i * S * 0.015, hy), (cx + i * S * 0.09, S)], fill=CYAN + (200,), width=int(S * 0.008))
    yy, st = hy, S * 0.02
    while yy < S:
        hd.line([(0, yy), (S, yy)], fill=CYAN + (200,), width=int(S * 0.008))
        yy += st
        st *= 1.5
    hz.putalpha(ImageChops.multiply(hz.getchannel("A"), m))
    inner.alpha_composite(hz)
    img.alpha_composite(inner)
    # contorno neón degradado magenta->cian
    ol = Image.new("L", (S, S), 0)
    ImageDraw.Draw(ol).line(poly + [poly[0]], fill=255, width=stroke, joint="curve")
    grad = Image.new("RGBA", (S, S))
    gd = ImageDraw.Draw(grad)
    for x in range(S):
        gd.line([(x, 0), (x, S)], fill=lerp(MAGENTA, CYAN, x / S) + (255,))
    outline = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    outline.paste(grad, (0, 0), ol)
    img = Image.alpha_composite(img, glow(outline, S * 0.02, 2))
    # punto blanco central (el "ojo" de la chincheta)
    d = ImageDraw.Draw(img)
    rr = r * 0.16
    d.ellipse([cx - rr, cy - r * 0.42 - rr, cx + rr, cy - r * 0.42 + rr], fill=WHITE, outline=CYAN, width=int(S * 0.012))
    return img.resize((size, size), Image.LANCZOS)


def wordmark(img, x, y, size, anchor_center=False, tagline=None):
    """Logotipo textual MAPA ABIERTO."""
    f1 = font(F_BLACK_IT, size)
    w1, h1, _ = text_size(f1, "MAPA ")
    w2, h2, _ = text_size(f1, "ABIERTO")
    total = w1 + w2
    if anchor_center:
        x = x - total // 2
    draw_text_outline(img, (x, y), "MAPA", f1, fill=WHITE, outline=NAVY, ow=max(2, size // 22), shadow=True)
    neon_text(img, (x + w1, y), "ABIERTO", f1, color=MAGENTA, core=(255, 235, 245), radius=max(4, size // 7))
    if tagline:
        ft = font(F_MONO, max(12, int(size * 0.26)))
        tw, th, _ = text_size(ft, tagline)
        tx = x + (total - tw) // 2
        ImageDraw.Draw(img).text((tx, y + int(size * 1.18)), tagline, font=ft, fill=CYAN)
    return total


def rounded_box(img, box, radius, fill, outline=None, width=0):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(box, radius, fill=fill, outline=outline, width=width)
    img.alpha_composite(layer)


def vignette(img, strength=0.55):
    w, h = img.size
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).ellipse([-w * 0.15, -h * 0.25, w * 1.15, h * 1.25], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(min(w, h) * 0.18))
    dark = Image.new("RGBA", (w, h), (0, 0, 0, int(255 * strength)))
    dark.putalpha(ImageChops.invert(m).point(lambda v: int(v * strength)))
    img.alpha_composite(dark)


def wrap(text, fnt, maxw):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if text_size(fnt, t)[0] <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines
