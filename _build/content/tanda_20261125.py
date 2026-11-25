"""V92-V93 · Tanda del 25/11 (ESTRATEGIA.md: novedad verificada + idea 'GTA 6 Online').
V92 Primer parche de GTA 6 (01.002.002 en PS5, 23/11/2026): arreglos de cierres inesperados, clima que no cambiaba,
  autoguardado que fallaba, llamadas de la historia que no llegaban y nivel de búsqueda que no se iba
  (Push Square, Comicbook, Vice, GamingBible; notas en la web de soporte de Rockstar). El tamaño del parche viene de un
  dataminer: NO se usa.
V93 ¿Hay GTA 6 Online?: Rockstar no ha anunciado modo online ni fecha; el juego salió como experiencia para un jugador;
  lo de 2027 es una expectativa de prensa (Bloomberg), no una fecha oficial (Vice, HuffPost UK).
DESCARTADO: 'Rockstar cierra un port de PC en Discord' (las fuentes no coinciden: parece un proyecto de mapa y filtraciones)."""
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


V92 = oficial(mk("V92", "Primer_parche", "NOTICIAS", "Primer parche de GTA 6",
    ["GTA 6 ya tiene su primer parche: esto arregla", "El primer parche de GTA 6, explicado", "GTA 6 se actualiza: qué cambia", "Lo que arregla el primer parche de GTA 6", "GTA 6 recibe su primera actualización"],
    [M(mezcla("persecucion", "conducir", n=3), "GTA 6 ya tiene su primer parche. Esto es lo que arregla.", "PRIMER PARCHE", sfx="Golpe"),
     G("Salió el 23 de noviembre, cuatro días después del lanzamiento. En PS5 es la versión 01.002.002.", "23 DE NOVIEMBRE", items=["PS5 y Xbox Series", "Versión 01.002.002 (PS5)"]),
     G("Corrige cierres inesperados del juego y fallos del autoguardado.", "CIERRES Y GUARDADO", items=["Cierres inesperados", "Autoguardado"]),
     M(mezcla("atardecer", "gente", n=2), "También el clima que se quedaba atascado sin cambiar y llamadas de la historia que no llegaban al móvil.", "CLIMA Y LLAMADAS"),
     M(mezcla("persecucion", n=2), "Y un fallo que impedía quitarte el nivel de búsqueda de la policía.", "NIVEL DE BÚSQUEDA"),
     M(mezcla("noche", n=2), "¿Te ha pasado alguno de estos fallos? Cuéntamelo.", "¿TE HA PASADO?", sfx="Sting")],
    dict(texto=["PRIMER", "PARCHE"], sub="GTA 6", estilo="stamp", concepto="Noticia."),
    "El primer parche de GTA 6 (versión 01.002.002 en PS5) llegó el 23/11/2026 a PS5 y Xbox Series X|S. Según las notas publicadas por Rockstar, corrige cierres inesperados, fallos del autoguardado, el clima que dejaba de cambiar, llamadas de la historia que no llegaban y un fallo que impedía perder el nivel de búsqueda.",
    ["GTA 6 parche", "GTA 6 actualización", "GTA 6 update"], "📌 ¿Te ha pasado alguno de estos fallos? 👇",
    objetivo="Novedad verificada de la semana (serie NOTICIAS)."),
    "notas de Rockstar en su web de soporte, vía Push Square, Comicbook y Vice.")

V93 = oficial(mk("V93", "GTA6_Online", "PREGUNTA RÁPIDA", "¿Hay GTA 6 Online?",
    ["¿Hay GTA 6 Online? La respuesta", "¿Cuándo sale GTA 6 Online?", "GTA 6 Online: lo que hay de verdad", "¿GTA 6 tiene modo online?", "GTA 6 Online: ¿hay fecha?"],
    [M(mezcla("club", "noche", n=3), "¿Hay GTA 6 Online? De momento, no.", "¿GTA 6 ONLINE?", sfx="Golpe"),
     G("GTA 6 salió el 19 de noviembre con su modo historia, para un jugador.", "SOLO HISTORIA", items=["Modo historia", "Un jugador"]),
     G("Rockstar no ha anunciado modo online ni fecha. Ni cómo será ni si vendrá incluido con el juego.", "SIN ANUNCIO", items=["Sin fecha oficial", "Sin detalles"]),
     G("Lo de 2027 que leerás por ahí es lo que espera parte de la prensa, no una fecha de Rockstar.", "2027: NO OFICIAL", items=["Expectativa de prensa", "No confirmado"]),
     M(mezcla("aire", "atardecer", n=2), "Cuando Rockstar lo anuncie, lo verás aquí. ¿Lo esperas o te basta con la historia?", "¿LO ESPERAS?", sfx="Sting")],
    dict(texto=["¿GTA 6", "ONLINE?"], sub="LA VERDAD", estilo="stamp", concepto="Pregunta."),
    "GTA 6 salió el 19/11/2026 con su modo historia para un jugador. Rockstar no ha anunciado modo online ni fecha, ni si estará incluido con el juego. La fecha de 2027 que circula es una expectativa de prensa (Bloomberg), no un anuncio oficial.",
    ["GTA 6 Online", "GTA 6 online fecha", "GTA 6 multijugador"], "📌 ¿Esperas el online o te basta con la historia? 👇",
    objetivo="Búsqueda 'gta 6 online' (idea b de ESTRATEGIA.md)."),
    "Vice, HuffPost UK (sobre lo publicado por Bloomberg).")

SHORTS = [V92, V93]
SCHED = []
