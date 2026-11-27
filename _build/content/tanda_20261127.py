"""V95-V96 · Tanda del 27/11 (ESTRATEGIA.md sección b, ideas 5 y 13).
V95 ¿Hay trucos en GTA 6?: se desbloquean al terminar la historia principal, en una pestaña de trucos del menú de
  progreso; cada truco va ligado a un reto; usarlos desactiva el guardado (y logros) en esa sesión; las guías hablan de 61;
  Rockstar no ha publicado lista oficial (TweakTown, Shacknews, Red Bull, Player.one).
V96 ¿GTA 6 va a 60 fps?: 30 fps en todas las consolas, incluida PS5 Pro; sin modo de 60 ni de 40 fps; Rockstar lo atribuye
  a la CPU (Rockstar a Kotaku, vía Engadget, VGC, HotHardware, Beebom). PS5 Pro: PSSR y sombras con trazado de rayos
  (TweakTown, Insider Gaming)."""
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


V95 = oficial(mk("V95", "Trucos", "PREGUNTA RÁPIDA", "¿Hay trucos en GTA 6?",
    ["¿Hay trucos en GTA 6? Sí, pero hay truco", "Trucos de GTA 6: cómo se desbloquean", "GTA 6 tiene trucos, pero no como antes", "¿Cómo se activan los trucos en GTA 6?", "Los trucos de GTA 6, explicados"],
    [M(mezcla("persecucion", "conducir", n=3), "¿Hay trucos en GTA 6? Sí… pero no puedes usarlos desde el principio.", "¿TRUCOS?", sfx="Golpe"),
     G("Primero tienes que terminar la historia principal. Después aparece una sección de trucos en el menú de progreso.", "PRIMERO, LA HISTORIA", items=["Termina la historia", "Menú de progreso → Trucos"]),
     G("Y cada truco se gana superando un reto dentro del juego.", "CADA UNO, UN RETO"),
     M(mezcla("noche", "gente", n=2), "Ojo: según varias guías, si activas uno, en esa partida no puedes guardar.", "OJO AL GUARDAR"),
     G("Las guías hablan de 61 trucos, aunque Rockstar no ha publicado una lista oficial.", "61 SEGÚN LAS GUÍAS", items=["Sin lista oficial"]),
     M(mezcla("atardecer", n=2), "¿Prefieres los trucos de antes, con botones? Comenta.", "¿Y TÚ?", sfx="Sting")],
    dict(texto=["¿HAY", "TRUCOS?"], sub="GTA 6", estilo="stamp", concepto="Pregunta."),
    "GTA 6 tiene trucos, pero se desbloquean al terminar la historia principal: aparece una sección de trucos en el menú de progreso y cada truco se gana superando un reto. Según varias guías, al activar uno no se puede guardar en esa partida. Las guías hablan de 61 trucos; Rockstar no ha publicado una lista oficial.",
    ["GTA 6 trucos", "trucos GTA 6", "GTA 6 cheats"], "📌 ¿Trucos de antes o así? 👇",
    objetivo="Búsquedas 'gta 6 trucos' (15.111/mes en ES) y 'trucos gta 6' (14.986)."),
    "TweakTown, Shacknews, Red Bull.")

V96 = oficial(mk("V96", "60_fps", "PREGUNTA RÁPIDA", "¿GTA 6 va a 60 fps?",
    ["¿GTA 6 va a 60 fps? La respuesta", "GTA 6 a 60 fps: lo que ha dicho Rockstar", "¿Por qué GTA 6 va a 30 fps?", "GTA 6 en PS5 Pro: ¿60 fps?", "GTA 6 y los 60 fps: no"],
    [M(mezcla("persecucion", "conducir", n=3), "¿GTA 6 va a 60 fps? No, ni siquiera en PS5 Pro.", "¿60 FPS?", sfx="Golpe"),
     G("Va a 30 fps en todas las consolas: PS5, PS5 Pro y Xbox Series X y S.", "30 FPS", items=["PS5 y PS5 Pro", "Xbox Series X|S"]),
     G("Rockstar dice que no habrá modo de 60 fps, ni de 40. Según la compañía, el procesador no da para mover todo lo que pasa en Leonida.", "SIN MODO RENDIMIENTO", items=["Ni 60 ni 40 fps", "Culpa del procesador"]),
     M(mezcla("aire", "atardecer", n=2), "Lo que sí tiene la PS5 Pro son mejoras gráficas, como el reescalado PSSR y sombras con trazado de rayos.", "EXTRAS EN PS5 PRO", items=["PSSR", "Sombras con trazado de rayos"]),
     M(mezcla("noche", n=2), "¿Te importan los fps o te vale con 30? Te leo.", "¿TE IMPORTA?", sfx="Sting")],
    dict(texto=["¿60", "FPS?"], sub="GTA 6", estilo="stamp", concepto="Pregunta."),
    "GTA 6 va a 30 fps en PS5, PS5 Pro y Xbox Series X|S. Rockstar ha dicho que no habrá modo de 60 ni de 40 fps en ninguna consola, incluida PS5 Pro, porque el procesador no puede mover la simulación a más fps. En PS5 Pro hay mejoras gráficas como el reescalado PSSR y sombras con trazado de rayos.",
    ["GTA 6 60 fps", "GTA 6 fps", "GTA 6 PS5 Pro"], "📌 ¿Te importan los fps? 👇",
    objetivo="Búsqueda 'como jugar gta 6 a 60 fps' (8.543 global)."),
    "Rockstar a Kotaku, vía Engadget y VGC; TweakTown, Insider Gaming.")

SHORTS = [V95, V96]
SCHED = []
