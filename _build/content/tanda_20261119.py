"""Tanda 4 (V41-V47). Temas elegidos con datos de vidIQ (búsquedas reales en español, 18/11/2026)."""
from content.common import S
from content.shorts3 import mk, quiz, mito

TANDA = "Tanda 4"

V41 = mito("V41", "Mito_Misma_Hora_Mundo", 6, "GTA 6 SALE A LA VEZ EN TODO EL MUNDO",
    "GTA 6 se desbloquea a la misma hora en todo el mundo.", "MITO",
    "Según el soporte de Rockstar, se desbloquea a medianoche, hora local, en cada región. Por eso Nueva Zelanda fue de los primeros países en jugar y América de los últimos.",
    ["00:00 en cada región", "N. Zelanda, de 1.ª"], "Por eso verás gente jugando horas antes que tú.",
    ["¿GTA 6 sale a la misma hora en todo el mundo?", "Por qué en Nueva Zelanda jugaron GTA 6 antes", "Mito o verdad: la hora mundial de GTA 6", "GTA 6: ¿por qué unos juegan antes?", "La hora de GTA 6 en el mundo, explicada"],
    "Mito: GTA 6 se desbloquea a medianoche, hora local, en cada región (según el soporte de Rockstar). Nueva Zelanda fue de los primeros países en jugar.",
    ["GTA 6 Nueva Zelanda", "GTA 6 hora mundial", "mito o verdad"])

V42 = mk("V42", "Descargar_en_PS5", "GUÍA RÁPIDA", "Cómo descargar GTA 6 en PS5",
    ["Cómo descargar GTA 6 en PS5 (digital y con código)", "GTA 6 en PS5: cómo descargarlo paso a paso", "¿Compraste GTA 6 en caja? Así se descarga en PS5", "Descargar GTA 6 en PS5 en 40 segundos", "GTA 6 PS5: descarga y código"],
    [S("GRAFICO", "¿Ya tienes GTA 6 y no sabes cómo descargarlo en PS5? Así se hace.", rotulo="DESCARGAR EN PS5", sfx="Golpe"),
     S("GRAFICO", "Si lo compraste en digital, entra en tu biblioteca de juegos, busca GTA 6 en la sección de comprados y pulsa descargar.", rotulo="DIGITAL", items=["Biblioteca de juegos", "Comprados → Descargar"]),
     S("GRAFICO", "Si lo compraste en caja con código, abre la PlayStation Store, pulsa el menú de los tres puntos y elige Canjear código.", rotulo="CON CÓDIGO", items=["PlayStation Store", "Menú ··· → Canjear código"]),
     S("GRAFICO", "Las tiendas hablan de unos doscientos diez gigas, y tiene que ir en el almacenamiento interno o en un SSD M.2. Un disco USB no vale para jugar.", rotulo="≈ 210 GB · INTERNO", items=["USB: solo guardar"]),
     S("GRAFICO", "Guárdalo y pásaselo a quien lo esté descargando ahora.", rotulo="GUÁRDALO", sfx="Sting")],
    dict(texto=["DESCARGAR", "EN PS5"], sub="GTA 6", estilo="checklist", concepto="Checklist."),
    "Cómo descargar GTA 6 en PS5: digital, desde Biblioteca → Comprados → Descargar; con código de la caja, PlayStation Store → menú ··· → Canjear código. Unos 210 GB según las tiendas; tiene que ir en el almacenamiento interno o en un SSD M.2.",
    ["como descargar gta 6 en ps5", "GTA 6 PS5 código", "canjear código PS5"], "📌 ¿Cuánto te ha tardado la descarga? ⏳",
    objetivo="Captar la búsqueda 'cómo descargar gta 6 en ps5' (~15.000/mes según vidIQ, competencia 35/100).")

V43 = mk("V43", "Descargar_en_Xbox", "GUÍA RÁPIDA", "Cómo descargar GTA 6 en Xbox Series",
    ["Cómo descargar GTA 6 en Xbox Series X|S", "GTA 6 en Xbox: descarga paso a paso", "¿Código de GTA 6 para Xbox? Así se canjea", "Descargar GTA 6 en Xbox en 40 segundos", "GTA 6 Xbox: descarga y código"],
    [S("GRAFICO", "¿Tienes GTA 6 para Xbox? Así lo descargas en un momento.", rotulo="DESCARGAR EN XBOX", sfx="Golpe"),
     S("GRAFICO", "Si lo reservaste en digital, entra en Mis juegos y aplicaciones, busca la sección de listo para instalar y pulsa instalar.", rotulo="DIGITAL", items=["Mis juegos y aplicaciones", "Listo para instalar"]),
     S("GRAFICO", "Si tienes un código, abre la Microsoft Store en la consola y elige Canjear. También puedes canjearlo desde el móvil o el ordenador en la web de Microsoft.", rotulo="CON CÓDIGO", items=["Microsoft Store → Canjear", "O en la web de Microsoft"]),
     S("GRAFICO", "Y en Series S, ojo con el espacio: las tiendas hablan de unos doscientos diez gigas.", rotulo="OJO CON EL ESPACIO", items=["≈ 210 GB"]),
     S("GRAFICO", "Pásaselo a tu amigo de Xbox. Nos vemos en Leonida.", rotulo="PÁSASELO", sfx="Sting")],
    dict(texto=["DESCARGAR", "EN XBOX"], sub="GTA 6", estilo="checklist", concepto="Checklist."),
    "Cómo descargar GTA 6 en Xbox Series X|S: digital, desde Mis juegos y aplicaciones → Listo para instalar; con código, Microsoft Store → Canjear (o en la web de Microsoft). Unos 210 GB según las tiendas.",
    ["como descargar gta 6 en xbox", "GTA 6 Xbox código", "canjear código Xbox"], "📌 ¿Series X o Series S? 🎮")

V44 = mk("V44", "Videos_Falsos_IA", "GUÍA RÁPIDA", "Cómo detectar vídeos falsos de GTA 6 hechos con IA",
    ["Cuidado con los vídeos falsos de GTA 6 hechos con IA", "Cómo saber si un vídeo de GTA 6 es falso", "GTA 6 e IA: 4 señales de que es fake", "Ese 'gameplay' de GTA 6 puede ser IA", "No te creas todo lo que ves de GTA 6"],
    [S("GRAFICO", "Ese vídeo de GTA 6 que se ha hecho viral puede ser falso. Así lo detectas.", rotulo="¿ES FALSO?", sfx="Golpe"),
     S("GRAFICO", "Uno: mira la fuente. Lo oficial sale en el canal de Rockstar Games y en su web. Si viene de una cuenta desconocida, desconfía.", rotulo="1 · LA FUENTE", items=["Canal oficial de Rockstar"]),
     S("GRAFICO", "Dos: fíjate en los detalles. Manos raras, textos que no se leen, coches que se deforman o físicas imposibles son señales típicas de vídeo generado con IA.", rotulo="2 · LOS DETALLES", items=["Manos y textos raros", "Objetos que se deforman"]),
     S("GRAFICO", "Tres: si promete algo demasiado bueno, como un mapa gigante o funciones que nadie más menciona, busca si algún medio fiable lo confirma.", rotulo="3 · DEMASIADO BUENO", items=["Busca otra fuente fiable"]),
     S("GRAFICO", "Aquí siempre te diremos qué es oficial y qué no. Sígueme.", rotulo="OFICIAL ≠ RUMOR", sfx="Sting")],
    dict(texto=["¿ES", "FALSO?"], sub="GTA 6 · IA", estilo="lupa", concepto="Lupa."),
    "Cómo detectar vídeos falsos de GTA 6 hechos con IA: comprueba la fuente (canal y web oficiales de Rockstar), fíjate en manos, textos y objetos que se deforman, y desconfía de lo que nadie más confirma.",
    ["gta 6 ia", "GTA 6 fake", "vídeos falsos GTA 6"], "📌 ¿Te has tragado algún fake de GTA 6? 😅",
    objetivo="Captar la búsqueda 'gta 6 ia' (~18.000/mes en España según vidIQ) y reforzar la marca de fiabilidad.")

V45 = mk("V45", "Grabar_Clips", "GUÍA RÁPIDA", "Cómo grabar clips de GTA 6 en PS5 y Xbox",
    ["Cómo grabar clips de GTA 6 en PS5 y Xbox", "Graba tus mejores momentos de GTA 6", "Clips de GTA 6: el truco de la consola", "Cómo hacer clipping de GTA 6", "No pierdas ese momentazo de GTA 6"],
    [S("GRAFICO", "¿Te acaba de pasar algo épico en GTA 6? Así lo guardas en segundos.", rotulo="GUARDA EL MOMENTAZO", sfx="Golpe"),
     S("GRAFICO", "En PS5, pulsa el botón Crear y elige guardar el juego reciente. La consola guarda lo que acaba de pasar.", rotulo="PS5 · BOTÓN CREAR", items=["Botón Crear", "Guardar juego reciente"]),
     S("GRAFICO", "En Xbox, mantén pulsado el botón Compartir para grabar lo que acaba de pasar. Una pulsación corta hace una captura.", rotulo="XBOX · BOTÓN COMPARTIR", items=["Mantener: clip", "Pulsar: captura"]),
     S("GRAFICO", "Truco: en los ajustes de capturas puedes elegir la duración y la calidad. Y antes de compartirlo, piensa en los spoilers.", rotulo="EL TRUCO", items=["Ajustes de capturas", "Cuidado con los spoilers"]),
     S("GRAFICO", "Etiquétanos en tus clips. Los mejores salen en el canal.", rotulo="ETIQUÉTANOS", sfx="Sting")],
    dict(texto=["GRABA TU", "CLIP"], sub="GTA 6", estilo="reloj", concepto="Reloj."),
    "Cómo grabar clips de GTA 6: en PS5, botón Crear → Guardar juego reciente; en Xbox, mantén pulsado Compartir (pulsación corta = captura). En los ajustes de capturas puedes cambiar duración y calidad.",
    ["como hacer clipping gta 6", "grabar clips PS5", "grabar clips Xbox"], "📌 Comparte tu mejor clip y etiquétanos 🎬",
    objetivo="Ocupar la búsqueda 'como hacer clipping gta 6' (competencia 14/100 según vidIQ).")

V46 = quiz("V46", "Quiz_Estado_Leonida", 6, "Pregunta básica para empezar el día. Tres segundos.",
    "¿EN QUÉ ESTADO TRANSCURRE GTA 6?", "¿Cómo se llama el estado ficticio donde transcurre GTA 6? A, San Andreas. B, Leonida. C, Liberty.",
    ["San Andreas", "Leonida", "Liberty"], 1,
    "¡La B! Leonida, inspirado en Florida, con Vice City como gran ciudad.", "LAS OTRAS DOS", "San Andreas era el estado de GTA 5, y Liberty City, la ciudad de GTA 3 y GTA 4.", ["San Andreas: GTA V", "Liberty City: GTA III y IV"],
    ["Quiz: ¿en qué estado transcurre GTA 6?", "¿Sabes dónde transcurre GTA 6?", "Quiz GTA #6: Leonida", "GTA 6: ¿San Andreas o Leonida?", "Curiosidades de GTA 6: quiz"],
    "Quiz GTA #6: GTA 6 transcurre en Leonida, un estado ficticio inspirado en Florida, con Vice City como gran ciudad.",
    ["gta 6 curiosidades", "Leonida", "quiz GTA"])

V47 = mk("V47", "Sin_Consola_o_Movil", "GUÍA RÁPIDA", "¿Se puede jugar GTA 6 sin consola o en el móvil?",
    ["¿Se puede jugar GTA 6 sin consola o en el móvil?", "GTA 6 en el móvil: cuidado", "¿GTA 6 sin PS5 ni Xbox? La respuesta", "GTA 6 para móvil: estafa", "Jugar GTA 6 sin consola: lo que hay"],
    [S("GRAFICO", "¿Se puede jugar a GTA 6 sin consola o en el móvil? Respuesta corta y sin rodeos.", rotulo="¿SIN CONSOLA?", sfx="Golpe"),
     S("GRAFICO", "Oficialmente, GTA 6 solo existe en PlayStation 5 y Xbox Series. No hay versión para móvil ni para PC anunciada.", rotulo="SOLO PS5 · XBOX SERIES", items=["Móvil: no", "PC: sin anunciar"]),
     S("GRAFICO", "Lo que sí puedes hacer es jugar a distancia a tu propia consola desde el móvil, con las aplicaciones de juego remoto de PlayStation o de Xbox. Pero necesitas la consola.", rotulo="JUEGO REMOTO", items=["Necesitas tu consola"]),
     S("GRAFICO", "Y cuidado: cualquier aplicación o web que te ofrezca GTA 6 para móvil o PC es una estafa.", rotulo="APPS FALSAS = ESTAFA"),
     S("GRAFICO", "Pásaselo a quien esté a punto de picar. Sígueme.", rotulo="PÁSASELO", sfx="Sting")],
    dict(texto=["¿SIN", "CONSOLA?"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "GTA 6 solo está disponible en PS5 y Xbox Series X|S; no hay versión para móvil ni versión de PC anunciada. Puedes jugar a distancia a tu propia consola con las apps de juego remoto de PlayStation o Xbox. Las apps o webs que ofrecen GTA 6 para móvil o PC son estafas.",
    ["como jugar gta 6 sin consola", "GTA 6 móvil", "como jugar gta 6 en pc"], "📌 ¿Has visto alguna app falsa de GTA 6? ⚠️",
    objetivo="Captar 'como jugar gta 6 sin consola' (~13.600/mes) y 'en pc' (~26.000/mes) según vidIQ.")

SHORTS = [V41, V42, V43, V44, V45, V46, V47]
# (id, fecha YouTube, hora, fecha TikTok, hora) · hora peninsular. Huecos libres entre la tanda 3.
SCHED = [
    ("V41", "2026-11-19", "08:15", "2026-11-19", "08:55"),
    ("V42", "2026-11-19", "12:45", "2026-11-19", "13:25"),
    ("V43", "2026-11-19", "15:45", "2026-11-19", "16:25"),
    ("V44", "2026-11-19", "19:45", "2026-11-19", "20:25"),
    ("V45", "2026-11-19", "23:15", "2026-11-19", "23:55"),
    ("V46", "2026-11-20", "08:45", "2026-11-20", "09:25"),
    ("V47", "2026-11-20", "11:45", "2026-11-20", "12:25"),
]
