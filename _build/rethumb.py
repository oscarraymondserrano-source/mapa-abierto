"""Regenera solo las miniaturas de los vídeos indicados (sin volver a renderizar)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_videos import VIDEOS, ROOT, thumb, text_layer
for v in VIDEOS:
    if v["id"] not in sys.argv[1:] or v["formato"] == "short":
        continue
    d = os.path.join(ROOT, v["carpeta"], "Miniatura")
    for f in os.listdir(d):
        if f.endswith(".png"):
            os.remove(os.path.join(d, f))
    for k, spec in enumerate(v["miniaturas"]):
        tag = "ABC"[k]; el = "_ELEGIDA" if k == v["mini_elegida"] else ""
        thumb(spec, 1280, 720, idx_seed=k).save(os.path.join(d, f"{v['id']}_miniatura_{tag}{el}_1280x720.png"))
        if spec["estilo"] in ("oficial", "gameplay"):
            text_layer(spec).save(os.path.join(d, f"{v['id']}_miniatura_{tag}_capa_texto_transparente.png"))
    print("miniaturas", v["id"])
