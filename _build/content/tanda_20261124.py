"""V90-V91 · Preguntas directas con búsqueda (ESTRATEGIA.md sección b, ideas 4 y 1).
V90 ¿GTA 6 está en español?: textos y subtítulos en español de España y de México, voces solo en inglés
  (Take-Two en reunión con inversores vía C5N; Vandal; ficha de la tienda de Xbox). Rótulos en español vistos en el
  Extended Look (fotograma 706 s, comprobado el 20/11).
V91 ¿GTA 6 en PC?: Rockstar no ha anunciado versión ni fecha para PC; prioriza consolas (PC Gamer, Sportskeeda,
  Beebom). Las fechas de 2027 son rumores sin confirmar."""
from content.common import S
from content.shorts3 import mk
from content.rk_pool import mezcla

PIE = "\n\nImágenes y vídeo: © Rockstar Games (material oficial de su web de descargas, incluido el Extended Look), con fines informativos. La voz está generada con IA. Mapa Abierto es un canal no oficial."


def M(clips, t, r, items=None, sfx=None):
    return dict(S("GRAFICO", t, rotulo=r, items=items or [], **({"sfx": sfx} if sfx else {})), clips=clips)


def G(t, r, items=None, sfx=None, **kw):
    return dict(S("GRAFICO", t, rotulo=r, items=items or [], **({"sfx": sfx} if sfx else {})), **kw)


def oficial(v, fuentes):
    v["seo"]["descripcion"] = v["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + "\n\nFuentes: " + fuentes + PIE
    v["oficial"] = True
    return v


V90 = oficial(mk("V90", "GTA6_en_espanol", "PREGUNTA RÁPIDA", "¿GTA 6 está en español?",
    ["¿GTA 6 está en español? La respuesta", "GTA 6 en español: ¿tiene doblaje?", "¿GTA 6 tiene voces en español?", "GTA 6 en español: lo que hay y lo que no", "¿Se puede jugar GTA 6 en español?"],
    [M(mezcla("conducir", "gente", n=3), "¿GTA 6 está en español? Sí… pero no del todo.", "¿EN ESPAÑOL?", sfx="Golpe"),
     G("Los textos y los subtítulos están en español, tanto de España como de México. Lo confirmó Take-Two, la dueña de Rockstar.", "TEXTOS: SÍ", items=["Español de España", "Español de México"]),
     G("Pero las voces solo están en inglés. No hay doblaje, igual que en GTA 5 o en Red Dead Redemption 2.", "VOCES: NO", items=["Voces solo en inglés", "Sin doblaje"]),
     M([("EL", 706, 1.6, 0.4), ("EL", 708, 1.6, 0.5)], "Y un detalle: dentro del juego hay carteles en español, como este de cerveza fría en una tienda de Leonida.", "RÓTULOS EN ESPAÑOL"),
     M(mezcla("atardecer", n=2), "¿Lo prefieres en inglés o te habría gustado doblado? Comenta.", "¿Y TÚ?", sfx="Sting")],
    dict(texto=["¿EN", "ESPAÑOL?"], sub="GTA 6", estilo="stamp", concepto="Pregunta."),
    "GTA 6 tiene textos y subtítulos en español de España y de México, pero las voces están solo en inglés: no hay doblaje, como en GTA 5 o Red Dead Redemption 2. Dentro del juego también hay rótulos en español, como los carteles de una tienda que se ven en el Extended Look.",
    ["GTA 6 español", "GTA 6 doblaje", "GTA 6 idiomas"], "📌 ¿Inglés con subtítulos o te habría gustado doblado? 👇",
    objetivo="Búsqueda 'gta 6 español' (44.397/mes en ES según vidIQ)."),
    "Take-Two vía C5N, Vandal, ficha de la tienda de Xbox.")

V91 = oficial(mk("V91", "GTA6_en_PC", "PREGUNTA RÁPIDA", "¿Se puede jugar GTA 6 en PC?",
    ["¿Se puede jugar GTA 6 en PC?", "GTA 6 en PC: lo que hay de verdad", "¿Cuándo sale GTA 6 para PC?", "GTA 6 en PC: ¿hay fecha?", "¿GTA 6 llega a PC?"],
    [M(mezcla("persecucion", "noche", n=3), "¿Se puede jugar GTA 6 en PC? Hoy, no.", "¿GTA 6 EN PC?", sfx="Golpe"),
     G("GTA 6 salió el 19 de noviembre solo en PlayStation 5 y Xbox Series X y S.", "SOLO CONSOLAS", items=["PS5", "Xbox Series X|S"]),
     G("Rockstar no ha anunciado versión de PC ni fecha. Ha dicho que da prioridad a las consolas, donde está la mayoría de sus jugadores.", "SIN FECHA EN PC", items=["Sin anuncio oficial", "Prioridad: consolas"]),
     G("Las fechas de 2027 que circulan son rumores. Y ojo: cualquier web que te ofrezca GTA 6 para PC ahora mismo es una estafa.", "OJO CON LAS ESTAFAS", items=["2027: solo rumores", "GTA 6 para PC hoy = estafa"]),
     M(mezcla("aire", "atardecer", n=2), "Cuando Rockstar lo anuncie, lo verás aquí. ¿Esperas al PC o te pasas a consola?", "¿ESPERAS?", sfx="Sting")],
    dict(texto=["¿GTA 6", "EN PC?"], sub="LA VERDAD", estilo="stamp", concepto="Pregunta."),
    "GTA 6 salió el 19/11/2026 solo en PlayStation 5 y Xbox Series X|S. Rockstar no ha anunciado versión de PC ni fecha y ha dicho que prioriza las consolas. Las fechas de 2027 que circulan son rumores sin confirmar, y cualquier web que ofrezca GTA 6 para PC hoy es una estafa.",
    ["GTA 6 PC", "GTA 6 en PC", "cuando sale GTA 6 en PC"], "📌 ¿Esperas a la versión de PC o te pasas a consola? 👇",
    objetivo="Búsquedas 'gta 6 pc' (44.740/mes en ES) y 'como jugar gta 6 en pc' (68.581 global)."),
    "PC Gamer, Sportskeeda, Beebom.")

SHORTS = [V90, V91]
SCHED = []
