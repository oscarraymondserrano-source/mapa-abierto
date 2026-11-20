"""Miniaturas 1280x720 para vídeos largos: fotograma oficial + capa de texto de marca."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gfx import *
from build_videos import text_layer, RK_DIR, official_photo

def make(rel, spec, out, fx=0.5, zoom=1.0):
    img = official_photo(rel, int(1280 * zoom), int(720 * zoom), fx)
    if zoom != 1.0:
        img = img.crop(((img.width - 1280) // 2, (img.height - 720) // 2, (img.width - 1280) // 2 + 1280, (img.height - 720) // 2 + 720))
    img.alpha_composite(text_layer(spec))
    m = pin_mark(90); img.alpha_composite(m, (1280 - m.width - 20, 720 - m.height - 16))
    img.convert("RGB").save(out, quality=92)

if __name__ == "__main__":
    from content.tanda_20261121_largo import V86
    d = os.path.join(os.path.dirname(__file__), "..", V86["carpeta"], "Miniatura"); os.makedirs(d, exist_ok=True)
    srcs = [("x_EL_stills/tiroteo.jpg", 0.75), ("x_EL_stills/thumb_estrellas.jpg", 0.5), ("x_EL_stills/paracaidas.jpg", 0.6)]
    for k, ((rel, fx), spec) in enumerate(zip(srcs, V86["miniaturas"])):
        make(rel, spec, os.path.join(d, f"V86_miniatura_{'ABC'[k]}{'_ELEGIDA' if k == 0 else ''}_1280x720.jpg"), fx)
    print("ok")
