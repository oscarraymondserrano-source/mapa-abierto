"""V87-V89 · Serie 'LA COMUNIDAD': lo que pasa con GTA 6 entre streamers y jugadores, contado con material oficial
(sin imágenes de los streamers). Datos comprobados en varias fuentes (20/11/2026):
- Récord Twitch ~3,29 M (SullyGnome 3.293.515; Streams Charts 3.292.986; Dot Esports, Talkesport), durante el lanzamiento
  escalonado (Nueva Zelanda), antes de EE. UU. Multiplataforma: >6 M (Streams Charts 6,38 M; otras fuentes más).
- Extended Look en directo: IlloJuan 233.520 (récord personal), Rubius 191.056, IShowSpeed 177.887 (Streams Charts vía
  LevelUp, Profesional Review, Inven Global); total ~3,97 M; Netflix 31,1 M visualizaciones, n.º 1 de la semana (GamesRadar,
  GamingBolt, Insider Gaming).
- Rubius en Rockstar North: sesión de varias horas en la que el mando lo llevaba Rob Nelson (Notebookcheck, Shazoo,
  Allthings); seis estrellas y la policía recuerda tu aspecto (TechWiser; coherente con el Extended Look); dijo que no le
  pagaron por ir (3DJuegos, KCH).
DESCARTADO por no confirmarse: 311.000 espectadores de Rubius el día del lanzamiento, nido de huevos en la torre, Bigfoot."""
from content.common import S
from content.shorts3 import mk
from content.rk_pool import mezcla

PIE = "\n\nImágenes y vídeo: © Rockstar Games (material oficial de su web de descargas), con fines informativos. No se usan imágenes de los streamers mencionados. Mapa Abierto es un canal no oficial."


def M(clips, t, r, items=None, sfx=None):
    return dict(S("GRAFICO", t, rotulo=r, items=items or [], **({"sfx": sfx} if sfx else {})), clips=clips)


def G(t, r, items=None, sfx=None, **kw):
    return dict(S("GRAFICO", t, rotulo=r, items=items or [], **({"sfx": sfx} if sfx else {})), **kw)


def oficial(v, fuentes):
    v["seo"]["descripcion"] = v["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + "\n\nFuentes: " + fuentes + PIE
    v["oficial"] = True
    return v


V87 = oficial(mk("V87", "Record_Twitch", "LA COMUNIDAD", "GTA 6 rompe el récord de Twitch",
    ["GTA 6 ha roto el récord de Twitch", "3,29 millones viendo GTA 6 a la vez", "El récord que GTA 6 rompió antes de salir en EE. UU.", "GTA 6 y el mayor récord de Twitch", "Nadie había visto algo así en Twitch"],
    [M(mezcla("persecucion", "noche", n=3), "GTA 6 acaba de romper el récord de Twitch. Y lo hizo antes de salir en Estados Unidos.", "RÉCORD EN TWITCH", sfx="Golpe"),
     M(mezcla("conducir", "aire", n=3), "Según SullyGnome, la categoría de GTA 6 llegó a *3,29 millones* de espectadores a la vez.", "3,29 MILLONES"),
     G("Es el pico más alto de un juego en la historia de Twitch, según ese rastreador. Y llegó en pleno lanzamiento escalonado, cuando en Nueva Zelanda ya se podía jugar.", "RÉCORD HISTÓRICO", items=["Según SullyGnome", "Antes del estreno en EE. UU."]),
     M(mezcla("gente", "club", n=2), "Si sumas YouTube y Kick, los rastreadores hablan de más de *seis millones* de personas mirando a la vez.", "+6 MILLONES"),
     M(mezcla("atardecer", n=2), "¿Tú lo viste en directo o ya estabas jugando? Te leo.", "¿Y TÚ?", sfx="Sting")],
    dict(texto=["RÉCORD", "EN TWITCH"], sub="GTA 6", estilo="stamp", concepto="Récord."),
    "GTA 6 alcanzó unos 3,29 millones de espectadores simultáneos en Twitch según SullyGnome (Streams Charts da una cifra casi idéntica), el pico más alto de un juego en la plataforma según ese rastreador. Llegó durante el lanzamiento escalonado, antes del estreno en Estados Unidos. Sumando YouTube y Kick, los rastreadores hablan de más de 6 millones de espectadores simultáneos.",
    ["GTA 6 Twitch", "récord GTA 6", "GTA 6 espectadores"], "📌 ¿Lo viste en directo? 👇",
    objetivo="Serie 'La comunidad': noticia de streaming de la semana de lanzamiento."),
    "SullyGnome, Streams Charts, Dot Esports.")

V88 = oficial(mk("V88", "Illojuan_Rubius_Speed", "LA COMUNIDAD", "Quién tuvo más espectadores con el Extended Look de GTA 6",
    ["Illojuan, Rubius o IShowSpeed: ¿quién arrasó con GTA 6?", "El streamer que más gente juntó con GTA 6", "Illojuan rompió su récord con GTA 6", "¿Quién ganó el directo de GTA 6?", "Rubius vs Illojuan: el récord de GTA 6"],
    [M(mezcla("noche", "club", n=3), "¿Qué streamer juntó a más gente viendo el estreno del Extended Look de GTA 6? Atento al primer puesto.", "¿QUIÉN GANÓ?", sfx="Golpe"),
     G("¿Rubius, Illojuan o IShowSpeed? Piénsalo.", "¿QUIÉN GANÓ?", hold=3, quiz=dict(options=["A) Rubius", "B) Illojuan", "C) IShowSpeed"], correct=1)),
     G("¡Illojuan! Llegó a *233.520* espectadores a la vez, el récord de su canal, según Streams Charts.", "RESPUESTA: B", sfx="Acierto",
       quiz=dict(options=["A) Rubius", "B) Illojuan", "C) IShowSpeed"], correct=1, reveal=True)),
     G("Detrás, Rubius, con unos ciento noventa y un mil, e IShowSpeed, con casi ciento setenta y ocho mil.", "EL PODIO", items=["1. Illojuan · 233.520", "2. Rubius · 191.056", "3. IShowSpeed · 177.887"]),
     M(mezcla("atardecer", "agua", n=2), "En total, casi *cuatro millones* de personas lo siguieron en directos, y en Netflix sumó 31,1 millones de visualizaciones en su primera semana.", "4 MILLONES EN DIRECTO"),
     M(mezcla("conducir", n=2), "¿Con quién lo viste tú? Dímelo en comentarios.", "¿CON QUIÉN?", sfx="Sting")],
    dict(texto=["¿QUIÉN", "GANÓ?"], sub="GTA 6", estilo="quiz", concepto="Opciones A/B/C."),
    "Durante el estreno del Extended Look de GTA 6 (27/08/2026), Illojuan alcanzó un pico de 233.520 espectadores simultáneos, récord de su canal; Rubius, 191.056; IShowSpeed, 177.887 (datos de Streams Charts). El estreno reunió casi 4 millones de espectadores simultáneos en directos y 31,1 millones de visualizaciones en Netflix en su primera semana.",
    ["Illojuan GTA 6", "Rubius GTA 6", "IShowSpeed GTA 6"], "📌 ¿Con quién lo viste? 👇",
    objetivo="Captar búsquedas de 'illojuan gta 6' (~148.000/mes en ES) y 'rubius gta 6' (~120.000) sin usar sus imágenes."),
    "Streams Charts (vía LevelUp y Profesional Review), Netflix (vía GamesRadar).")

V89 = oficial(mk("V89", "Rubius_Rockstar_North", "LA COMUNIDAD", "Lo que vio Rubius de GTA 6 en Rockstar North",
    ["Rubius vio GTA 6 en Rockstar North: esto contó", "Lo que vio Rubius de GTA 6 antes que nadie", "Rubius en Rockstar: ¿jugó a GTA 6?", "Rubius y GTA 6: lo que no sabías", "La visita de Rubius a Rockstar North"],
    [M(mezcla("conducir", "persecucion", n=3), "Antes de que saliera GTA 6, Rubius estuvo en Rockstar North, en Escocia, viendo el juego por dentro.", "RUBIUS EN ROCKSTAR", sfx="Golpe"),
     G("Pero ojo: no jugó él. Según varios medios, el mando lo llevaba un responsable de desarrollo de Rockstar, en una sesión de varias horas.", "¿JUGÓ ÉL?", items=["No: jugaba Rockstar", "Sesión de varias horas"]),
     M(mezcla("persecucion", "noche", n=3), "Entre lo que contó: vuelven las *seis estrellas* de búsqueda y la policía recuerda tu aspecto.", "6 ESTRELLAS"),
     G("Y tras publicarlo, aclaró que no le pagaron por ir.", "«NO ME PAGARON»"),
     M(mezcla("atardecer", "aire", n=2), "¿Te habría gustado estar ahí? Comenta.", "¿TE APUNTAS?", sfx="Sting")],
    dict(texto=["RUBIUS", "EN ROCKSTAR"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "Antes del lanzamiento, Rubius visitó Rockstar North (Escocia) y vio una sesión de varias horas de GTA 6 en la que el mando lo llevaba un responsable de desarrollo de Rockstar. Entre los detalles que contó: vuelven las seis estrellas de búsqueda y la policía recuerda tu aspecto. Después aclaró que no le pagaron por la visita.",
    ["Rubius GTA 6", "Rubius Rockstar", "GTA 6 Rubius"], "📌 ¿Te habría gustado ir? 👇",
    objetivo="Búsqueda 'rubius gta 6' con datos verificados y sin imágenes del streamer."),
    "Notebookcheck, Shazoo, 3DJuegos.")

SHORTS = [V87, V88, V89]
SCHED = []
