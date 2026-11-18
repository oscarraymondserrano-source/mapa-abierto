import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gfx import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ID = os.path.join(ROOT, "01_IDENTIDAD_VISUAL")
for sub in ["Logotipo", "Perfil", "Banner", "Marca_de_agua", "Plantillas", "Intro_Outro"]:
    os.makedirs(os.path.join(ID, sub), exist_ok=True)

# 1. Isotipo
mark = pin_mark(1024)
mark.save(os.path.join(ID, "Logotipo", "MapaAbierto_isotipo_1024.png"))

# 2. Logotipo horizontal (transparente y sobre fondo)
for bg_name, bg in [("transparente", None), ("fondo_oscuro", NAVY)]:
    W, H = 2400, 800
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0) if bg is None else bg + (255,))
    m = pin_mark(640)
    img.alpha_composite(m, (60, 80))
    wordmark(img, 720, 250, 230, tagline="NOTICIAS · GUÍAS · SECRETOS")
    img.save(os.path.join(ID, "Logotipo", f"MapaAbierto_logotipo_horizontal_{bg_name}.png"))

# 3. Logotipo vertical
W, H = 1600, 1600
img = sunset_scene(W, H, seed=7, palms=False, city=True, horizon=0.72, sun_r=330)
vignette(img, 0.6)
img.alpha_composite(pin_mark(700), (450, 130))
wordmark(img, W // 2, 1000, 190, anchor_center=True, tagline="NOTICIAS · GUÍAS · SECRETOS")
img.convert("RGB").save(os.path.join(ID, "Logotipo", "MapaAbierto_logotipo_vertical.png"))

# 4. Foto de perfil 800x800 (se recorta en círculo en YouTube)
P = 800
pf = vgradient(P, P, [(0, NIGHT), (0.6, PURPLE), (1, MAGENTA)]).convert("RGBA")
halo = Image.new("RGBA", (P, P), (0, 0, 0, 0))
ImageDraw.Draw(halo).ellipse([60, 60, P - 60, P - 60], outline=CYAN + (255,), width=10)
pf.alpha_composite(glow(halo, 12, 2))
pf.alpha_composite(pin_mark(600), (100, 95))
pf.convert("RGB").save(os.path.join(ID, "Perfil", "MapaAbierto_perfil_800x800.png"))
# vista previa circular
prev = pf.copy()
mask = Image.new("L", (P, P), 0)
ImageDraw.Draw(mask).ellipse([0, 0, P, P], fill=255)
prev.putalpha(mask)
prev.save(os.path.join(ID, "Perfil", "MapaAbierto_perfil_vista_previa_circular.png"))

# 5. Banner 2560x1440 con zona segura 1546x423 centrada
BW, BH = 2560, 1440
bn = sunset_scene(BW, BH, seed=11, horizon=0.66, sun_r=300)
vignette(bn, 0.35)
# zona segura: x 507..2053, y 508..931
bn.alpha_composite(pin_mark(360), (560, 535))
wordmark(bn, 960, 600, 150)
f = font(F_MONO, 44)
ImageDraw.Draw(bn).text((975, 805), "GTA VI · NOTICIAS · GUÍAS · SECRETOS", font=f, fill=CYAN)
f2 = font(F_BOLD, 40)
rounded_box(bn, (975, 870, 1745, 925), 14, (0, 0, 0, 150))
ImageDraw.Draw(bn).text((995, 876), "NUEVOS VÍDEOS CADA SEMANA · 19.11.2026", font=f2, fill=YELLOW)
bn.convert("RGB").save(os.path.join(ID, "Banner", "MapaAbierto_banner_2560x1440.png"))
# guía de zonas seguras
g = bn.copy()
d = ImageDraw.Draw(g)
d.rectangle([507, 508, 2053, 931], outline=(0, 255, 0), width=6)
d.rectangle([0, 509, 2560, 932], outline=(255, 255, 0), width=3)
d.text((520, 470), "ZONA SEGURA (todos los dispositivos) 1546x423", font=font(F_BOLD, 32), fill=(0, 255, 0))
g.convert("RGB").resize((1280, 720)).save(os.path.join(ID, "Banner", "guia_zonas_seguras_banner.png"))

# 6. Marca de agua 150x150 (PNG transparente)
wm = pin_mark(150)
wm.save(os.path.join(ID, "Marca_de_agua", "MapaAbierto_marca_agua_150x150.png"))
# versión 300 para calidad
pin_mark(300).save(os.path.join(ID, "Marca_de_agua", "MapaAbierto_marca_agua_300x300.png"))

# 7. Plantillas de miniatura (base vacía + guía)
T = sunset_scene(1280, 720, seed=5, horizon=0.7)
vignette(T, 0.5)
T.alpha_composite(pin_mark(90), (1170, 618))
T.convert("RGB").save(os.path.join(ID, "Plantillas", "plantilla_miniatura_fondo_1280x720.png"))
G = T.copy()
d = ImageDraw.Draw(G)
d.rectangle([40, 40, 640, 680], outline=(0, 255, 0), width=4)
d.text((52, 50), "ZONA TEXTO (2-5 palabras)", font=font(F_BOLD, 28), fill=(0, 255, 0))
d.rectangle([680, 40, 1240, 680], outline=(255, 255, 0), width=4)
d.text((692, 50), "PUNTO FOCAL: captura oficial / personaje", font=font(F_BOLD, 24), fill=(255, 255, 0))
d.rectangle([1090, 610, 1280, 720], outline=(255, 0, 0), width=4)
d.text((1000, 575), "NO USAR: duración", font=font(F_BOLD, 22), fill=(255, 80, 80))
G.convert("RGB").save(os.path.join(ID, "Plantillas", "plantilla_miniatura_guia_1280x720.png"))

# 8. Fondo para Shorts y tarjeta de pantalla final
S = sunset_scene(1080, 1920, seed=9, horizon=0.62, sun_r=330)
vignette(S, 0.45)
S.convert("RGB").save(os.path.join(ID, "Plantillas", "fondo_shorts_1080x1920.png"))

E = sunset_scene(1920, 1080, seed=13, horizon=0.72)
vignette(E, 0.6)
d = ImageDraw.Draw(E)
for (x, y, w, h) in [(110, 260, 760, 428), (1050, 260, 760, 428)]:
    rounded_box(E, (x, y, x + w, y + h), 24, (0, 0, 0, 140), outline=CYAN + (255,), width=4)
    ImageDraw.Draw(E).text((x + w // 2, y + h // 2), "ELEMENTO DE PANTALLA FINAL\n(vídeo recomendado)", font=font(F_BOLD, 34),
                           fill=(255, 255, 255, 180), anchor="mm", align="center")
E.alpha_composite(pin_mark(200), (860, 760))
wordmark(E, 960, 120, 90, anchor_center=True)
E.convert("RGB").save(os.path.join(ID, "Intro_Outro", "pantalla_final_1920x1080.png"))
print("identidad ok")
