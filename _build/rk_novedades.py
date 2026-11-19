"""Detecta material nuevo en la web de descargas de Rockstar (GTA VI) y lo descarga a RK_DIR.
Uso: python3 rk_novedades.py  ->  imprime NUEVO: <url> por cada archivo no visto y actualiza rk_assets_vistos.txt."""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
RK = os.environ.get("MA_RK", "/tmp/claude-0/rk_dl")
VISTOS = os.path.join(HERE, "rk_assets_vistos.txt")
html = subprocess.run(["curl", "-sL", "https://www.rockstargames.com/VI/downloads"], capture_output=True, text=True).stdout
urls = sorted(set("https://" + u for u in re.findall(r'media-rockstargames-com\.akamaized\.net/VI/downloads/[A-Za-z0-9_./-]+\.(?:mp4|zip)', html)))
if not urls:
    sys.exit("No se pudo leer la página de descargas (¿red?).")
vistos = set(open(VISTOS).read().split()) if os.path.exists(VISTOS) else set()
nuevos = [u for u in urls if u not in vistos]
os.makedirs(RK, exist_ok=True)
for u in nuevos:
    size = subprocess.run(["curl", "-sI", u], capture_output=True, text=True).stdout
    m = re.search(r"content-length:\s*(\d+)", size, re.I)
    mb = int(m.group(1)) // 2**20 if m else -1
    print(f"NUEVO: {u} ({mb} MB)")
    name = u.rsplit("/", 1)[1]
    if mb < 0 or mb > 1500:
        print("  (demasiado grande: usar por rangos como el Extended Look)")
        continue
    dst = os.path.join(RK, name)
    subprocess.run(["curl", "-sfL", "-o", dst, u], check=False)
    if name.endswith(".zip"):
        subprocess.run(["unzip", "-qo", dst, "-d", os.path.join(RK, "x_" + name[:-4])], check=False)
        os.remove(dst)
with open(VISTOS, "w") as f:
    f.write("\n".join(sorted(vistos | set(urls))) + "\n")
print(f"{len(urls)} archivos en la web; {len(nuevos)} nuevos.")
