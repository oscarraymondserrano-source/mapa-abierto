import os, sys, math, subprocess, shutil
sys.path.insert(0, os.path.dirname(__file__))
from gfx import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "01_IDENTIDAD_VISUAL", "Intro_Outro")
AUD = os.path.join(ROOT, "05_RECURSOS_AUDIO")
work = "/tmp/claude-0/work/intro"
shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
W, H, FPS = 1920, 1080, 30
bg = sunset_scene(W, H, seed=31, horizon=0.7, sun_r=300)
vignette(bg, 0.5)
pin = pin_mark(420)
N = 75
for f in range(N):
    t = f / FPS
    img = bg.copy()
    # caída con rebote de la chincheta
    if t < 0.6:
        p = t / 0.6
        y = -420 + (300 + 420) * (1 - (1 - p) ** 3)
    elif t < 0.9:
        p = (t - 0.6) / 0.3
        y = 300 - 40 * math.sin(p * math.pi)
    else:
        y = 300
    x = W // 2 - 210 - int(min(1, max(0, (t - 1.0) / 0.4)) * 520)
    img.alpha_composite(pin, (x, int(y) - 150))
    if t > 1.1:
        a = min(1, (t - 1.1) / 0.35)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        wordmark(layer, 620, 400, 190, tagline="NOTICIAS · GUÍAS · SECRETOS")
        layer.putalpha(layer.getchannel("A").point(lambda v: int(v * a)))
        img.alpha_composite(layer)
    if 1.05 < t < 1.35:  # destello
        fl = Image.new("RGBA", (W, H), (255, 255, 255, int(160 * (1 - abs(t - 1.2) / 0.15))))
        img.alpha_composite(fl)
    if t > 2.2:
        img.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (t - 2.2) / 0.3))))
    img.convert("RGB").save(f"{work}/f{f:03d}.png")
sting = os.path.join(AUD, "SFX", "sting_marca.wav")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{work}/f%03d.png", "-i", sting, "-c:v", "libx264", "-crf", "18",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(OUT, "MapaAbierto_intro_sting_1920x1080.mp4")], check=True)
# pantalla final animada 20 s con música
music = os.path.join(AUD, "Musica", "MapaAbierto_synthwave_bed.wav")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", os.path.join(OUT, "pantalla_final_1920x1080.png"), "-ss", "40", "-i", music,
                "-t", "20", "-vf", "zoompan=z='min(1+0.0003*on,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=600:s=1920x1080:fps=30,fade=t=in:d=0.5,fade=t=out:st=19:d=1,format=yuv420p",
                "-af", "afade=t=in:d=0.5,afade=t=out:st=18:d=2,volume=0.6", "-c:v", "libx264", "-crf", "19", "-c:a", "aac", "-b:a", "192k",
                os.path.join(OUT, "MapaAbierto_pantalla_final_20s_1920x1080.mp4")], check=True)
print("intro/outro ok")
