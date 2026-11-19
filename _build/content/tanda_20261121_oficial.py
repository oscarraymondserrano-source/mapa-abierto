"""Tanda con material oficial de Rockstar (V60-V65). Datos de personajes según las fichas oficiales de rockstargames.com/VI."""
from content.common import S
from content.shorts3 import mk, quiz

TANDA = "Tanda 2026-11-21 oficial"
T = "GTAVI_Launch_Trailer.mp4"
P = "People/"; L = "Places/"
PIE = "\n\nImágenes y vídeo: © Rockstar Games (material oficial de su web de descargas), con fines informativos. Mapa Abierto es un canal no oficial."

def F(rel, texto, rotulo, fx=0.5, items=None, sfx=None):
    s = S("GRAFICO", texto, rotulo=rotulo, items=items or [], **({"sfx": sfx} if sfx else {}))
    return dict(s, foto=rel, fx=fx)

def C(start, texto, rotulo, items=None, sfx=None):
    s = S("GRAFICO", texto, rotulo=rotulo, items=items or [], **({"sfx": sfx} if sfx else {}))
    return dict(s, clip=(T, start))

def oficial(v):
    v["seo"]["descripcion"] = v["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + PIE
    v["oficial"] = True
    return v

V60 = oficial(mk("V60", "Quien_es_Jason", "PERSONAJES", "¿Quién es Jason Duval?",
    ["¿Quién es Jason Duval? El protagonista de GTA 6", "Jason Duval, explicado en 30 segundos", "GTA 6: la historia de Jason", "Así es Jason, el protagonista de GTA 6", "Jason Duval: lo que dice Rockstar"],
    [F(P+"Jason Duval/Jason_Duval_02.jpg", "Este es Jason Duval, uno de los dos protagonistas de GTA 6. Esto es lo que cuenta Rockstar de él.", "JASON DUVAL", 0.45, sfx="Golpe"),
     F(P+"Jason Duval/Jason_Duval_06.jpg", "Creció rodeado de estafadores y delincuentes.", "UNA INFANCIA DIFÍCIL", 0.5),
     F(P+"Jason Duval/Jason_Duval_15.jpg", "Intentó dejar atrás una adolescencia complicada alistándose en el ejército.", "EL EJÉRCITO", 0.5),
     F(P+"Jason Duval/Jason_Duval_03.jpg", "Pero acabó en los Cayos, haciendo lo que mejor sabe: trabajar para traficantes de la zona.", "LOS CAYOS", 0.5),
     F(P+"Jason and Lucia/Jason_and_Lucia_01.jpg", "Hasta que conoce a Lucia. ¿Te gusta Jason como protagonista? Comenta.", "¿TE GUSTA?", 0.5, sfx="Sting")],
    dict(texto=["¿QUIÉN ES", "JASON?"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "Jason Duval, protagonista de GTA 6, según su ficha oficial de Rockstar: creció entre estafadores y delincuentes, pasó por el ejército para dejar atrás una adolescencia difícil y acabó en los Cayos trabajando para traficantes locales.",
    ["Jason Duval", "Jason GTA 6", "protagonista GTA 6", "personajes GTA 6"], "📌 ¿Jason o Lucia? 👇",
    objetivo="Captar búsquedas de personajes ('jason gta 6') con imagen oficial."))

V61 = oficial(mk("V61", "Quien_es_Lucia", "PERSONAJES", "¿Quién es Lucia Caminos?",
    ["¿Quién es Lucia Caminos? La protagonista de GTA 6", "Lucia, explicada en 30 segundos", "GTA 6: la historia de Lucia", "Así es Lucia, la protagonista de GTA 6", "Lucia Caminos: lo que dice Rockstar"],
    [F(P+"Lucia Caminos/Lucia_Caminos_10.jpg", "Esta es Lucia Caminos, la otra protagonista de GTA 6. Esto es lo que cuenta Rockstar de ella.", "LUCIA CAMINOS", 0.45, sfx="Golpe"),
     F(P+"Lucia Caminos/Lucia_Caminos_05.jpg", "Luchar por su familia la llevó a la penitenciaría de Leonida.", "PRISIÓN DE LEONIDA", 0.45),
     F(P+"Lucia Caminos/Lucia_Caminos_01.jpg", "Y fue pura suerte lo que la sacó de allí. Ahora quiere cambiar las cosas a su favor.", "RECIÉN SALIDA", 0.5),
     F(P+"Jason and Lucia/Jason_and_Lucia_03.jpg", "Según Rockstar, una vida con Jason podría ser su forma de salir adelante.", "SU SALIDA: JASON", 0.5),
     C(72, "¿Qué te parece Lucia como protagonista? Comenta.", "¿QUÉ TE PARECE?", sfx="Sting")],
    dict(texto=["¿QUIÉN ES", "LUCIA?"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "Lucia Caminos, protagonista de GTA 6, según su ficha oficial de Rockstar: luchar por su familia la llevó a la penitenciaría de Leonida, la suerte la sacó y una vida con Jason podría ser su salida.",
    ["Lucia Caminos", "Lucia GTA 6", "protagonista GTA 6", "personajes GTA 6"], "📌 ¿Jason o Lucia? 👇",
    objetivo="Captar búsquedas de personajes ('lucia gta 6') con imagen oficial."))

V62 = oficial(mk("V62", "Reparto_Jason", "PERSONAJES", "3 personajes de GTA 6 del entorno de Jason",
    ["3 personajes de GTA 6 que tienes que conocer", "El reparto de GTA 6: Cal, Brian y Raul", "¿Quiénes son Cal, Brian y Raul en GTA 6?", "GTA 6: los secundarios de Jason", "Los otros personajes de GTA 6"],
    [F(P+"Cal Hampton/Cal_Hampton_03.jpg", "GTA 6 no es solo Jason y Lucia. Te presento a tres secundarios oficiales.", "EL REPARTO", 0.5, sfx="Golpe"),
     F(P+"Cal Hampton/Cal_Hampton_02.jpg", "Cal Hampton: amigo de Jason, conspiranoico, y se pasa el día escuchando la radio de la Guardia Costera desde casa.", "CAL HAMPTON", 0.45),
     F(P+"Brian Heder/Brian_Heder_03.jpg", "Brian Heder: traficante veterano de los Cayos, de la vieja escuela del contrabando. Le da trabajo a Jason.", "BRIAN HEDER", 0.55),
     F(P+"Raul Bautista/Raul_Bautista_03.jpg", "Y Raul Bautista: un atracador de bancos con experiencia que busca talento para golpes grandes y arriesgados.", "RAUL BAUTISTA", 0.5),
     F(P+"Raul Bautista/Raul_Bautista_04.jpg", "¿Cuál te da más curiosidad? Comenta.", "¿CUÁL TE GUSTA?", 0.5, sfx="Sting")],
    dict(texto=["EL", "REPARTO"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "Personajes secundarios de GTA 6 según las fichas oficiales de Rockstar: Cal Hampton (amigo de Jason que escucha la radio de la Guardia Costera), Brian Heder (traficante veterano de los Cayos que da trabajo a Jason) y Raul Bautista (atracador de bancos que recluta talento para golpes arriesgados).",
    ["personajes GTA 6", "Cal Hampton", "Brian Heder", "Raul Bautista"], "📌 ¿Cuál te da más curiosidad? 👇"))

V63 = oficial(mk("V63", "Only_Raw_Records", "PERSONAJES", "Boobie Ike, Dre'Quan y Real Dimez: la música de Vice City",
    ["Los personajes de la música en GTA 6", "Only Raw Records: el sello de GTA 6", "Boobie Ike, Dre'Quan y Real Dimez", "GTA 6: quién manda en Vice City", "El reparto de Vice City en GTA 6"],
    [F(P+"Boobie Ike/Boobie_Ike_03.jpg", "En Vice City hay un sello discográfico con mucho poder. Te presento a su gente.", "VICE CITY", 0.5, sfx="Golpe"),
     F(P+"Boobie Ike/Boobie_Ike_02.jpg", "Boobie Ike: una leyenda de la calle convertida en empresario, con inmuebles, un club y un estudio de grabación.", "BOOBIE IKE", 0.45),
     F(P+"DreQuan Priest/DreQuan_Priest_04.jpg", "Dre'Quan Priest: de buscavidas a magnate de la música. Lleva Only Raw Records junto a Boobie.", "DRE'QUAN PRIEST", 0.5, items=["Only Raw Records"]),
     F(P+"Real Dimez/Real_Dimez_04.jpg", "Y Real Dimez: el dúo de rap de Bae-Luxe y Roxy, recién fichado por el sello.", "REAL DIMEZ", 0.5, items=["Bae-Luxe", "Roxy"]),
     F(P+"Real Dimez/Real_Dimez_02.jpg", "¿Qué papel tendrán en la historia? Lo veremos jugando. Comenta tu apuesta.", "¿TU APUESTA?", 0.5, sfx="Sting")],
    dict(texto=["ONLY RAW", "RECORDS"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "Personajes de GTA 6 según las fichas oficiales de Rockstar: Boobie Ike (leyenda de la calle convertida en empresario), Dre'Quan Priest (dirige Only Raw Records con Boobie) y Real Dimez (dúo de rap de Bae-Luxe y Roxy fichado por el sello).",
    ["personajes GTA 6", "Boobie Ike", "DreQuan Priest", "Real Dimez"], "📌 ¿Qué papel crees que tendrán? 👇"))

V64 = quiz("V64", "Quiz_Que_Zona_Es", 9, "Mira bien esta imagen oficial. Tres segundos.",
    "¿QUÉ ZONA DE LEONIDA ES?", "¿Qué zona de Leonida es esta? A, Vice City. B, Grassrivers. C, Ambrosia.",
    ["Vice City", "Grassrivers", "Ambrosia"], 1,
    "¡La B! Grassrivers, los pantanos de Leonida.", "INSPIRADA EN LOS EVERGLADES", "Es la versión de GTA 6 de los Everglades de Florida: agua, manglares y caimanes.", ["Pantanos", "Caimanes"],
    ["Quiz: ¿qué zona de GTA 6 es esta?", "¿Reconoces esta zona de Leonida?", "Quiz GTA #9: adivina la zona", "Solo los fans aciertan esta zona de GTA 6", "¿Vice City, Grassrivers o Ambrosia?"],
    "Quiz GTA #9 con imagen oficial de Rockstar: la zona es Grassrivers, los pantanos de Leonida, inspirados en los Everglades de Florida.",
    ["zonas GTA 6", "Grassrivers", "quiz GTA"])
_fotos = [L+"Grassrivers/Grassrivers_01.jpg", L+"Grassrivers/Grassrivers_01.jpg", L+"Grassrivers/Grassrivers_02.jpg", L+"Grassrivers/Grassrivers_06.jpg", L+"Grassrivers/Grassrivers_08.jpg"]
for _sc, _f in zip(V64["escenas"] if "escenas" in V64 else V64["scenes"], _fotos):
    _sc["foto"] = _f
oficial(V64)

V65 = oficial(mk("V65", "Asi_es_Vice_City", "LA SAGA EN 30 s", "Así es Vice City en GTA 6 (imágenes oficiales)",
    ["Así es Vice City en GTA 6", "Vice City 2026: imágenes oficiales", "La ciudad de GTA 6 en 30 segundos", "Vice City vuelve: así se ve en GTA 6", "Vice City en GTA 6, de día y de noche"],
    [F(L+"Vice City/Vice_City_15.jpg", "Vuelve Vice City. Así se ve en GTA 6, con imágenes oficiales de Rockstar.", "VICE CITY", 0.5, sfx="Golpe"),
     F(L+"Vice City/Vice_City_05.jpg", "Playas llenas de gente.", "LA PLAYA", 0.4),
     F(L+"Vice City/Vice_City_10.jpg", "Rascacielos frente al agua.", "EL SKYLINE", 0.45),
     F(L+"Vice City/Vice_City_26.jpg", "Mansiones con piscina vistas desde el aire.", "DESDE EL AIRE", 0.5),
     F(L+"Vice City/Vice_City_24.jpg", "Coches de lujo y palmeras.", "LAS CALLES", 0.5),
     F(L+"Vice City/Vice_City_27.jpg", "Y de noche, toda la ciudad encendida. La primera Vice City fue en 2002; esta es la de 2026.", "DE NOCHE", 0.5, items=["2002: Vice City", "2026: GTA 6"]),
     F(L+"Vice City/Vice_City_08.jpg", "¿De día o de noche? Comenta.", "¿DÍA O NOCHE?", 0.5, sfx="Sting")],
    dict(texto=["ASÍ ES", "VICE CITY"], sub="GTA 6", estilo="paisaje", concepto="Paisaje."),
    "Vice City en GTA 6 con imágenes oficiales de Rockstar Games: playa, rascacielos, mansiones, calles y la ciudad de noche. La primera Vice City fue GTA: Vice City (2002).",
    ["Vice City GTA 6", "Vice City", "mapa GTA 6"], "📌 ¿Vice City de día o de noche? 🌴🌃"))

SHORTS = [V60, V61, V62, V63, V64, V65]
SCHED = [
    ("V60", "2026-11-21", "13:30", "2026-11-21", "14:10"),
    ("V64", "2026-11-21", "17:30", "2026-11-21", "18:10"),
    ("V61", "2026-11-21", "20:30", "2026-11-21", "21:10"),
    ("V65", "2026-11-22", "12:30", "2026-11-22", "13:10"),
    ("V62", "2026-11-22", "16:30", "2026-11-22", "17:10"),
    ("V63", "2026-11-22", "20:30", "2026-11-22", "21:10"),
]
