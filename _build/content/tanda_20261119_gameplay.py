"""Tanda V66-V75: juego real del Extended Look y material oficial de Rockstar (web de descargas de prensa).
Fuentes de datos: V48/V49/V53 (Extended Look), entrevista de The Guardian (v01) y descripciones de las zonas de Leonida (Rockstar vía Game Informer)."""
from content.common import S
from content.shorts3 import mk, quiz

TANDA = "Tanda 2026-11-19 juego real"
TR = "GTAVI_Launch_Trailer.mp4"
P = "People/"; L = "Places/"
PIE = "\n\nImágenes y vídeo: © Rockstar Games (material oficial de su web de descargas, incluido el Extended Look), con fines informativos. Mapa Abierto es un canal no oficial."

def _s(texto, rotulo, items, sfx):
    return S("GRAFICO", texto, rotulo=rotulo, items=items or [], **({"sfx": sfx} if sfx else {}))
def F(rel, texto, rotulo, fx=0.5, items=None, sfx=None):
    return dict(_s(texto, rotulo, items, sfx), foto=rel, fx=fx)
def E(start, texto, rotulo, vel=1.0, fx=0.5, items=None, sfx=None):
    return dict(_s(texto, rotulo, items, sfx), clip=("EL", start, vel), fx=fx)
def C(start, texto, rotulo, vel=1.0, fx=0.5, items=None, sfx=None):
    return dict(_s(texto, rotulo, items, sfx), clip=(TR, start, vel), fx=fx)
def oficial(v):
    v["seo"]["descripcion"] = v["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + PIE
    v["oficial"] = True
    return v
JR = "JUEGO REAL"

V66 = oficial(mk("V66", "Asi_se_conduce", JR, "Así se conduce en GTA 6 (juego real)",
    ["Así se conduce en GTA 6: juego real", "GTA 6 al volante: imágenes reales del juego", "Conducir por Vice City en GTA 6", "Esto es GTA 6 de verdad (no es un tráiler)", "GTA 6 gameplay: conducción"],
    [E(506, "Esto no es un tráiler: es juego real de GTA 6, del Extended Look que Rockstar grabó en una PlayStation 5.", "JUEGO REAL", fx=0.4, sfx="Golpe"),
     E(514, "Un descapotable cruzando Vice City a plena luz del día.", "VICE CITY", fx=0.4),
     E(522, "Tráfico, palmeras y rascacielos al fondo.", "EL TRÁFICO", fx=0.5),
     E(760, "La carretera, al atardecer.", "ATARDECER", fx=0.5),
     E(925, "Y persecuciones entre callejones. ¿Qué coche vas a coger primero? Comenta.", "¿TU COCHE?", fx=0.45, sfx="Sting")],
    dict(texto=["JUEGO", "REAL"], sub="GTA 6", estilo="paisaje", concepto="Paisaje."),
    "Así se conduce en GTA 6, con juego real del Extended Look que Rockstar grabó en una PS5: descapotable por Vice City, tráfico, atardecer y persecuciones.",
    ["GTA 6 gameplay", "GTA 6 conducción", "GTA 6 extended look"], "📌 ¿Qué coche vas a coger primero? 🚗",
    objetivo="Probar planos de juego real (Extended Look) frente a capturas."))

V67 = oficial(mk("V67", "Policia_Juego_Real", JR, "Así funciona la policía en GTA 6",
    ["Así funciona la policía en GTA 6", "La policía de GTA 6 se fija en tu ropa", "6 estrellas en GTA 6: imágenes reales", "Cómo escapar de la policía en GTA 6", "GTA 6: la policía, en juego real"],
    [E(849, "La policía de GTA 6, en juego real del Extended Look. Esto es lo que enseñó Rockstar.", "LA POLICÍA", vel=1.2, fx=0.35, sfx="Golpe"),
     E(925, "Vuelven las seis estrellas de búsqueda, el máximo clásico de la saga. GTA 5 se quedaba en cinco.", "6 ESTRELLAS", fx=0.45, items=["GTA V: 5", "GTA VI: 6"]),
     F(P+"Lucia Caminos/Lucia_Caminos_14.jpg", "Y la policía se fija en tu coche, en tu ropa y en tu descripción.", "TE RECONOCEN", 0.4, items=["Coche", "Ropa", "Descripción"]),
     F(P+"Jason Duval/Jason_Duval_07.jpg", "Así que cambiar de ropa o de coche puede salvarte. ¿Cuántas estrellas aguantarás? Comenta.", "¿CUÁNTAS AGUANTAS?", 0.5, sfx="Sting")],
    dict(texto=["6", "ESTRELLAS"], sub="GTA 6", estilo="stamp", concepto="Sello."),
    "Según lo mostrado en el Extended Look (agosto de 2026), GTA 6 recupera las 6 estrellas de búsqueda (GTA V tenía 5) y la policía rastrea tu vehículo, tu ropa y tu descripción.",
    ["GTA 6 policía", "GTA 6 estrellas", "GTA 6 gameplay"], "📌 ¿Cuántas estrellas aguantarás? ⭐"))

V68 = oficial(mk("V68", "Que_hacer_juego_real", JR, "Qué puedes hacer en GTA 6 (juego real)",
    ["Qué puedes hacer en GTA 6: juego real", "GTA 6 no es solo misiones: mira esto", "Hidrodeslizador, moto de agua y paracaídas en GTA 6", "Las actividades de GTA 6 en imágenes reales", "GTA 6 más allá de la historia"],
    [E(1030, "Qué se puede hacer en GTA 6 además de la historia, con juego real del Extended Look.", "MÁS ALLÁ DE LA HISTORIA", vel=2.5, fx=0.5, sfx="Golpe"),
     E(1045, "Moto de agua frente a Vice City.", "MOTO DE AGUA", vel=2.5, fx=0.45),
     E(1133, "Paracaídas sobre la ciudad.", "PARACAÍDAS", vel=1.0, fx=0.5),
     E(1222, "Y carreras de noche. Rockstar enseñó también motos de tierra, buceo y salto base.", "CARRERAS", vel=1.4, fx=0.5, items=["Motos de tierra", "Buceo", "Salto base"]),
     F(L+"Vice City/Vice_City_15.jpg", "¿Cuál vas a probar primero? Comenta.", "¿CUÁL PRIMERO?", 0.5, sfx="Sting")],
    dict(texto=["MÁS QUE", "MISIONES"], sub="JUEGO REAL", estilo="paisaje", concepto="Paisaje."),
    "Actividades de GTA 6 con juego real del Extended Look (agosto de 2026): hidrodeslizador, moto de agua, paracaídas y carreras nocturnas; Rockstar también mostró motos de tierra, buceo y salto base.",
    ["GTA 6 actividades", "GTA 6 gameplay", "qué hacer en GTA 6"], "📌 ¿Cuál vas a probar primero? 🏍️🪂"))

V69 = oficial(mk("V69", "Empiezan_desde_abajo", JR, "Jason y Lucia empiezan desde abajo",
    ["Jason y Lucia empiezan desde abajo en GTA 6", "Así empieza la historia de GTA 6", "GTA 6: nada de golpes millonarios al principio", "Los primeros trabajos de Jason y Lucia", "GTA 6 empieza con robos pequeños"],
    [E(1003, "En GTA 6, Jason y Lucia no empiezan con golpes millonarios.", "DESDE ABAJO", fx=0.45, sfx="Golpe"),
     F(P+"Jason and Lucia/Jason_and_Lucia_06.jpg", "Según contó Rockstar a The Guardian, sus primeros trabajos son cosas como hacer el puente a coches baratos.", "COCHES BARATOS", 0.5),
     F(P+"Jason and Lucia/Jason_and_Lucia_12.jpg", "O forzar cerraduras sencillas.", "CERRADURAS", 0.5),
     F(P+"Jason and Lucia/Jason_and_Lucia_08.jpg", "Y a partir de ahí, a subir. ¿Te gusta empezar desde cero? Comenta.", "¿DESDE CERO?", 0.5, sfx="Sting")],
    dict(texto=["DESDE", "ABAJO"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "Según Rockstar en una entrevista con The Guardian, Jason y Lucia empiezan desde abajo en GTA 6: sus primeros trabajos son hacer el puente a coches baratos o forzar cerraduras sencillas.",
    ["GTA 6 historia", "Jason y Lucia", "GTA 6 misiones"], "📌 ¿Te gusta empezar desde cero? 👇"))

V70 = oficial(mk("V70", "Cayos_de_Leonida", "ZONAS", "Así son los Cayos de Leonida en GTA 6",
    ["Así son los Cayos de Leonida en GTA 6", "Leonida Keys: la zona de las islas", "GTA 6: los Cayos, en imágenes oficiales", "La zona de Jason en GTA 6", "Islas y puentes en GTA 6"],
    [F(L+"Leonida Keys/Leonida_Keys_06.jpg", "Los Cayos de Leonida, en imágenes oficiales de Rockstar.", "CAYOS DE LEONIDA", 0.5, sfx="Golpe"),
     F(L+"Leonida Keys/Leonida_Keys_02.jpg", "Están inspirados en los Cayos de Florida.", "COMO FLORIDA", 0.5),
     F(L+"Leonida Keys/Leonida_Keys_03.jpg", "Islas tropicales unidas por carreteras y largos puentes sobre el mar.", "ISLAS Y PUENTES", 0.5),
     F(P+"Jason Duval/Jason_Duval_03.jpg", "Es la zona de Jason: allí trabaja para traficantes locales, según su ficha oficial.", "LA ZONA DE JASON", 0.5),
     F(L+"Leonida Keys/Leonida_Keys_05.jpg", "¿Te harías una casa aquí? Comenta.", "¿VIVIRÍAS AQUÍ?", 0.5, sfx="Sting")],
    dict(texto=["LOS", "CAYOS"], sub="GTA 6", estilo="mapa", concepto="Mapa."),
    "Los Cayos de Leonida en GTA 6, con imágenes oficiales de Rockstar: inspirados en los Cayos de Florida, islas tropicales unidas por carreteras y puentes sobre el mar. Según su ficha oficial, Jason trabaja allí para traficantes locales.",
    ["Leonida Keys", "Cayos de Leonida", "mapa GTA 6"], "📌 ¿Vivirías en los Cayos? 🏝️"))

V71 = oficial(mk("V71", "Grassrivers", "ZONAS", "Así es Grassrivers, los pantanos de GTA 6",
    ["Así es Grassrivers, los pantanos de GTA 6", "Grassrivers: caimanes e hidrodeslizadores", "GTA 6: la zona de los pantanos", "Los Everglades de GTA 6", "Grassrivers en imágenes reales"],
    [E(1030, "Esto es Grassrivers, los pantanos de GTA 6, en juego real del Extended Look.", "GRASSRIVERS", vel=2.5, fx=0.5, sfx="Golpe"),
     F(L+"Grassrivers/Grassrivers_03.jpg", "Es la versión de Leonida de los Everglades de Florida.", "LOS EVERGLADES", 0.5),
     F(L+"Grassrivers/Grassrivers_05.jpg", "Pantanos con rutas en hidrodeslizador.", "EN BARCA", 0.5),
     F(L+"Grassrivers/Grassrivers_01.jpg", "Y encuentros con caimanes. ¿Te atreves a entrar? Comenta.", "¿TE ATREVES?", 0.5, sfx="Sting")],
    dict(texto=["LOS", "PANTANOS"], sub="GTA 6", estilo="paisaje", concepto="Paisaje."),
    "Grassrivers, la zona de pantanos de GTA 6, inspirada en los Everglades de Florida: rutas en hidrodeslizador y caimanes. Con juego real del Extended Look e imágenes oficiales de Rockstar.",
    ["Grassrivers", "GTA 6 pantanos", "mapa GTA 6"], "📌 ¿Te atreves con los caimanes? 🐊"))

V72 = oficial(mk("V72", "Port_Gellhorn", "ZONAS", "Así es Port Gellhorn en GTA 6",
    ["Así es Port Gellhorn en GTA 6", "Port Gellhorn: la costa decadente de GTA 6", "La zona más peligrosa de GTA 6", "GTA 6: Port Gellhorn en imágenes oficiales", "Port Gellhorn, explicado"],
    [F(L+"Port Gellhorn/Port_Gellhorn_02.jpg", "Port Gellhorn, en imágenes oficiales de Rockstar.", "PORT GELLHORN", 0.5, sfx="Golpe"),
     F(L+"Port Gellhorn/Port_Gellhorn_03.jpg", "Un pueblo costero de vacaciones venido a menos.", "COSTA DECADENTE", 0.5),
     F(L+"Port Gellhorn/Port_Gellhorn_05.jpg", "Con tiendas abandonadas y mucho crimen por debajo.", "TIENDAS VACÍAS", 0.5),
     F(L+"Port Gellhorn/Port_Gellhorn_06.jpg", "Un crimen más de barrio obrero que el crimen organizado de Vice City.", "OTRO CRIMEN", 0.5),
     F(L+"Port Gellhorn/Port_Gellhorn_04.jpg", "¿Irías de vacaciones aquí? Comenta.", "¿DE VACACIONES?", 0.5, sfx="Sting")],
    dict(texto=["PORT", "GELLHORN"], sub="GTA 6", estilo="mapa", concepto="Mapa."),
    "Port Gellhorn en GTA 6, con imágenes oficiales de Rockstar: un pueblo costero de vacaciones venido a menos, con tiendas abandonadas y un crimen más obrero que el de Vice City.",
    ["Port Gellhorn", "zonas GTA 6", "mapa GTA 6"], "📌 ¿Irías de vacaciones a Port Gellhorn? 🏚️"))

V73 = oficial(mk("V73", "Ambrosia_y_Kalaga", "ZONAS", "Ambrosia y Mount Kalaga: el interior de GTA 6",
    ["Ambrosia y Mount Kalaga: el interior de GTA 6", "GTA 6 no es solo playa: mira esto", "La refinería, los moteros y el bosque de GTA 6", "GTA 6: las zonas del norte", "Caza y pesca en GTA 6"],
    [F(L+"Ambrosia/Ambrosia_02.jpg", "GTA 6 no es solo playa. Esto es el interior de Leonida, en imágenes oficiales.", "EL INTERIOR", 0.5, sfx="Golpe"),
     F(L+"Ambrosia/Ambrosia_03.jpg", "Ambrosia es la zona industrial: la refinería de azúcar Allied Crystal da los empleos.", "AMBROSIA", 0.5, items=["Refinería de azúcar"]),
     F(L+"Ambrosia/Ambrosia_01.jpg", "Y una banda de moteros controla casi todo lo demás.", "LOS MOTEROS", 0.5),
     F(L+"Mount Kalaga National Park/Mount_Kalaga_National_Park_01.jpg", "Más al norte, Mount Kalaga: un parque nacional de bosques donde Rockstar confirma caza y pesca.", "MOUNT KALAGA", 0.5, items=["Caza", "Pesca"]),
     F(L+"Mount Kalaga National Park/Mount_Kalaga_National_Park_03.jpg", "¿Ciudad o naturaleza? Comenta.", "¿CIUDAD O BOSQUE?", 0.5, sfx="Sting")],
    dict(texto=["EL", "INTERIOR"], sub="GTA 6", estilo="paisaje", concepto="Paisaje."),
    "Ambrosia y Mount Kalaga en GTA 6, con imágenes oficiales de Rockstar: Ambrosia es la zona industrial (refinería de azúcar Allied Crystal y una banda de moteros); Mount Kalaga es un parque nacional al norte con caza y pesca confirmadas por Rockstar.",
    ["Ambrosia GTA 6", "Mount Kalaga", "mapa GTA 6"], "📌 ¿Ciudad o naturaleza? 🌲🏙️"))

V74 = quiz("V74", "Quiz_Estrellas", 10, "Pregunta con juego real. Tres segundos.",
    "¿CUÁNTAS ESTRELLAS TIENE GTA 6?", "¿Cuántas estrellas de búsqueda tiene GTA 6? A, cinco. B, seis. C, siete.",
    ["5 estrellas", "6 estrellas", "7 estrellas"], 1,
    "¡La B! Seis estrellas, como se vio en el Extended Look.", "GTA 5 TENÍA 5", "GTA 5 se quedaba en cinco. Y ahora la policía se fija en tu coche y en tu ropa.", ["GTA V: 5", "GTA VI: 6"],
    ["Quiz: ¿cuántas estrellas de búsqueda tiene GTA 6?", "¿5, 6 o 7 estrellas en GTA 6?", "Quiz GTA #10: la policía", "Solo los fans aciertan esto de GTA 6", "Quiz GTA 6: estrellas de búsqueda"],
    "Quiz GTA #10 con juego real del Extended Look: GTA 6 tiene 6 estrellas de búsqueda (GTA V tenía 5).",
    ["GTA 6 estrellas", "quiz GTA", "GTA 6 policía"])
for _sc, _c in zip(V74["escenas"], [(925, 1.0, 0.45), (849, 1.6, 0.35), (507, 1.0, 0.4), (760, 1.0, 0.5), (1133, 1.0, 0.5)]):
    _sc["clip"] = ("EL", _c[0], _c[1]); _sc["fx"] = _c[2]
oficial(V74)

V75 = oficial(mk("V75", "Atardeceres", JR, "Los atardeceres de GTA 6 (juego real)",
    ["Los atardeceres de GTA 6 en juego real", "GTA 6 es precioso: mira esto", "Vice City al atardecer en GTA 6", "La luz de GTA 6, en imágenes reales", "GTA 6 se ve así en PS5"],
    [E(1571, "Así se ve GTA 6 al atardecer, en juego real grabado en PlayStation 5.", "AL ATARDECER", vel=2.5, fx=0.5, sfx="Golpe"),
     E(763, "La luz del sol entre las palmeras.", "LA LUZ", fx=0.5),
     E(1136, "Vice City desde el aire.", "DESDE EL AIRE", fx=0.5),
     E(1045, "El agua, a contraluz.", "EL AGUA", vel=2.5, fx=0.45),
     F(L+"Vice City/Vice_City_27.jpg", "¿Es el GTA más bonito? Comenta.", "¿EL MÁS BONITO?", 0.5, sfx="Sting")],
    dict(texto=["AL", "ATARDECER"], sub="GTA 6", estilo="paisaje", concepto="Paisaje."),
    "Los atardeceres de GTA 6 con juego real del Extended Look, grabado por Rockstar en una PS5: Vice City, palmeras, vistas aéreas y el agua a contraluz.",
    ["GTA 6 gráficos", "GTA 6 gameplay", "Vice City"], "📌 ¿Es el GTA más bonito? 🌅"))

SHORTS = [V66, V67, V68, V69, V70, V71, V72, V73, V74, V75]
SCHED = [
    ("V66", "2026-11-19", "15:30", "2026-11-19", "16:10"),
    ("V68", "2026-11-19", "19:00", "2026-11-19", "19:40"),
    ("V67", "2026-11-20", "14:00", "2026-11-20", "14:40"),
    ("V70", "2026-11-20", "19:30", "2026-11-20", "20:10"),
    ("V75", "2026-11-20", "22:00", "2026-11-20", "22:40"),
    ("V74", "2026-11-21", "10:30", "2026-11-21", "11:10"),
    ("V71", "2026-11-21", "15:30", "2026-11-21", "16:10"),
    ("V69", "2026-11-22", "10:30", "2026-11-22", "11:10"),
    ("V72", "2026-11-22", "14:30", "2026-11-22", "15:10"),
    ("V73", "2026-11-22", "18:30", "2026-11-22", "19:10"),
]
