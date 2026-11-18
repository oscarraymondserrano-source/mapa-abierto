"""Tanda 5 (V48-V53). Temas con demanda según vidIQ + verificación en medios (18/11/2026)."""
from content.common import S
from content.shorts3 import mk, quiz, mito

TANDA = "Tanda 5"

V48 = mk("V48", "Que_fue_el_Extended_Look", "NOTICIA", "¿Qué fue el Extended Look de GTA 6?",
    ["¿Qué fue el Extended Look de GTA 6?", "El Extended Look de GTA 6, explicado en 40 segundos", "GTA 6 Extended Look: lo que tienes que saber", "Los 27 minutos de GTA 6 que se estrenaron en Netflix", "GTA 6 en Netflix: el Extended Look"],
    [S("GRAFICO", "Si te perdiste el Extended Look de GTA 6, te lo resumo en cuarenta segundos.", rotulo="EXTENDED LOOK", sfx="Golpe"),
     S("GRAFICO", "Fue un vídeo de unos veintisiete minutos que Rockstar estrenó el 27 de agosto en Netflix y en su canal de YouTube.", rotulo="27 DE AGOSTO", items=["≈ 27 minutos", "Netflix + YouTube"]),
     S("GRAFICO", "Según Rockstar, todo estaba grabado dentro del juego en una PlayStation 5 normal, no en la versión Pro.", rotulo="GRABADO EN PS5", items=["PS5 normal, no Pro"]),
     S("GRAFICO", "Mostró a Jason y Lucia en misiones, la vuelta de las seis estrellas de búsqueda y un montón de actividades en Leonida. Lo que no enseñó fue nada del modo online.", rotulo="LO QUE ENSEÑÓ", items=["Jason y Lucia", "6 estrellas de búsqueda", "Online: nada"]),
     S("GRAFICO", "¿Lo viste entero? Dime qué fue lo que más te sorprendió.", rotulo="¿LO VISTE?", sfx="Sting")],
    dict(texto=["EXTENDED", "LOOK"], sub="GTA 6", estilo="reloj", concepto="Reloj."),
    "El Extended Look de GTA 6 fue un vídeo de unos 27 minutos estrenado el 27/08/2026 en Netflix y en el canal de YouTube de Rockstar, grabado en una PS5 estándar. Mostró a Jason y Lucia, la vuelta de las 6 estrellas de búsqueda y actividades de Leonida; no hubo información del modo online.",
    ["gta 6 extended look", "extended look gta 6", "GTA 6 Netflix"], "📌 ¿Qué fue lo que más te sorprendió del Extended Look? 👇",
    objetivo="Captar 'gta 6 extended look' (~69.000 búsquedas/mes en España según vidIQ).")

V49 = mito("V49", "Mito_Seis_Estrellas", 7, "GTA 6 TIENE 6 ESTRELLAS DE BÚSQUEDA",
    "GTA 6 tiene seis estrellas de búsqueda.", "VERDAD",
    "En el Extended Look volvieron las seis estrellas, el máximo clásico de la saga. GTA 5 se quedaba en cinco. Y la policía ahora se fija en tu coche, tu ropa y tu descripción.",
    ["GTA V: 5 estrellas", "GTA VI: 6 estrellas"], "Así que cambiar de ropa o de coche puede salvarte.",
    ["¿GTA 6 tiene 6 estrellas de búsqueda?", "Vuelven las 6 estrellas en GTA 6", "Mito o verdad: la policía de GTA 6", "GTA 6: la policía se fija en tu ropa", "6 estrellas en GTA 6: verdad"],
    "Verdad: según lo mostrado en el Extended Look (agosto de 2026), GTA 6 recupera las 6 estrellas de búsqueda (GTA V tenía 5) y la policía rastrea tu vehículo, tu ropa y tu descripción.",
    ["GTA 6 estrellas", "GTA 6 policía", "mito o verdad"])

V50 = mk("V50", "GTA6_en_South_Park", "NOTICIA", "GTA 6 apareció en South Park",
    ["GTA 6 apareció en South Park (y no era broma)", "South Park emitió gameplay real de GTA 6", "El momento de GTA 6 en South Park", "GTA 6 y South Park: lo que pasó", "17 segundos de GTA 6 en South Park"],
    [S("GRAFICO", "Uno de los primeros vistazos extra a GTA 6 no salió de Rockstar, sino de South Park.", rotulo="¿SOUTH PARK?", sfx="Golpe"),
     S("GRAFICO", "En el episodio Guinea Pig on a Stick, emitido el 28 de octubre, aparecieron diecisiete segundos seguidos de juego real de GTA 6.", rotulo="28 DE OCTUBRE", items=["17 s de juego real"]),
     S("GRAFICO", "¿Qué se veía? A Jason recogiendo una bolsa de excrementos de perro del suelo y usándola para golpear a un transeúnte. Muy South Park.", rotulo="LO QUE SE VEÍA"),
     S("GRAFICO", "Y no era un montaje: Rockstar Games aparecía en los créditos del episodio con un agradecimiento por ceder las imágenes.", rotulo="ROCKSTAR, EN LOS CRÉDITOS"),
     S("GRAFICO", "¿Lo habías visto? Comenta.", rotulo="¿LO VISTE?", sfx="Sting")],
    dict(texto=["GTA 6 EN", "SOUTH PARK"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "En el episodio 'Guinea Pig on a Stick' de South Park (temporada 29, emitido el 28/10/2026) aparecieron 17 segundos de juego real de GTA 6, con agradecimiento a Rockstar Games en los créditos.",
    ["south park gta 6", "gta 6 south park", "GTA 6 gameplay"], "📌 ¿Lo habías visto? 😂",
    objetivo="Captar 'south park gta 6' (~24.000 búsquedas/mes en España según vidIQ).")

V51 = quiz("V51", "Quiz_Extended_Look", 7, "Pregunta de actualidad. Tres segundos.",
    "¿DÓNDE SE ESTRENÓ EL EXTENDED LOOK?", "¿En qué plataforma, además del YouTube de Rockstar, se estrenó el Extended Look de GTA 6? A, Netflix. B, Twitch. C, Prime Video.",
    ["Netflix", "Twitch", "Prime Video"], 0,
    "¡La A! Netflix. Se estrenó el 27 de agosto, a la vez que en el canal de YouTube de Rockstar.", "UNOS 27 MINUTOS", "Duraba unos veintisiete minutos y estaba grabado en una PlayStation 5.", ["≈ 27 minutos", "Grabado en PS5"],
    ["Quiz: ¿dónde se estrenó el Extended Look de GTA 6?", "GTA 6 y Netflix: ¿lo sabías?", "Quiz GTA #7", "¿Sabes dónde se estrenó GTA 6?", "Quiz GTA: el Extended Look"],
    "Quiz GTA #7: el Extended Look de GTA 6 se estrenó el 27/08/2026 en Netflix y en el canal de YouTube de Rockstar.",
    ["extended look gta 6", "GTA 6 Netflix", "quiz GTA"])

V52 = mk("V52", "Como_Hacer_Stream", "GUÍA RÁPIDA", "Cómo hacer stream de GTA 6 desde PS5 o Xbox",
    ["Cómo hacer stream de GTA 6 desde PS5 o Xbox", "Retransmite GTA 6 en Twitch o YouTube desde la consola", "Stream de GTA 6 sin PC: así se hace", "Cómo emitir GTA 6 en directo", "GTA 6 en directo desde tu consola"],
    [S("GRAFICO", "¿Quieres emitir GTA 6 en directo sin ordenador? Desde la consola se puede.", rotulo="STREAM SIN PC", sfx="Golpe"),
     S("GRAFICO", "En PS5, pulsa el botón Crear y elige Transmitir. La primera vez te pedirá vincular tu cuenta de Twitch o de YouTube.", rotulo="PS5", items=["Botón Crear → Transmitir", "Twitch o YouTube"]),
     S("GRAFICO", "En Xbox Series, entra en Ajustes, Preferencias, Capturar y compartir, y activa la retransmisión con tu cuenta de Twitch.", rotulo="XBOX SERIES", items=["Capturar y compartir", "Retransmisión: Twitch"]),
     S("GRAFICO", "Consejo: comprueba tu velocidad de subida antes de empezar, y avisa en el título si vas a enseñar la historia. Spoilers, con cuidado.", rotulo="ANTES DE EMPEZAR", items=["Velocidad de subida", "Aviso de spoilers"]),
     S("GRAFICO", "Pásame el enlace de tu directo en comentarios.", rotulo="¿TU DIRECTO?", sfx="Sting")],
    dict(texto=["STREAM", "SIN PC"], sub="GTA 6", estilo="checklist", concepto="Checklist."),
    "Cómo hacer stream de GTA 6 desde la consola: en PS5, botón Crear → Transmitir (vincula Twitch o YouTube); en Xbox Series, Ajustes → Preferencias → Capturar y compartir → retransmisión con Twitch. Revisa tu velocidad de subida y avisa de spoilers.",
    ["como hacer stream de gta 6", "stream GTA 6 PS5", "stream GTA 6 Xbox"], "📌 Deja el enlace de tu directo 🎥",
    objetivo="Captar 'como hacer stream de gta 6' (búsqueda en crecimiento, +92 % según vidIQ).")

V53 = mk("V53", "Actividades_Extended_Look", "NOTICIA", "Las actividades de GTA 6 que se vieron en el Extended Look",
    ["Lo que puedes hacer en GTA 6 además de la historia", "Las actividades de GTA 6 que enseñó Rockstar", "GTA 6: buceo, carreras y salto base", "Qué hacer en Leonida: lo que se vio", "GTA 6 más allá de las misiones"],
    [S("GRAFICO", "¿Qué se puede hacer en GTA 6 además de la historia? Esto es lo que enseñó Rockstar.", rotulo="MÁS ALLÁ DE LA HISTORIA", sfx="Golpe"),
     S("GRAFICO", "En el Extended Look aparecieron carreras de motos de tierra y carreras de aceleración.", rotulo="CARRERAS", items=["Motos de tierra", "Aceleración"]),
     S("GRAFICO", "También buceo y salto base, aunque la mayoría de actividades se vieron de pasada, en un montaje rápido.", rotulo="AIRE Y AGUA", items=["Buceo", "Salto base"]),
     S("GRAFICO", "Cuánto dan de sí, lo veremos jugando. Pero Leonida promete mucho más que robar coches.", rotulo="LEONIDA PROMETE"),
     S("GRAFICO", "¿Cuál vas a probar primero? Comenta.", rotulo="¿CUÁL PRIMERO?", sfx="Sting")],
    dict(texto=["MÁS QUE", "MISIONES"], sub="GTA 6", estilo="paisaje", concepto="Paisaje."),
    "Actividades de GTA 6 que se vieron en el Extended Look (agosto de 2026): carreras de motos de tierra, carreras de aceleración, buceo y salto base, la mayoría en un montaje rápido.",
    ["gta 6 things you can do", "GTA 6 actividades", "GTA 6 extended look"], "📌 ¿Cuál vas a probar primero? 🏍️🤿")

SHORTS = [V48, V49, V50, V51, V52, V53]
# (id, fecha YouTube, hora, fecha TikTok, hora) · huecos libres respecto a tandas 3 y 4.
SCHED = [
    ("V48", "2026-11-20", "11:45", "2026-11-20", "12:25"),
    ("V50", "2026-11-21", "23:15", "2026-11-21", "23:55"),
    ("V49", "2026-11-23", "09:30", "2026-11-23", "10:10"),
    ("V51", "2026-11-23", "16:00", "2026-11-23", "16:40"),
    ("V52", "2026-11-23", "20:30", "2026-11-23", "21:10"),
    ("V53", "2026-11-24", "13:30", "2026-11-24", "14:10"),
]
