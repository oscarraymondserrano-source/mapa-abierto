"""Tanda diaria 19/11/2026 (V54-V58). Temas: vidIQ (preguntas en crecimiento) + novedades verificadas del día de lanzamiento."""
from content.common import S
from content.shorts3 import mk, quiz, mito

TANDA = "Tanda 2026-11-19"

V54 = mk("V54", "Que_pasa_con_GTA5_Online", "NOTICIA", "¿Qué pasará con GTA 5 y GTA Online ahora que sale GTA 6?",
    ["¿Qué pasará con GTA 5 y GTA Online ahora que sale GTA 6?", "¿Cierra GTA Online con la llegada de GTA 6?", "GTA 5 tras GTA 6: lo que se sabe", "GTA Online y GTA 6: ¿qué pasa ahora?", "¿Adiós a GTA 5? Lo que hay de verdad"],
    [S("GRAFICO", "Sale GTA 6. ¿Y ahora qué pasa con GTA 5 y GTA Online? Esto es lo que se sabe de verdad.", rotulo="¿Y GTA 5?", sfx="Golpe"),
     S("GRAFICO", "Rockstar no ha anunciado el cierre de GTA 5 ni de GTA Online. A día de hoy, siguen funcionando.", rotulo="SIN CIERRE ANUNCIADO", items=["GTA 5: sigue", "GTA Online: sigue"]),
     S("GRAFICO", "GTA Online lleva activo desde octubre de 2013, y es uno de los juegos que más dinero ha generado a Rockstar en todos estos años.", rotulo="ACTIVO DESDE 2013"),
     S("GRAFICO", "¿Y el online de GTA 6? Rockstar tampoco lo ha detallado: en el Extended Look no enseñó nada del modo online.", rotulo="ONLINE DE GTA 6: SIN DETALLES"),
     S("GRAFICO", "Si algo cambia, aquí te lo contamos. Sígueme.", rotulo="TE AVISAMOS", sfx="Sting")],
    dict(texto=["¿Y GTA 5", "AHORA?"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "¿Qué pasará con GTA 5 y GTA Online tras el lanzamiento de GTA 6? Rockstar no ha anunciado su cierre: siguen activos. GTA Online funciona desde octubre de 2013. Rockstar tampoco ha detallado el modo online de GTA 6.",
    ["que pasara con gta 5 cuando sale gta 6", "GTA Online GTA 6", "GTA 5 cierre"], "📌 ¿Seguirás jugando a GTA Online? 👇",
    objetivo="Captar 'que pasara con gta 5 cuando sale gta 6' (~8.400 búsquedas/mes según vidIQ).")

V55 = mk("V55", "GTA6_Gratis_Estafa", "GUÍA RÁPIDA", "¿Se puede conseguir GTA 6 gratis?",
    ["¿Se puede conseguir GTA 6 gratis? Cuidado", "GTA 6 gratis: estafa", "No caigas en esto con GTA 6", "GTA 6 gratis: lo que nadie te dice", "Las estafas de GTA 6 que debes conocer"],
    [S("GRAFICO", "¿Has visto que regalan GTA 6? Para antes de pulsar nada.", rotulo="¿GTA 6 GRATIS?", sfx="Golpe"),
     S("GRAFICO", "No hay ninguna forma oficial de conseguir GTA 6 gratis. Se compra para PlayStation 5 o Xbox Series, y punto.", rotulo="NO EXISTE GRATIS"),
     S("GRAFICO", "Las webs, aplicaciones y sorteos que te lo regalan a cambio de tus datos o de tu contraseña son estafas: buscan robar tu cuenta o meterte un virus.", rotulo="ES UNA ESTAFA", items=["Robo de cuentas", "Virus y datos"]),
     S("GRAFICO", "Regla de oro: nunca des la contraseña de PlayStation o de Xbox a nadie. Ningún sorteo legal te la pedirá, ni te hará pagar para ganar.", rotulo="NUNCA TU CONTRASEÑA", items=["Ni contraseña", "Ni pagos"]),
     S("GRAFICO", "Pásaselo a quien esté a punto de picar.", rotulo="PÁSASELO", sfx="Sting")],
    dict(texto=["¿GTA 6", "GRATIS?"], sub="CUIDADO", estilo="lupa", concepto="Lupa."),
    "No existe ninguna forma oficial de conseguir GTA 6 gratis. Las webs, apps y sorteos que lo regalan a cambio de datos o contraseñas son estafas. Nunca des la contraseña de tu cuenta de PlayStation o Xbox.",
    ["como conseguir gta 6 gratis", "GTA 6 gratis", "estafas GTA 6"], "📌 ¿Has visto alguna estafa de GTA 6? Avisa a los demás 👇",
    objetivo="Captar 'como conseguir gta 6 gratis' (+87 % según vidIQ) con un mensaje de seguridad.")

V56 = mk("V56", "Metacritic_Resenas_Falsas", "NOTICIA", "Metacritic borró reseñas falsas de GTA 6",
    ["Metacritic tuvo que borrar reseñas falsas de GTA 6", "GTA 6 recibió notas antes de salir (y eran falsas)", "Lo que pasó con GTA 6 en Metacritic", "Reseñas falsas de GTA 6: qué pasó", "GTA 6 y Metacritic: la polémica"],
    [S("GRAFICO", "GTA 6 recibió notas de usuarios antes de que nadie pudiera jugarlo. Y Metacritic tuvo que intervenir.", rotulo="NOTAS SIN JUGAR", sfx="Golpe"),
     S("GRAFICO", "Días antes del lanzamiento, la página de usuarios de GTA 6 en Metacritic se llenó de puntuaciones de gente que no había podido jugar.", rotulo="RESEÑAS FALSAS"),
     S("GRAFICO", "Metacritic las borró y bloqueó las nuevas valoraciones de usuarios hasta que el juego saliera.", rotulo="BORRADAS Y BLOQUEADAS", items=["Reseñas borradas", "Bloqueo hasta la salida"]),
     S("GRAFICO", "Moraleja: antes de fiarte de una nota, mira quién la pone y si de verdad ha jugado.", rotulo="MIRA QUIÉN PUNTÚA"),
     S("GRAFICO", "¿Qué nota le pondrías tú tras las primeras horas? Comenta.", rotulo="¿TU NOTA?", sfx="Sting")],
    dict(texto=["NOTAS", "FALSAS"], sub="GTA 6", estilo="stamp", concepto="Sello."),
    "Antes del lanzamiento, la página de usuarios de GTA 6 en Metacritic recibió puntuaciones de gente que no había jugado. Metacritic las eliminó y bloqueó nuevas valoraciones de usuarios hasta la salida del juego.",
    ["GTA 6 Metacritic", "GTA 6 reseñas", "GTA 6 nota"], "📌 ¿Qué nota le pones tras las primeras horas? 🎮")

V57 = quiz("V57", "Quiz_Mejor_Nota_Metacritic", 8, "Pregunta de récord. Tres segundos.",
    "¿QUÉ GTA TIENE MEJOR NOTA?", "¿Qué GTA tiene la nota más alta de la prensa en Metacritic? A, GTA 5. B, GTA 4. C, San Andreas.",
    ["GTA 5", "GTA 4", "San Andreas"], 1,
    "¡La B! GTA 4, con un noventa y ocho en Xbox 360. Es el récord de la saga.", "MUY DE CERCA", "GTA 5 y GTA 3 se quedaron en un noventa y siete. ¿Lo superará GTA 6?", ["GTA IV: 98", "GTA V y GTA III: 97"],
    ["Quiz: ¿qué GTA tiene la mejor nota de la historia?", "El GTA con mejor nota en Metacritic", "Quiz GTA #8: el récord de la saga", "¿GTA 5 o GTA 4? La nota más alta", "¿Superará GTA 6 este récord?"],
    "Quiz GTA #8: el GTA con mejor nota de la prensa en Metacritic es GTA IV (98 en Xbox 360). GTA V y GTA III tienen 97.",
    ["GTA Metacritic", "mejor GTA", "quiz GTA"])

V58 = mk("V58", "Comprar_GTA6_Barato", "GUÍA RÁPIDA", "Cómo comprar GTA 6 más barato sin caer en estafas",
    ["Cómo comprar GTA 6 más barato (sin estafas)", "GTA 6 más barato: 3 consejos", "¿Dónde comprar GTA 6 barato?", "Ahorra en GTA 6 sin arriesgarte", "Comprar GTA 6: lo que debes mirar"],
    [S("GRAFICO", "¿Quieres GTA 6 más barato? Tres consejos para ahorrar sin jugártela.", rotulo="GTA 6 MÁS BARATO", sfx="Golpe"),
     S("GRAFICO", "Uno: compara tiendas. El precio cambia entre la tienda de la consola y las grandes cadenas, sobre todo en la versión en caja.", rotulo="1 · COMPARA", items=["Tienda digital", "Grandes cadenas"]),
     S("GRAFICO", "Dos: vigila las ofertas oficiales de PlayStation y Xbox. Las rebajas llegan, aunque en un juego recién salido tardan.", rotulo="2 · OFERTAS OFICIALES"),
     S("GRAFICO", "Y tres: evita claves de otras regiones y cuentas compartidas. Pueden no funcionar o ser revocadas, y te quedas sin juego y sin dinero.", rotulo="3 · SIN ATAJOS", items=["Claves de otra región: no", "Cuentas compartidas: no"]),
     S("GRAFICO", "Guárdalo antes de comprar. Nos vemos en Leonida.", rotulo="GUÁRDALO", sfx="Sting")],
    dict(texto=["MÁS", "BARATO"], sub="GTA 6", estilo="checklist", concepto="Checklist."),
    "Tres consejos para comprar GTA 6 más barato sin riesgos: compara la tienda digital con las grandes cadenas (sobre todo en caja), vigila las ofertas oficiales de PlayStation y Xbox, y evita claves de otras regiones y cuentas compartidas.",
    ["como comprar gta 6 barato", "GTA 6 precio", "GTA 6 oferta"], "📌 ¿Digital o en caja? 👇",
    objetivo="Captar 'como comprar gta 6 barato' (~13.800 búsquedas/mes según vidIQ).")

SHORTS = [V54, V55, V56, V57, V58]
# Horas según getBestTimeToPostByNetwork y huecos libres (≥45 min) respecto a lo programado.
SCHED = [
    ("V54", "2026-11-19", "13:40", "2026-11-19", "14:20"),
    ("V55", "2026-11-19", "17:15", "2026-11-19", "18:05"),
    ("V56", "2026-11-19", "20:40", "2026-11-19", "21:20"),
    ("V57", "2026-11-19", "22:20", "2026-11-19", "23:00"),
    ("V58", "2026-11-20", "09:40", "2026-11-20", "10:20"),
]
