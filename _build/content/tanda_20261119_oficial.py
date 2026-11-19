"""Short de demostración con material oficial de Rockstar (capturas y tráiler de lanzamiento de su web de descargas)."""
from content.common import S
from content.shorts3 import mk

TANDA = "Tanda 2026-11-19 oficial"
T = "GTAVI_Launch_Trailer.mp4"

def F(rel, texto, rotulo, fx=0.5, items=None):
    return dict(S("GRAFICO", texto, rotulo=rotulo, items=items or []), foto=rel, fx=fx)

def C(start, texto, rotulo, items=None):
    return dict(S("GRAFICO", texto, rotulo=rotulo, items=items or []), clip=(T, start))

V59 = mk("V59", "Leonida_Imagenes_Oficiales", "LA SAGA EN 30 s", "Las 6 zonas de GTA 6 con imágenes oficiales",
    ["Así es Leonida: las 6 zonas de GTA 6 en imágenes oficiales", "GTA 6: las 6 zonas del mapa, una a una", "Recorre Leonida en 40 segundos", "Vice City, los Cayos y más: GTA 6 por dentro", "Las zonas de GTA 6 que vas a explorar"],
    [C(54, "Así es Leonida, con imágenes oficiales de Rockstar. Seis zonas en cuarenta segundos.", "ASÍ ES LEONIDA"),
     F("Places/Vice City/Vice_City_01.jpg", "Vice City: la gran ciudad, inspirada en Miami.", "VICE CITY", 0.45),
     F("Places/Leonida Keys/Leonida_Keys_01.jpg", "Los Cayos de Leonida: islas, puentes y agua turquesa.", "CAYOS DE LEONIDA", 0.55),
     F("Places/Grassrivers/Grassrivers_04.jpg", "Grassrivers: los pantanos, con hidrodeslizadores y caimanes.", "GRASSRIVERS", 0.5),
     F("Places/Port Gellhorn/Port_Gellhorn_01.jpg", "Port Gellhorn: moteles de carretera y neón en la costa.", "PORT GELLHORN", 0.35),
     F("Places/Ambrosia/Ambrosia_01.jpg", "Ambrosia: el interior rural, territorio de moteros.", "AMBROSIA", 0.5),
     F("Places/Mount Kalaga National Park/Mount_Kalaga_National_Park_04.jpg", "Y Mount Kalaga: el parque nacional, con cañones y bosques.", "MOUNT KALAGA", 0.6),
     C(39, "¿Cuál vas a explorar primero? Dímelo en comentarios.", "¿CUÁL PRIMERO?")],
    dict(texto=["ASÍ ES", "LEONIDA"], sub="GTA 6", estilo="mapa", concepto="Esquema."),
    "Las 6 zonas de Leonida en GTA 6 con imágenes oficiales de Rockstar Games: Vice City, los Cayos de Leonida, Grassrivers, Port Gellhorn, Ambrosia y Mount Kalaga.",
    ["mapa gta 6", "GTA 6 zonas", "Leonida", "Vice City"], "📌 ¿Cuál vas a explorar primero? 🗺️",
    objetivo="Probar el formato con material oficial (capturas + tráiler) frente a los gráficos propios.")

V59["seo"]["descripcion"] = V59["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + "\n\nImágenes y vídeo: © Rockstar Games (material oficial de su web de descargas), con fines informativos. Mapa Abierto es un canal no oficial."
V59["oficial"] = True
SHORTS = [V59]
SCHED = [("V59", "2026-11-20", "17:00", "2026-11-20", "17:40")]
