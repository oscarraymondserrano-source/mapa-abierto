"""Quiz y Mito o verdad con juego real del Extended Look (V76-V83). Datos ya verificados en tandas anteriores o en fuentes citadas."""
from content.shorts3 import quiz, mito

TANDA = "Tanda 2026-11-19 quiz y mitos con juego real"
TR = "GTAVI_Launch_Trailer.mp4"
PIE = "\n\nImágenes y vídeo: © Rockstar Games (material oficial de su web de descargas, incluido el Extended Look), con fines informativos. Mapa Abierto es un canal no oficial."

def real(v, clips):
    """clips: lista por escena de (fuente, segundo, vel, fx); fuente 'EL' o el tráiler."""
    for sc, (src, t, vel, fx) in zip(v["escenas"], clips):
        sc["clip"] = (src, t, vel); sc["fx"] = fx
    v["seo"]["descripcion"] = v["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + PIE
    v["oficial"] = True
    return v

V76 = real(quiz("V76", "Quiz_Zonas_Leonida", 11, "Pregunta con juego real. Tres segundos.",
    "¿CUÁNTAS ZONAS TIENE LEONIDA?", "¿En cuántas zonas grandes se divide Leonida? A, cuatro. B, seis. C, ocho.",
    ["4 zonas", "6 zonas", "8 zonas"], 1,
    "¡La B! Seis zonas, según Rockstar.", "LAS 6 ZONAS", "Vice City, los Cayos de Leonida, Grassrivers, Port Gellhorn, Ambrosia y Mount Kalaga.", ["Vice City", "Cayos · Grassrivers", "Port Gellhorn · Ambrosia", "Mount Kalaga"],
    ["Quiz: ¿cuántas zonas tiene el mapa de GTA 6?", "¿4, 6 u 8 zonas en GTA 6?", "Quiz GTA #11: el mapa de Leonida", "¿Conoces el mapa de GTA 6?", "Quiz GTA 6: las zonas de Leonida"],
    "Quiz GTA #11 con juego real: Leonida, el estado de GTA 6, se divide en 6 zonas: Vice City, los Cayos de Leonida, Grassrivers, Port Gellhorn, Ambrosia y Mount Kalaga.",
    ["mapa GTA 6", "zonas GTA 6", "quiz GTA"]),
    [("EL", 1133, 1, .5), ("EL", 506, 1, .4), ("EL", 1030, 2.5, .5), ("EL", 760, 1, .5), ("EL", 1571, 2.5, .5)])

V77 = real(quiz("V77", "Quiz_Duracion_Extended_Look", 12, "Pregunta con juego real. Tres segundos.",
    "¿CUÁNTO DURÓ EL EXTENDED LOOK?", "¿Cuánto duraba el Extended Look de GTA 6? A, diez minutos. B, unos veintisiete. C, una hora.",
    ["10 minutos", "≈ 27 minutos", "1 hora"], 1,
    "¡La B! Unos veintisiete minutos de juego.", "GRABADO EN PS5", "Y según Rockstar, todo estaba grabado en una PlayStation 5 normal. Como estas imágenes.", ["PS5 normal, no Pro"],
    ["Quiz: ¿cuánto duró el Extended Look de GTA 6?", "¿10, 27 o 60 minutos?", "Quiz GTA #12: el Extended Look", "¿Viste entero el Extended Look?", "Quiz GTA 6: juego real"],
    "Quiz GTA #12 con juego real: el Extended Look de GTA 6 (27/08/2026) duraba unos 27 minutos y, según Rockstar, se grabó en una PS5 estándar.",
    ["GTA 6 extended look", "quiz GTA", "GTA 6 gameplay"]),
    [("EL", 925, 1, .45), ("EL", 512, 1, .4), ("EL", 1222, 1.4, .5), ("EL", 1003, 1, .45), ("EL", 1136, 1, .5)])

V78 = real(quiz("V78", "Quiz_Vice_City_Miami", 13, "Pregunta fácil… o no. Tres segundos.",
    "¿EN QUÉ CIUDAD SE INSPIRA VICE CITY?", "¿En qué ciudad real se inspira Vice City? A, Los Ángeles. B, Nueva York. C, Miami.",
    ["Los Ángeles", "Nueva York", "Miami"], 2,
    "¡La C! Miami. Y Leonida entera es la versión de Rockstar de Florida.", "LOS ÁNGELES Y NUEVA YORK", "Los Ángeles es Los Santos, y Nueva York, Liberty City.", ["Los Santos = Los Ángeles", "Liberty City = Nueva York"],
    ["Quiz: ¿en qué ciudad se inspira Vice City?", "¿Vice City es Miami?", "Quiz GTA #13: Vice City", "Solo los fans aciertan esto", "Quiz GTA 6: la ciudad real"],
    "Quiz GTA #13 con juego real: Vice City se inspira en Miami, y Leonida es la versión de Florida de GTA 6. Los Santos se inspira en Los Ángeles y Liberty City en Nueva York.",
    ["Vice City", "Vice City Miami", "quiz GTA"]),
    [("EL", 518, 1, .45), ("EL", 524, 1, .45), ("EL", 1136, 1, .5), ("EL", 760, 1, .5), ("EL", 1571, 2.5, .5)])

V79 = real(quiz("V79", "Quiz_Anos_GTA5_GTA6", 14, "Pregunta de paciencia. Tres segundos.",
    "¿CUÁNTOS AÑOS ENTRE GTA 5 Y GTA 6?", "¿Cuántos años han pasado entre GTA 5 y GTA 6? A, diez. B, trece. C, quince.",
    ["10 años", "13 años", "15 años"], 1,
    "¡La B! Trece años: GTA 5 salió en septiembre de 2013 y GTA 6, este noviembre de 2026.", "LA ESPERA MÁS LARGA", "Nunca había pasado tanto tiempo entre dos GTA principales.", ["2013: GTA V", "2026: GTA VI"],
    ["Quiz: ¿cuántos años hemos esperado GTA 6?", "¿10, 13 o 15 años?", "Quiz GTA #14: la espera", "13 años esperando GTA 6", "Quiz GTA 6: la espera más larga"],
    "Quiz GTA #14 con juego real: entre GTA V (septiembre de 2013) y GTA VI (noviembre de 2026) han pasado 13 años, la espera más larga entre dos GTA principales.",
    ["GTA 6", "GTA 5", "quiz GTA"]),
    [("EL", 1571, 2.5, .5), ("EL", 530, 1, .4), ("EL", 1003, 1, .45), ("EL", 925, 1, .45), ("EL", 1133, 1, .5)])

V80 = real(mito("V80", "Mito_Dos_Protagonistas", 8, "GTA 6 TIENE DOS PROTAGONISTAS",
    "GTA 6 tiene dos protagonistas.", "VERDAD",
    "Jason Duval y Lucia Caminos, una pareja que se mete en un golpe que sale mal.",
    ["Jason Duval", "Lucia Caminos"], "¿Con quién vas a jugar más?",
    ["¿GTA 6 tiene dos protagonistas? Mito o verdad", "Jason y Lucia: ¿dos protagonistas?", "Mito o verdad: los protagonistas de GTA 6", "GTA 6: ¿uno, dos o tres protagonistas?", "Los protagonistas de GTA 6: verdad"],
    "Verdad: GTA 6 tiene dos protagonistas, Jason Duval y Lucia Caminos. Según Rockstar, cuando un golpe fácil sale mal acaban metidos en una conspiración criminal por todo Leonida.",
    ["Jason y Lucia", "protagonistas GTA 6", "mito o verdad"]),
    [("EL", 1003, 1, .45), (TR, 39, 1.6, .5), ("EL", 512, 1, .4)])

V81 = real(mito("V81", "Mito_PS5_Pro", 9, "EL EXTENDED LOOK SE GRABÓ EN PS5 PRO",
    "El Extended Look de GTA 6 se grabó en una PS5 Pro.", "MITO",
    "Según Rockstar, todo se grabó dentro del juego en una PlayStation 5 normal. Lo que ves aquí es eso.",
    ["PS5 normal", "No Pro"], "Así que en tu PS5 se verá así.",
    ["¿GTA 6 se grabó en PS5 Pro? Mito o verdad", "El Extended Look y la PS5 Pro: la verdad", "¿Hace falta PS5 Pro para GTA 6?", "Mito o verdad: GTA 6 en PS5", "GTA 6 se ve así en una PS5 normal"],
    "Mito: según Rockstar, el Extended Look de GTA 6 se grabó en una PS5 estándar, no en la versión Pro.",
    ["GTA 6 PS5", "GTA 6 PS5 Pro", "mito o verdad"]),
    [("EL", 760, 1, .5), ("EL", 506, 1, .4), ("EL", 1571, 2.5, .5)])

V82 = real(mito("V82", "Mito_Lucia_Primera_Mujer", 10, "LUCIA ES LA PRIMERA MUJER JUGABLE",
    "Lucia es el primer personaje femenino jugable de la saga GTA.", "MITO",
    "En el primer GTA, de 1997, ya podías elegir personajes femeninos. Lo nuevo es que Lucia es protagonista de la historia, al nivel de Jason.",
    ["GTA (1997): ya había", "GTA 6: protagonista"], "Un cambio grande para la saga.",
    ["¿Lucia es la primera mujer jugable de GTA? Mito", "Mito o verdad: Lucia y la saga GTA", "El dato de Lucia que casi nadie sabe", "¿Primera mujer en GTA? No exactamente", "Lucia, GTA 6: mito o verdad"],
    "Mito: en el primer GTA (1997) ya se podía elegir personajes femeninos. La novedad de GTA 6 es que Lucia es protagonista de la historia junto a Jason.",
    ["Lucia GTA 6", "historia GTA", "mito o verdad"]),
    [("EL", 1003, 1, .45), ("EL", 1222, 2.0, .5), ("EL", 760, 1, .5)])

V83 = real(mito("V83", "Mito_Hidrodeslizadores", 11, "PASEOS POR EL PANTANO",
    "En GTA 6 puedes ir en hidrodeslizador por los pantanos.", "VERDAD",
    "Se vio en el Extended Look: hidrodeslizador por Grassrivers, la versión de los Everglades. Y también motos de agua.",
    ["Hidrodeslizador", "Moto de agua"], "Y cuidado con los caimanes.",
    ["¿Hay hidrodeslizadores en GTA 6? Mito o verdad", "GTA 6: hidrodeslizador por los pantanos", "Mito o verdad: vehículos de GTA 6", "Así son los pantanos de GTA 6", "Hidrodeslizador en GTA 6: verdad"],
    "Verdad: en el Extended Look de GTA 6 se vio un hidrodeslizador por Grassrivers, la zona de pantanos inspirada en los Everglades, y también motos de agua.",
    ["GTA 6 vehículos", "Grassrivers", "mito o verdad"]),
    [("EL", 1030, 2.5, .5), ("EL", 1030.3, 4.0, .45), ("EL", 1045, 2.5, .45)])

SHORTS = [V76, V77, V78, V79, V80, V81, V82, V83]
SCHED = [
    ("V78", "2026-11-23", "12:30", "2026-11-23", "13:10"),
    ("V80", "2026-11-23", "18:15", "2026-11-23", "18:55"),
    ("V76", "2026-11-23", "22:15", "2026-11-23", "22:55"),
    ("V81", "2026-11-24", "10:30", "2026-11-24", "11:10"),
    ("V77", "2026-11-24", "16:30", "2026-11-24", "17:10"),
    ("V83", "2026-11-24", "19:30", "2026-11-24", "20:10"),
    ("V79", "2026-11-24", "22:00", "2026-11-24", "22:40"),
    ("V82", "2026-11-25", "13:00", "2026-11-25", "13:40"),
]
