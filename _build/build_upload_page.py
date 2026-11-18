import os, sys, re, json, glob, io, base64, html
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
import build_calendar as cal
from build_videos import VIDEOS, apply_final, FO
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = sys.argv[1]
V = {v["id"]: v for v in VIDEOS}
for v in VIDEOS:
    if v["id"] in FO.FINAL_IDS:
        apply_final(v)
DOW = {"2026-11-17": "Martes 17/11", "2026-11-18": "Miércoles 18/11", "2026-11-19": "Jueves 19/11", "2026-11-20": "Viernes 20/11",
       "2026-11-21": "Sábado 21/11", "2026-11-22": "Domingo 22/11", "2026-11-23": "Lunes 23/11"}
items = []
for fecha, hora, vid, titulo, formato, estado in cal.PUB:
    if "FINAL" not in estado:
        continue
    v = V[vid]; base = os.path.join(ROOT, v["carpeta"])
    when = f"{DOW[fecha]} · {hora}"
    # sincronizar fecha en los archivos SEO
    for f in glob.glob(os.path.join(base, "SEO", "*_seo.md")) + glob.glob(f"/tmp/claude-0/pack2/MAPA_ABIERTO_LISTOS_PARA_SUBIR/{v['carpeta']}/*_seo.md"):
        s = open(f).read()
        s = re.sub(r"\*\*Fecha y hora recomendadas:\*\* .*", f"**Fecha y hora recomendadas:** {when} (hora peninsular)", s)
        s = re.sub(r"\*\*Título definitivo:\*\* .*", f"**Título definitivo:** {titulo}", s)
        open(f, "w").write(s)
    desc = open(glob.glob(os.path.join(base, "SEO", "*_descripcion_youtube.txt"))[0]).read().strip()
    mp4 = os.path.basename(glob.glob(os.path.join(base, "Video_Final", "*FINAL*.mp4"))[0])
    thumbs = glob.glob(os.path.join(base, "Miniatura", "*ELEGIDA*.png")) or glob.glob(os.path.join(base, "Miniatura", "*portada*.png"))
    im = Image.open(thumbs[0]).convert("RGB")
    im.thumbnail((240, 240))
    b = io.BytesIO(); im.save(b, "JPEG", quality=72)
    items.append(dict(id=vid, when=when, fecha=fecha, titulo=titulo, formato=formato, carpeta=v["carpeta"], mp4=mp4,
                      mini=os.path.basename(thumbs[0]) if formato == "Largo" else "", srt=f"{vid}_subtitulos.srt", desc=desc,
                      tags=", ".join(v["seo"]["tags"]), playlist=v["seo"]["playlist"], comentario=v["seo"]["comentario"],
                      img="data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode(), vertical=formato == "Short"))
tpl = open(os.path.join(os.path.dirname(__file__), "upload_page_template.html")).read()
open(OUT, "w").write(tpl.replace("__DATA__", json.dumps(items, ensure_ascii=False).replace("</", "<\\/")))
print(len(items), "vídeos")
