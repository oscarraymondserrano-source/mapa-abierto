"""Segunda tanda de Shorts (V11-V20): solo gráficos propios, sin gameplay."""
from content.common import S
from content.final_overrides import PIE_FINAL

PIE = "\n\n" + PIE_FINAL


def short(id_, carpeta, tema, concepto, titulos, escenas, portada, desc, keywords, tags, comentario, playlist, fecha, elegido=0, just=""):
    return dict(id=id_, carpeta=carpeta, formato="short", modo="final", tema=tema, concepto=concepto, titulos=titulos, elegido=elegido,
                justificacion=just or "Pregunta o promesa concreta con 'GTA 6' al principio; cumple exactamente lo que promete.",
                escenas=escenas, miniaturas=[portada], mini_elegida=0, mini_motivo="Portada de Short.",
                seo=dict(descripcion=desc + PIE, keywords=keywords, tags=tags, hashtags=["#GTA6", "#Shorts", "#GTAVI"],
                         comentario=comentario, categoria="Videojuegos (Gaming)", playlist=playlist, fecha=fecha))


def C(tematica, publico, intencion, clic, objetivo):
    return dict(tematica=tematica, publico=publico, intencion=intencion, clic=clic, duracion="35-50 segundos", objetivo=objetivo)


V11 = short("V11", "VIDEO_11_Short_GTA6_en_PC", "¿Cuándo sale GTA 6 en PC?",
    C("Estado de la versión de PC y precedentes de Rockstar.", "Jugadores de PC.", "'gta 6 pc', 'gta 6 pc fecha'.",
      "Respuesta honesta + dato histórico que permite hacerse una idea.", "Captar la búsqueda de PC, muy alta y sin respuesta oficial."),
    ["¿Cuándo sale GTA 6 en PC?", "GTA 6 en PC: lo que nadie te dice", "¿Habrá GTA 6 para PC?", "GTA 6 PC: fecha y advertencia", "Jugadores de PC y GTA 6: la verdad"],
    [S("GRAFICO", "¿Juegas en PC y quieres GTA 6? Esto es lo que hay.", rotulo="¿GTA 6 EN PC?", items=["PS5 · Xbox Series: 19/11", "PC: sin fecha"], sfx="Golpe"),
     S("GRAFICO", "A día de hoy, Rockstar *no ha anunciado* versión de PC. El 19 de noviembre sale solo en PlayStation 5 y Xbox Series.", rotulo="PC: SIN ANUNCIAR", items=["Solo consolas el día 1"]),
     S("GRAFICO", "¿Y qué podemos esperar? Mira el historial: GTA 5 salió en consolas en 2013 y llegó a PC en abril de 2015. Red Dead Redemption 2 salió en 2018 y llegó a PC un año después.",
       rotulo="EL HISTORIAL DE ROCKSTAR", items=["GTA 5: 2013 → PC en 2015", "RDR 2: 2018 → PC en 2019"]),
     S("GRAFICO", "Así que lo razonable es pensar en *meses*, no en semanas. Pero ojo: eso es una estimación, no un anuncio.", rotulo="¿MESES? ESTIMACIÓN", items=["No es oficial"]),
     S("GRAFICO", "Y cuidado: si una web te vende una clave de GTA 6 para PC, es una *estafa*. Ahora mismo no existe.", rotulo="CLAVES DE PC = ESTAFA", items=["No compres claves"]),
     S("GRAFICO", "Sígueme y te aviso en cuanto haya fecha oficial.", rotulo="TE AVISO", sfx="Sting")],
    dict(texto=["¿Y EN", "PC?"], sub="GTA 6", estilo="reloj", concepto="Pregunta + reloj."),
    "GTA 6 sale el 19/11/2026 solo en PS5 y Xbox Series X|S. Rockstar no ha anunciado versión de PC. Precedentes: GTA 5 llegó a PC en abril de 2015 (consolas: 2013) y Red Dead Redemption 2 en 2019 (consolas: 2018). Cuidado con las webs que venden claves de PC: no existen.",
    ["GTA 6 PC", "GTA 6 PC fecha"], ["GTA 6", "GTA 6 PC", "GTA 6 PC fecha", "GTA 6 Steam", "GTA 6 ordenador", "GTA VI PC"],
    "📌 ¿Esperas la versión de PC o te pasas a consola? 👇", "GTA 6 · Shorts", "Miércoles 18/11/2026 · 11:00")

V12 = short("V12", "VIDEO_12_Short_Vice_City_1986_2026", "Vice City: de 1986 a hoy",
    C("La vuelta de Vice City a la saga y en qué se diferencia del GTA de 2002.", "Veteranos y nuevos jugadores.", "'vice city gta 6', 'gta vice city'.",
      "Nostalgia + contraste de épocas.", "Viralidad por nostalgia."),
    ["Vice City vuelve: de 1986 a hoy", "GTA 6 vuelve a Vice City (y no es la misma)", "Vice City: 2002 vs 2026", "La ciudad más mítica de GTA vuelve", "Así cambia Vice City en GTA 6"],
    [S("GRAFICO", "Vice City vuelve. Pero no es la Vice City que recuerdas.", rotulo="VICE CITY VUELVE", sfx="Golpe"),
     S("GRAFICO", "En 2002, GTA Vice City nos llevó a 1986: neones, trajes blancos, música ochentera y Tommy Vercetti.", rotulo="2002 → AÑO 1986", items=["Tommy Vercetti", "Neón y años 80"]),
     S("GRAFICO", "En 2006, Vice City Stories volvió a la misma ciudad, esta vez en 1984.", rotulo="2006 → AÑO 1984", items=["Vice City Stories"]),
     S("GRAFICO", "Y ahora GTA 6 la trae a la actualidad: en los tráileres hay móviles, redes sociales y vídeos virales por todas partes.", rotulo="2026 → HOY", items=["Móviles", "Redes sociales", "Vídeos virales"]),
     S("GRAFICO", "Mismo espíritu, el de Miami, pero con otra escala y dentro de un estado entero: Leonida.", rotulo="DENTRO DE LEONIDA"),
     S("GRAFICO", "¿Jugaste al de 2002? Dímelo en comentarios.", rotulo="¿JUGASTE AL DE 2002?", sfx="Sting")],
    dict(texto=["1986", "→ HOY"], sub="VICE CITY", estilo="paisaje", concepto="Contraste de fechas sobre atardecer."),
    "Vice City vuelve en GTA 6. En 2002, GTA Vice City transcurría en 1986; Vice City Stories (2006), en 1984. GTA 6 la lleva a la actualidad, dentro del estado de Leonida.",
    ["Vice City GTA 6", "GTA Vice City"], ["GTA 6", "Vice City", "GTA Vice City", "Tommy Vercetti", "Vice City Stories", "Leonida", "GTA VI"],
    "📌 ¿Jugaste al Vice City de 2002? 👇", "GTA 6 · Shorts", "Jueves 19/11/2026 · 18:00")

V13 = short("V13", "VIDEO_13_Short_Cronologia_13_anos", "13 años de espera: la cronología de GTA 6",
    C("Fechas clave desde GTA 5 hasta el lanzamiento de GTA 6.", "Fans y público general.", "'gta 6 cuándo sale', 'gta 6 retrasos'.",
      "Recorrido rápido y emocional por la espera.", "Hype previo al lanzamiento."),
    ["13 años esperando GTA 6, en 45 segundos", "La espera más larga de GTA, en 45 segundos", "GTA 6: toda la cronología", "De GTA 5 a GTA 6: 13 años", "Así llegó GTA 6 hasta aquí"],
    [S("GRAFICO", "Trece años esperando un juego. Así ha sido, en cuarenta y cinco segundos.", rotulo="13 AÑOS", sfx="Golpe"),
     S("GRAFICO", "Septiembre de 2013: sale GTA 5. Nadie imaginaba que habría que esperar tanto al siguiente.", rotulo="2013 · GTA 5"),
     S("GRAFICO", "Febrero de 2022: Rockstar confirma que el nuevo GTA está en desarrollo. Y en septiembre, una filtración enorme muestra material de una versión temprana.",
       rotulo="2022 · CONFIRMADO", items=["Febrero: anuncio", "Septiembre: filtración"]),
     S("GRAFICO", "Diciembre de 2023: llega el primer tráiler, y se publica antes de tiempo por otra filtración.", rotulo="2023 · TRÁILER 1"),
     S("GRAFICO", "Mayo de 2025: primer retraso, al 26 de mayo de 2026, y segundo tráiler. Noviembre de 2025: segundo retraso, al 19 de noviembre de 2026.",
       rotulo="2025 · DOS RETRASOS", items=["→ 26 de mayo de 2026", "→ 19 de noviembre de 2026"]),
     S("GRAFICO", "Y ya está aquí. ¿Desde qué año lo esperas tú?", rotulo="¿DESDE CUÁNDO ESPERAS?", sfx="Sting")],
    dict(texto=["13 AÑOS", "DE ESPERA"], sub="GTA 6", estilo="reloj", concepto="Reloj + años."),
    "La cronología de GTA 6: GTA 5 (septiembre de 2013), confirmación del desarrollo (febrero de 2022), filtración (septiembre de 2022), tráiler 1 (diciembre de 2023), retrasos de 2025 y lanzamiento el 19 de noviembre de 2026.",
    ["GTA 6 cronología", "GTA 6 retrasos"], ["GTA 6", "GTA 6 cronología", "GTA 6 retraso", "GTA 6 historia", "GTA 5", "GTA VI"],
    "📌 ¿Desde qué año lo esperas? 👇", "GTA 6 · Shorts", "Martes 17/11/2026 · 15:00")

V14 = short("V14", "VIDEO_14_Short_No_Confirmado", "Lo que Rockstar NO ha confirmado de GTA 6",
    C("Lista de lo no confirmado antes del lanzamiento.", "Jugadores saturados de rumores.", "'gta 6 rumores', 'gta 6 60 fps', 'gta 6 online'.",
      "Desmontar rumores con honestidad.", "Posicionar la marca como fiable."),
    ["Lo que NO sabemos de GTA 6 (a 2 días)", "4 cosas que Rockstar no ha confirmado", "GTA 6: rumores vs realidad", "Cuidado con estos rumores de GTA 6", "Lo que nadie sabe aún de GTA 6"],
    [S("GRAFICO", "A dos días del lanzamiento, hay cosas de GTA 6 que *nadie* sabe todavía.", rotulo="SIN CONFIRMAR", sfx="Golpe"),
     S("GRAFICO", "Uno: el rendimiento. No hay cifras oficiales de resolución ni de fotogramas por segundo.", rotulo="1 · RENDIMIENTO", items=["¿Resolución?", "¿FPS?"]),
     S("GRAFICO", "Dos: el mapa completo. Rockstar no lo ha publicado, ni su tamaño.", rotulo="2 · EL MAPA", items=["Sin mapa oficial", "Sin tamaño oficial"]),
     S("GRAFICO", "Tres: el modo online. No hay detalles para el día del lanzamiento.", rotulo="3 · EL ONLINE"),
     S("GRAFICO", "Y cuatro: la versión de PC. Sin fecha.", rotulo="4 · EL PC"),
     S("GRAFICO", "Si alguien te lo da por hecho, desconfía. Aquí te diremos siempre qué es oficial y qué no.", rotulo="OFICIAL ≠ RUMOR", sfx="Sting")],
    dict(texto=["SIN", "CONFIRMAR"], sub="GTA 6", estilo="checklist", concepto="Checklist."),
    "Lo que Rockstar todavía no ha confirmado de GTA 6 a 17/11/2026: rendimiento (resolución y FPS), mapa completo y su tamaño, modo online en el lanzamiento y versión de PC.",
    ["GTA 6 rumores", "GTA 6 sin confirmar"], ["GTA 6", "GTA 6 rumores", "GTA 6 60 fps", "GTA 6 online", "GTA 6 mapa", "GTA 6 PC", "GTA VI"],
    "📌 ¿Qué rumor te has creído hasta hoy? 😅", "GTA 6 · Shorts", "Martes 17/11/2026 · 12:00")

V15 = short("V15", "VIDEO_15_Short_Xbox_Series_S", "Xbox Series S y GTA 6: lo que debes saber",
    C("Espacio y expectativas para quien juega en Series S.", "Usuarios de Xbox Series S.", "'gta 6 series s', 'gta 6 series s espacio'.",
      "Problema concreto de espacio.", "Nicho con alta intención y poca competencia."),
    ["¿Tienes Xbox Series S? Mira esto antes de GTA 6", "GTA 6 en Series S: el problema del espacio", "Series S y GTA 6: lo que debes saber",
     "GTA 6 en Series S: ¿cabe?", "Series S: prepárate para GTA 6"],
    [S("GRAFICO", "¿Juegas en Xbox Series S? Entonces tienes un problema con GTA 6. Y tiene solución.", rotulo="¿SERIES S?", sfx="Golpe"),
     S("GRAFICO", "La Series S tiene un disco de 512 gigas, pero el espacio libre real ronda los 364.", rotulo="≈ 364 GB LIBRES", items=["Disco de 512 GB"]),
     S("GRAFICO", "Y las tiendas hablan de unos 210 gigas para GTA 6. Más de la mitad de tu consola.", rotulo="GTA 6 ≈ 210 GB", items=["Dato de tiendas, no oficial"]),
     S("GRAFICO", "Solución: borra juegos hoy, o usa la tarjeta de expansión oficial. Un disco USB solo sirve para guardarlo, no para jugarlo.",
       rotulo="LA SOLUCIÓN", items=["Borra juegos hoy", "Tarjeta de expansión", "USB: solo guardar"]),
     S("GRAFICO", "¿Y el rendimiento en Series S? Rockstar no lo ha detallado. Lo veremos el día 19.", rotulo="RENDIMIENTO: SIN DATOS"),
     S("GRAFICO", "Pásaselo a tu amigo de la Series S.", rotulo="PÁSASELO", sfx="Sting")],
    dict(texto=["¿CABE EN", "SERIES S?"], sub="GTA 6", estilo="almacen", concepto="Barra de almacenamiento."),
    "GTA 6 en Xbox Series S: el disco es de 512 GB con unos 364 GB libres, y las tiendas hablan de unos 210 GB para el juego (no es una cifra oficial de Rockstar). Libera espacio o usa la tarjeta de expansión oficial; un disco USB solo sirve para almacenar.",
    ["GTA 6 Series S", "GTA 6 espacio Series S"], ["GTA 6", "GTA 6 Series S", "Xbox Series S", "GTA 6 espacio", "GTA 6 Xbox", "GTA VI"],
    "📌 ¿Cuántos juegos has borrado? 😭", "GTA 6 · Shorts", "Miércoles 18/11/2026 · 09:30")

V16 = short("V16", "VIDEO_16_Short_Diferencias_GTA5", "3 cosas que cambian respecto a GTA 5",
    C("Diferencias confirmadas entre GTA 5 y GTA 6.", "Jugadores de GTA 5.", "'gta 6 vs gta 5', 'gta 6 diferencias'.",
      "Comparativa directa con algo que conocen.", "Captar a la enorme base de jugadores de GTA 5."),
    ["GTA 6 vs GTA 5: 3 cambios confirmados", "3 cosas que GTA 5 no tenía", "GTA 6 no es GTA 5 con otro mapa", "Lo que cambia de GTA 5 a GTA 6", "GTA 5 → GTA 6: 3 diferencias"],
    [S("GRAFICO", "Si vienes de GTA 5, estas tres cosas cambian en GTA 6. Y son oficiales.", rotulo="GTA 5 → GTA 6", sfx="Golpe"),
     S("GRAFICO", "Una: los protagonistas. En GTA 5 eran tres hombres por separado. En GTA 6 es una pareja: Jason y Lucia.", rotulo="1 · UNA PAREJA", items=["GTA 5: tres protagonistas", "GTA 6: Jason y Lucia"]),
     S("GRAFICO", "Dos: el escenario. De San Andreas, inspirado en California, a Leonida, inspirado en Florida.", rotulo="2 · DE CALIFORNIA A FLORIDA", items=["San Andreas → Leonida"]),
     S("GRAFICO", "Tres: según Rockstar, es el primer GTA con mecánicas que fomentan la empatía. Opcionales, eso sí: el caos sigue ahí.", rotulo="3 · EMPATÍA OPCIONAL"),
     S("GRAFICO", "¿Cuál de los tres cambios te convence más?", rotulo="¿CUÁL PREFIERES?", sfx="Sting")],
    dict(texto=["GTA 5", "→ GTA 6"], sub="3 CAMBIOS", estilo="checklist", concepto="Checklist."),
    "Tres diferencias confirmadas entre GTA 5 y GTA 6: pareja protagonista (Jason y Lucia) en lugar de tres protagonistas, Leonida (Florida) en lugar de San Andreas (California) y mecánicas opcionales de empatía, según Rockstar en The Guardian.",
    ["GTA 6 vs GTA 5", "GTA 6 diferencias"], ["GTA 6", "GTA 5", "GTA 6 vs GTA 5", "GTA 6 diferencias", "Jason y Lucia", "Leonida", "GTA VI"],
    "📌 ¿Echarás de menos a Trevor? 👇", "GTA 6 · Shorts", "Sábado 21/11/2026 · 19:00")

V17 = short("V17", "VIDEO_17_Short_Tamano_del_Mapa", "¿Cuánto mide el mapa de GTA 6?",
    C("Por qué no hay una cifra fiable del tamaño del mapa.", "Curiosos del mapa.", "'gta 6 tamaño mapa', 'gta 6 mapa km'.",
      "Desmontar cifras inventadas.", "Captar búsqueda alta con respuesta honesta."),
    ["¿Cuánto mide el mapa de GTA 6? La verdad", "El tamaño del mapa de GTA 6 (no te creas cualquier cifra)", "GTA 6: ¿más grande que GTA 5?",
     "Mapa de GTA 6: ¿cuántos km?", "Nadie sabe cuánto mide el mapa de GTA 6"],
    [S("GRAFICO", "¿Cuánto mide el mapa de GTA 6? Si alguien te da una cifra exacta, sigue leyendo.", rotulo="¿CUÁNTO MIDE?", sfx="Golpe"),
     S("GRAFICO", "Rockstar *no ha publicado* ni el mapa completo ni su tamaño.", rotulo="CIFRA OFICIAL: NINGUNA"),
     S("GRAFICO", "Los mapas que ves por internet los hacen fans, uniendo planos de los tráileres. Son un trabajo increíble, pero son estimaciones.",
       rotulo="MAPAS DE FANS", items=["Hechos con los tráileres", "Son estimaciones"]),
     S("GRAFICO", "Lo que sí sabemos: seis regiones, de Vice City a Mount Kalaga, y el escenario más variado de la saga.", rotulo="LO QUE SÍ SABEMOS", items=["6 regiones", "Ciudad, islas, pantanos"]),
     S("GRAFICO", "Cuando salga, lo mediremos nosotros. Sígueme para verlo.", rotulo="LO MEDIREMOS", sfx="Sting")],
    dict(texto=["¿CUÁNTO", "MIDE?"], sub="MAPA GTA 6", estilo="mapa", concepto="Esquema de regiones."),
    "Rockstar no ha publicado el tamaño del mapa de GTA 6. Los mapas que circulan son estimaciones de fans a partir de los tráileres. Lo confirmado: seis regiones en Leonida.",
    ["GTA 6 tamaño mapa", "mapa GTA 6"], ["GTA 6", "mapa GTA 6", "GTA 6 tamaño mapa", "GTA 6 km", "Leonida", "GTA VI"],
    "📌 ¿Más grande o más pequeño que GTA 5? Apuesta 👇", "GTA 6 · Shorts", "Miércoles 18/11/2026 · 17:00")

V18 = short("V18", "VIDEO_18_Short_3_Errores_Lanzamiento", "3 errores que vas a cometer esta noche con GTA 6",
    C("Errores típicos la noche del lanzamiento.", "Quien juega a medianoche.", "'gta 6 lanzamiento', 'gta 6 no me deja jugar'.",
      "Evitar frustración inminente.", "Publicar justo antes del desbloqueo."),
    ["3 errores que vas a cometer esta noche con GTA 6", "No hagas esto la noche de GTA 6", "Esta noche sale GTA 6: evita estos errores",
     "GTA 6 a medianoche: 3 fallos típicos", "Antes de las 00:00, revisa esto"],
    [S("GRAFICO", "Esta noche sale GTA 6, y hay tres errores que mucha gente va a cometer.", rotulo="3 ERRORES", sfx="Golpe"),
     S("GRAFICO", "Uno: no precargar. Si a las doce empiezas a descargar más de doscientos gigas, no juegas hasta mañana.", rotulo="1 · NO PRECARGAR", items=["≈ 210 GB"]),
     S("GRAFICO", "Dos: no dejar margen de espacio. El parche del primer día también ocupa. Deja libres unos cuarenta gigas extra.", rotulo="2 · SIN MARGEN", items=["Parche del día 1"]),
     S("GRAFICO", "Y tres: entrar en redes. A medianoche van a llover *spoilers*. Silencia palabras clave antes de jugar.", rotulo="3 · LOS SPOILERS", items=["Silencia palabras clave"]),
     S("GRAFICO", "Revisa estas tres cosas y nos vemos en Leonida.", rotulo="NOS VEMOS EN LEONIDA", sfx="Sting")],
    dict(texto=["3 ERRORES", "ESTA NOCHE"], sub="GTA 6", estilo="reloj", concepto="Reloj 00:00."),
    "Tres errores típicos la noche del lanzamiento de GTA 6: no precargar (unos 210 GB según las tiendas), no dejar espacio para el parche del primer día y entrar en redes sin silenciar spoilers.",
    ["GTA 6 lanzamiento", "GTA 6 esta noche"], ["GTA 6", "GTA 6 lanzamiento", "GTA 6 precarga", "GTA 6 spoilers", "GTA 6 medianoche", "GTA VI"],
    "📌 ¿Todo listo para las 00:00? ✅", "GTA 6 · Shorts", "Miércoles 18/11/2026 · 22:30")

V19 = short("V19", "VIDEO_19_Short_El_Caiman_Viral", "El caimán del tráiler de GTA 6",
    C("El momento viral del caimán y su relación con Florida y Grassrivers.", "Público general y fans.", "'gta 6 caimán', 'gta 6 florida man'.",
      "Humor + curiosidad real.", "Short ligero con alto potencial de compartidos."),
    ["El caimán más famoso de GTA 6", "Por qué hay un caimán en una tienda en GTA 6", "GTA 6 y el 'Florida Man'", "El momento más loco del tráiler de GTA 6", "GTA 6: el caimán tiene explicación"],
    [S("GRAFICO", "Un caimán entrando en una tienda. Uno de los momentos más comentados del primer tráiler de GTA 6.", rotulo="EL CAIMÁN", sfx="Golpe"),
     S("GRAFICO", "¿Por qué? Porque Leonida está inspirada en Florida, y allí los caimanes en sitios inesperados son casi un clásico de las noticias locales.", rotulo="LEONIDA = FLORIDA"),
     S("GRAFICO", "De hecho, internet tiene hasta un nombre para las noticias más locas de Florida: el *Florida Man*. Y el tráiler está lleno de guiños a ese humor.", rotulo="EL «FLORIDA MAN»"),
     S("GRAFICO", "En el juego, los humedales de Grassrivers, inspirados en los Everglades, prometen muchos más encuentros con estos vecinos.", rotulo="GRASSRIVERS", items=["Inspiración: Everglades"]),
     S("GRAFICO", "¿Qué es lo más loco que esperas ver en Leonida?", rotulo="¿LO MÁS LOCO?", sfx="Sting")],
    dict(texto=["EL", "CAIMÁN"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "El caimán del primer tráiler de GTA 6 tiene explicación: Leonida está inspirada en Florida, famosa por sus noticias locales insólitas (el meme del 'Florida Man'). En el juego, la región de Grassrivers está inspirada en los Everglades.",
    ["GTA 6 caimán", "GTA 6 Florida Man"], ["GTA 6", "GTA 6 caimán", "Florida Man", "Grassrivers", "Everglades", "GTA 6 tráiler", "GTA VI"],
    "📌 ¿Qué es lo más loco que esperas ver en Leonida? 🐊", "GTA 6 · Shorts", "Viernes 20/11/2026 · 13:00")

V20 = short("V20", "VIDEO_20_Short_Leonida_es_Florida", "Leonida es Florida: cada zona y su inspiración",
    C("Equivalencias reales de las regiones de Leonida.", "Curiosos de la geografía del juego.", "'leonida gta 6', 'gta 6 florida'.",
      "Conectar el juego con lugares reales.", "Complementar al vídeo largo del mapa (V03)."),
    ["Leonida es Florida: cada zona explicada", "Los lugares reales de GTA 6", "GTA 6: ¿qué zona es cada sitio de Florida?", "La Florida escondida en GTA 6", "De Miami a los Cayos: GTA 6 real"],
    [S("GRAFICO", "Cada zona de GTA 6 tiene un lugar real detrás. Te lo explico en cuarenta segundos.", rotulo="LEONIDA = FLORIDA", sfx="Golpe"),
     S("GRAFICO", "Vice City es Miami. Los Cayos de Leonida, los Cayos de Florida. Y Grassrivers, los Everglades.", rotulo="EL SUR", items=["Vice City → Miami", "Cayos → Florida Keys", "Grassrivers → Everglades"]),
     S("GRAFICO", "Port Gellhorn, según la comunidad, recuerda al Panhandle, el norte costero de Florida. Y Ambrosia, a su zona azucarera del interior.", rotulo="EL NORTE", items=["Port Gellhorn → Panhandle", "Ambrosia → zona azucarera"]),
     S("GRAFICO", "¿Y Mount Kalaga? Florida no tiene montañas de verdad. Ahí Rockstar se ha tomado licencias, como hizo con el monte Chiliad en GTA 5.", rotulo="¿Y LA MONTAÑA?", items=["Licencia creativa"]),
     S("GRAFICO", "El vídeo completo del mapa está en el canal. ¿Cuál vas a visitar primero?", rotulo="¿PRIMERA ZONA?", sfx="Sting")],
    dict(texto=["LEONIDA", "= FLORIDA"], sub="GTA 6", estilo="mapa", concepto="Esquema de regiones."),
    "Las inspiraciones reales de Leonida: Vice City (Miami), Cayos de Leonida (Cayos de Florida), Grassrivers (Everglades), Port Gellhorn (Panhandle, según la comunidad), Ambrosia (zona azucarera del interior) y Mount Kalaga (licencia creativa: Florida no tiene montañas).",
    ["Leonida GTA 6", "GTA 6 Florida"], ["GTA 6", "Leonida", "GTA 6 Florida", "Vice City Miami", "Cayos de Leonida", "Grassrivers", "Port Gellhorn", "Ambrosia", "Mount Kalaga", "GTA VI"],
    "📌 ¿Has estado en Florida? ¿Qué zona reconoces? 👇", "GTA 6 · Shorts", "Sábado 21/11/2026 · 13:00")

SHORTS2 = [V11, V12, V13, V14, V15, V16, V17, V18, V19, V20]
