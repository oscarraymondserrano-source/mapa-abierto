"""V84-V85: material nuevo de la web de descargas de Rockstar (19/11): Vintage Vice City Pack y Ultimate Edition.
Datos: GamesRadar, Vice y la wiki de GTA (ver respuesta del 19/11). Montaje con cortes rápidos (content.rk_pool)."""
from content.common import S
from content.shorts3 import mk
from content.rk_pool import mezcla

TANDA = "Tanda 2026-11-19 novedades oficiales"
VP = "x_GTAVI_Vintage_Vice_City_Pack/"
UE = "x_GTAVI_Ultimate_Edition_Benefits/"
PIE = "\n\nImágenes y vídeo: © Rockstar Games (material oficial de su web de descargas), con fines informativos. Mapa Abierto es un canal no oficial."

def _s(t, r, items, sfx):
    return S("GRAFICO", t, rotulo=r, items=items or [], **({"sfx": sfx} if sfx else {}))
def F(rel, t, r, fx=0.5, items=None, sfx=None):
    return dict(_s(t, r, items, sfx), foto=rel, fx=fx)
def M(clips, t, r, items=None, sfx=None):
    return dict(_s(t, r, items, sfx), clips=clips)
def oficial(v):
    v["seo"]["descripcion"] = v["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + PIE
    v["oficial"] = True
    return v

V84 = oficial(mk("V84", "Vintage_Vice_City_Pack", "NOTICIA", "El pack gratis de GTA 6 que acaba el 20 de noviembre",
    ["Este pack de GTA 6 solo lo tienes si lo compras antes del 20/11", "Vintage Vice City Pack: qué incluye", "El regalo de GTA 6 que acaba mañana", "GTA 6: el coche y la ropa extra de la reserva", "No te quedes sin el Vintage Vice City Pack"],
    [M(mezcla("noche", "club", n=3), "Si te haces con GTA 6 antes del 20 de noviembre, te llevas un pack extra. Y eso es ya.", "HASTA EL 20/11", sfx="Golpe"),
     F(VP + "VINTAGE_VICE_CITY_PACK_VAPID_STANIER_01.jpg", "Se llama Vintage Vice City Pack. Trae un Vapid Stanier del cincuenta y cinco, con su garaje en Shore Court.", "VAPID STANIER '55", 0.5),
     F(VP + "VINTAGE_VICE_CITY_PACK_EXCLUSIVE_LOOKS_01.jpg", "Ropa de estilo Vice City para Jason y para Lucia.", "ROPA VICE CITY", 0.5),
     F(VP + "VINTAGE_VICE_CITY_WEAPON_PATTERN_01.jpg", "Y un acabado tropical para las armas.", "ACABADO TROPICAL", 0.5),
     F(VP + "VINTAGE_VICE_CITY_PACK_02.jpg", "Vale para la edición estándar y para la Ultimate, en compras digitales y reservas en tienda hechas antes del 20.", "ESTÁNDAR Y ULTIMATE", 0.5, items=["Digital o reserva", "Antes del 20/11"]),
     M(mezcla("conducir", "noche", n=2), "Pásaselo a quien aún no lo tenga.", "PÁSASELO", sfx="Sting")],
    dict(texto=["PACK", "EXTRA"], sub="HASTA EL 20/11", estilo="reloj", concepto="Reloj."),
    "Vintage Vice City Pack de GTA 6: Vapid Stanier del 55 con garaje en Shore Court, ropa de estilo Vice City para Jason y Lucia y un acabado tropical para armas. Para la edición estándar y la Ultimate, en compras digitales y reservas en tienda hechas antes del 20/11/2026.",
    ["Vintage Vice City Pack", "GTA 6 reserva", "GTA 6 bonus"], "📌 ¿Ya lo tienes? 👇",
    objetivo="Noticia con fecha límite (20/11) e imágenes oficiales nuevas."))

V85 = oficial(mk("V85", "Que_incluye_Ultimate", "GUÍA RÁPIDA", "Qué incluye la Ultimate Edition de GTA 6",
    ["¿Qué incluye la Ultimate Edition de GTA 6?", "GTA 6 Ultimate Edition: todo lo que trae", "¿Merece la pena la Ultimate de GTA 6?", "Ultimate Edition de GTA 6 en 40 segundos", "Los extras de GTA 6 Ultimate Edition"],
    [M(mezcla("conducir", "agua", n=3), "¿Qué trae la Ultimate Edition de GTA 6? Te lo enseño con las imágenes oficiales de Rockstar.", "ULTIMATE EDITION", sfx="Golpe"),
     F(UE + "ULTIMATE_EDITION_GROTTI_CHEETAH_01.jpg", "Un Grotti Cheetah del noventa y cinco, con su propio garaje.", "GROTTI CHEETAH '95", 0.5),
     F(UE + "ULTIMATE_EDITION_SQUALO_01.jpg", "La lancha Shitzu Squalo.", "SHITZU SQUALO", 0.5),
     F(UE + "ULTIMATE_EDITION_WYMAN_CAR_COLLECTION_01.jpg", "Encargos del coleccionista Wyman para restaurar coches clásicos, con cuatro exclusivos de esta edición.", "COCHES CLÁSICOS", 0.5),
     F(UE + "ULTIMATE_EDITION_ELECTRIC_FANG_01.jpg", "El estudio de tatuajes Electric Fang, en Vice City, con diseños de FAILE.", "ELECTRIC FANG", 0.5),
     F(UE + "ULTIMATE_EDITION_ONE_EYED_WILLIE_01.jpg", "Y el taller One-Eyed Willie's, para preparar todoterrenos.", "ONE-EYED WILLIE'S", 0.5),
     F(UE + "ULTIMATE_EDITION_HAWK_AND_LITTLE_MORGAN_REVOLVERS_02.jpg", "Además de revólveres, ropa y más extras. ¿Merece la pena? Comenta.", "¿MERECE LA PENA?", 0.5, sfx="Sting")],
    dict(texto=["ULTIMATE", "EDITION"], sub="GTA 6", estilo="checklist", concepto="Checklist."),
    "Qué incluye la Ultimate Edition de GTA 6: Grotti Cheetah del 95 con garaje, lancha Shitzu Squalo, encargos del coleccionista Wyman con cuatro clásicos exclusivos, el estudio de tatuajes Electric Fang (diseños de FAILE), el taller One-Eyed Willie's, revólveres, ropa y más extras.",
    ["GTA 6 Ultimate Edition", "Ultimate Edition GTA 6", "GTA 6 ediciones"], "📌 ¿Estándar o Ultimate? 👇",
    objetivo="Búsqueda de la semana de lanzamiento ('gta 6 ultimate edition') con imágenes oficiales nuevas."))

SHORTS = [V84, V85]
SCHED = [("V84", "2026-11-19", "20:30", "2026-11-19", "21:00"), ("V85", "2026-11-20", "19:30", "2026-11-20", "18:30")]
