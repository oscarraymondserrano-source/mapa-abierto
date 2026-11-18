"""Tercera tanda (V21-V40): 20 Shorts en 5 series con formato propio. Solo gráficos propios y datos verificables."""
from content.common import S
from content.final_overrides import PIE_FINAL

PIE = "\n\n" + PIE_FINAL
BASE_TAGS = ["GTA 6", "GTA VI", "Grand Theft Auto", "GTA", "Mapa Abierto"]


def mk(id_, slug, serie, tema, titulos, escenas, portada, desc, tags, comentario, publico="Fans de GTA y jugadores que esperan GTA 6.", intencion="", clic="", objetivo=""):
    return dict(id=id_, carpeta=f"VIDEO_{id_[1:]}_Short_{slug}", formato="short", modo="final", serie=serie, barra=True, tema=tema,
                concepto=dict(tematica=tema, publico=publico, intencion=intencion or ", ".join(tags[:3]).lower(),
                              clic=clic or "Formato de serie reconocible + reto o dato sorprendente en los 2 primeros segundos.",
                              duracion="30-45 segundos", objetivo=objetivo or "Retención alta (formato interactivo) y comentarios."),
                titulos=titulos, elegido=0, justificacion="Gancho directo con la palabra clave; el formato de serie se reconoce en el feed.",
                escenas=escenas, miniaturas=[portada], mini_elegida=0, mini_motivo="Portada de Short.",
                seo=dict(descripcion=desc + PIE, keywords=tags[:2], tags=BASE_TAGS + tags, hashtags=["#GTA6", "#Shorts", "#GTAVI"],
                         comentario=comentario, categoria="Videojuegos (Gaming)", playlist="GTA 6 · Shorts", fecha=""))


def quiz(id_, slug, n, hook, pregunta_rot, pregunta_txt, opciones, correcta, revelado_txt, extra_rot, extra_txt, extra_items, titulos, desc, tags):
    L = "ABC"[correcta]
    return mk(id_, slug, f"QUIZ GTA · #{n}", "Quiz: " + pregunta_rot, titulos, [
        S("GRAFICO", hook, rotulo="¿ERES FAN DE VERDAD?", sfx="Golpe"),
        dict(S("GRAFICO", pregunta_txt, rotulo=pregunta_rot, sfx="Tic-tac en la pausa"), quiz=dict(options=opciones, correct=correcta), hold=3),
        dict(S("GRAFICO", revelado_txt, rotulo=f"RESPUESTA: {L}", sfx="Acierto"), quiz=dict(options=opciones, correct=correcta, reveal=True)),
        S("GRAFICO", extra_txt, rotulo=extra_rot, items=extra_items),
        S("GRAFICO", "¿Acertaste? Dímelo en comentarios y sígueme para el siguiente quiz.", rotulo="¿ACERTASTE?", sfx="Sting"),
    ], dict(texto=["QUIZ", f"GTA #{n}"], sub="¿ACIERTAS?", estilo="quiz", concepto="Opciones A/B/C."),
        desc, tags, "📌 ¿Cuál marcaste? Sé sincero 😅 Mañana, otro quiz.")


def mito(id_, slug, n, afirmacion_rot, afirmacion_txt, veredicto, explic_txt, explic_items, cierre_txt, titulos, desc, tags):
    return mk(id_, slug, f"MITO O VERDAD · #{n}", "Mito o verdad: " + afirmacion_rot, titulos, [
        S("GRAFICO", "¿Mito o verdad? " + afirmacion_txt, rotulo=afirmacion_rot, sfx="Golpe"),
        dict(S("GRAFICO", ("¡Mito! " if veredicto == "MITO" else "¡Verdad! ") + explic_txt, rotulo=afirmacion_rot, items=explic_items, sfx="Sello"), stamp=veredicto),
        S("GRAFICO", cierre_txt + " Sígueme para más mitos y verdades de GTA.", rotulo="SÍGUEME", sfx="Sting"),
    ], dict(texto=["¿MITO O", "VERDAD?"], sub="GTA 6", estilo="stamp", concepto="Sello rojo."),
        desc, tags, "📌 ¿Te lo creías? 👇 Propón el próximo mito en comentarios.")


SAGA = "LA SAGA EN 30 s"

V21 = mito("V21", "Mito_PS4", 1, "GTA 6 SALE EN PS4",
    "GTA 6 también sale en PlayStation 4.", "MITO",
    "Rockstar solo ha anunciado GTA 6 para PlayStation 5 y Xbox Series X y Series S. Ni PS4 ni Xbox One.",
    ["Solo PS5", "Solo Xbox Series X|S"], "Si aún tienes una PS4, toca dar el salto o esperar.",
    ["¿GTA 6 en PS4? Mito o verdad", "GTA 6 en PS4 y Xbox One: la respuesta", "¿Puedo jugar GTA 6 en PS4?", "GTA 6: ¿sale en consolas antiguas?", "PS4 y GTA 6: mito"],
    "¿Sale GTA 6 en PS4 o Xbox One? No: Rockstar solo lo ha anunciado para PS5 y Xbox Series X|S.",
    ["GTA 6 PS4", "GTA 6 Xbox One", "mito o verdad"])

V22 = mk("V22", "Hora_Latinoamerica", "LANZAMIENTO", "¿A qué hora sale GTA 6 en Latinoamérica?",
    ["¿A qué hora sale GTA 6 en Latinoamérica?", "GTA 6: hora en México, Argentina, Colombia y Chile", "Hora de GTA 6 en tu país", "GTA 6 en Latinoamérica: cuándo juegas", "¿Medianoche en tu país? GTA 6"],
    [S("GRAFICO", "¿Juegas desde Latinoamérica? Esta es la hora de GTA 6 en tu país.", rotulo="¿Y EN TU PAÍS?", sfx="Golpe"),
     S("GRAFICO", "Según el soporte de Rockstar, GTA 6 se desbloquea a medianoche, hora local, del jueves 19 de noviembre en cada región.", rotulo="00:00 HORA LOCAL", items=["Jueves 19 de noviembre"]),
     S("GRAFICO", "Es decir: en México, en Argentina, en Colombia o en Chile, a las doce de la noche del miércoles al jueves de cada país.", rotulo="MEDIANOCHE EN TU PAÍS", items=["México", "Argentina", "Colombia", "Chile"]),
     S("GRAFICO", "Ojo: algunas tiendas usan una única hora de referencia para varios países. Para salir de dudas, mira la cuenta atrás en la ficha del juego de tu tienda.", rotulo="MIRA TU TIENDA", items=["Cuenta atrás en la ficha"]),
     S("GRAFICO", "Dime desde qué país juegas y te leo en comentarios.", rotulo="¿DESDE DÓNDE JUEGAS?", sfx="Sting")],
    dict(texto=["¿A QUÉ", "HORA?"], sub="LATINOAMÉRICA", estilo="reloj", concepto="Reloj."),
    "GTA 6 se desbloquea a medianoche, hora local, del jueves 19/11/2026 en cada región (según el soporte de Rockstar). En Latinoamérica: a las 00:00 del miércoles al jueves de cada país. Algunas tiendas usan una hora de referencia común: comprueba la cuenta atrás en tu tienda.",
    ["GTA 6 hora México", "GTA 6 hora Argentina", "GTA 6 Latinoamérica", "GTA 6 hora Colombia", "GTA 6 hora Chile"],
    "📌 ¿Desde qué país juegas? 🌎", publico="Jugadores de Latinoamérica (gran audiencia hispanohablante).",
    objetivo="Ampliar audiencia a Latinoamérica justo antes del lanzamiento.")

V23 = mito("V23", "Mito_USB", 2, "SE JUEGA DESDE UN USB",
    "Puedes jugar a GTA 6 desde un disco duro USB.", "MITO",
    "En un USB puedes guardarlo, pero los juegos de nueva generación solo se juegan desde el almacenamiento interno, un SSD M.2 en PS5 o la tarjeta de expansión oficial en Xbox.",
    ["USB: solo guardar", "Interno o M.2: jugar"], "Si vas justo de espacio, muévelo al USB y pásalo al interno para jugar.",
    ["¿Se puede jugar GTA 6 desde un USB?", "GTA 6 en disco externo: mito", "Disco duro externo y GTA 6", "GTA 6: USB sí o no", "Ojo con el disco externo y GTA 6"],
    "En PS5 y Xbox Series, los juegos de nueva generación como GTA 6 pueden guardarse en un USB, pero solo se juegan desde el almacenamiento interno, un SSD M.2 (PS5) o la tarjeta de expansión oficial (Xbox).",
    ["GTA 6 disco externo", "GTA 6 USB", "GTA 6 almacenamiento"])

V24 = mk("V24", "No_Me_Deja_Jugar", "LANZAMIENTO", "Si a las 00:00 GTA 6 no te deja jugar",
    ["Si GTA 6 no te deja jugar a las 00:00, haz esto", "GTA 6 no arranca a medianoche: soluciones", "GTA 6 bloqueado a las 00:00: qué hacer", "¿GTA 6 no se desbloquea? Mira esto", "Soluciones rápidas para la noche de GTA 6"],
    [S("GRAFICO", "Son las doce y GTA 6 no te deja jugar. Calma: prueba esto.", rotulo="¿NO TE DEJA JUGAR?", sfx="Golpe"),
     S("GRAFICO", "Uno: comprueba la cuenta atrás en la tienda. Puede que en tu región aún no sea la hora.", rotulo="1 · LA HORA", items=["Cuenta atrás de la tienda"]),
     S("GRAFICO", "Dos: asegúrate de estar en la cuenta con la que lo compraste y de que la descarga está completa al cien por cien.", rotulo="2 · CUENTA Y DESCARGA", items=["Cuenta correcta", "Descarga al 100 %"]),
     S("GRAFICO", "Tres: en PS5, entra en Ajustes, Usuarios y cuentas, Otros, y pulsa Restaurar licencias. Luego reinicia la consola.", rotulo="3 · PS5: LICENCIAS", items=["Usuarios y cuentas", "Otros", "Restaurar licencias"]),
     S("GRAFICO", "Y si todo está bien, puede que los servidores estén saturados. Espera unos minutos y vuelve a intentarlo.", rotulo="4 · PACIENCIA", items=["Servidores saturados"]),
     S("GRAFICO", "Guárdalo por si acaso. Nos vemos en Leonida.", rotulo="GUÁRDALO", sfx="Sting")],
    dict(texto=["¿NO TE", "DEJA?"], sub="GTA 6 · 00:00", estilo="reloj", concepto="Reloj 00:00."),
    "Si GTA 6 no te deja jugar a medianoche: comprueba la cuenta atrás de tu tienda, la cuenta con la que lo compraste y que la descarga esté completa; en PS5, Ajustes → Usuarios y cuentas → Otros → Restaurar licencias; y si todo está bien, espera unos minutos por saturación de servidores.",
    ["GTA 6 no funciona", "GTA 6 no se desbloquea", "restaurar licencias PS5", "GTA 6 error"],
    "📌 ¿Te ha funcionado? Cuéntame qué te pasaba 👇", objetivo="Responder a la búsqueda urgente de la noche del lanzamiento.")

V25 = quiz("V25", "Quiz_Primer_GTA", 1, "Solo los fans de verdad aciertan esta. Tienes tres segundos.",
    "¿AÑO DEL PRIMER GTA?", "¿En qué año salió el primer Grand Theft Auto? A, 1995. B, 1997. C, 2001.", ["1995", "1997", "2001"], 1,
    "La respuesta es la B: 1997. Era un juego con vista desde arriba, muy distinto a lo que conocemos hoy.",
    "ANTES DE 2001", "Hasta GTA 3, de 2001, la saga no dio el salto a las tres dimensiones.", ["1997: GTA", "1999: GTA 2", "2001: GTA III en 3D"],
    ["Quiz GTA: ¿en qué año salió el primer GTA?", "Solo los fans aciertan esto de GTA", "¿Sabes cuándo empezó GTA?", "Quiz de GTA #1", "¿Eres fan de GTA? Demuéstralo"],
    "Quiz GTA #1: ¿en qué año salió el primer Grand Theft Auto? Respuesta: 1997, con vista cenital. El salto al 3D llegó con GTA III en 2001.",
    ["quiz GTA", "primer GTA", "historia de GTA"])

V26 = mk("V26", "Saga_Protagonistas", SAGA, "Todos los protagonistas de GTA, del III al VI",
    ["Todos los protagonistas de GTA en 30 segundos", "De Claude a Lucia: los protagonistas de GTA", "¿Cuál es tu protagonista favorito de GTA?", "La evolución de los protagonistas de GTA", "Protagonistas de GTA: ranking"],
    [S("GRAFICO", "De Claude a Lucia. Todos los protagonistas de GTA desde que la saga pasó al 3D, en treinta segundos.", rotulo="LOS PROTAGONISTAS", sfx="Golpe"),
     S("GRAFICO", "GTA 3, en 2001: Claude, el protagonista que no dice ni una palabra. Vice City: Tommy Vercetti. San Andreas: Carl Johnson, CJ.", rotulo="2001 – 2004", items=["GTA III: Claude", "Vice City: Tommy", "San Andreas: CJ"]),
     S("GRAFICO", "GTA 4, en 2008: Niko Bellic. GTA 5, en 2013: tres a la vez, Michael, Franklin y Trevor.", rotulo="2008 – 2013", items=["GTA IV: Niko Bellic", "GTA V: Michael", "Franklin y Trevor"]),
     S("GRAFICO", "Y GTA 6: por primera vez, una pareja. Jason y Lucia.", rotulo="2026: JASON Y LUCIA"),
     S("GRAFICO", "¿Cuál es tu favorito? Te leo.", rotulo="¿TU FAVORITO?", sfx="Sting")],
    dict(texto=["DE CLAUDE", "A LUCIA"], sub="GTA", estilo="paisaje", concepto="Atardecer con pines."),
    "Los protagonistas de GTA desde el 3D: Claude (GTA III, 2001), Tommy Vercetti (Vice City), Carl 'CJ' Johnson (San Andreas), Niko Bellic (GTA IV, 2008), Michael, Franklin y Trevor (GTA V, 2013) y Jason y Lucia (GTA VI, 2026).",
    ["protagonistas GTA", "Tommy Vercetti", "CJ", "Niko Bellic", "Trevor", "Jason y Lucia"],
    "📌 ¿Tommy, CJ, Niko, Trevor… o Lucia? 👇")

V27 = mk("V27", "PS5_o_Xbox", "ESTO O AQUELLO", "¿PS5 o Xbox para GTA 6?",
    ["¿PS5 o Xbox para jugar GTA 6?", "GTA 6: ¿dónde lo compro, PS5 o Xbox?", "PS5 vs Xbox para GTA 6: lo que sabemos", "¿Qué consola para GTA 6?", "GTA 6: elige consola"],
    [S("GRAFICO", "¿PS5 o Xbox para GTA 6? Esto es lo que se sabe, sin fanatismos.", rotulo="¿PS5 O XBOX?", sfx="Golpe"),
     S("GRAFICO", "Las dos versiones salen el mismo día, el 19 de noviembre, y Rockstar no ha publicado diferencias de rendimiento entre ellas.", rotulo="MISMO DÍA", items=["Rendimiento: sin datos"]),
     S("GRAFICO", "Si tienes una Series S, recuerda: menos espacio. Revisa el disco antes de comprar.", rotulo="OJO CON LA SERIES S"),
     S("GRAFICO", "Mi consejo: elige la consola donde juegan tus amigos. En un GTA, la compañía cuenta.", rotulo="DONDE JUEGUEN TUS AMIGOS"),
     S("GRAFICO", "¿Equipo PlayStation o equipo Xbox? Comenta.", rotulo="¿TU EQUIPO?", sfx="Sting")],
    dict(texto=["¿PS5 O", "XBOX?"], sub="GTA 6", estilo="lupa", concepto="Lupa."),
    "PS5 o Xbox Series para GTA 6: ambas versiones salen el 19/11/2026 y Rockstar no ha publicado diferencias de rendimiento. En Xbox Series S, ojo con el espacio. Consejo: elige donde jueguen tus amigos.",
    ["GTA 6 PS5 o Xbox", "GTA 6 qué consola", "PS5 vs Xbox"], "📌 ¿Equipo PlayStation o Xbox? 🎮")

V28 = quiz("V28", "Quiz_Vice_City", 2, "Pregunta para veteranos de Vice City. Tres segundos.",
    "¿QUIÉN PROTAGONIZÓ VICE CITY?", "¿Quién era el protagonista de GTA Vice City, el de 2002? A, Carl Johnson. B, Niko Bellic. C, Tommy Vercetti.",
    ["Carl Johnson", "Niko Bellic", "Tommy Vercetti"], 2,
    "¡La C! Tommy Vercetti, en la Vice City de 1986.", "LOS OTROS DOS", "Carl Johnson era el de San Andreas, y Niko Bellic, el de GTA 4.", ["CJ: San Andreas", "Niko: GTA IV"],
    ["Quiz: ¿quién protagonizó GTA Vice City?", "¿Recuerdas al protagonista de Vice City?", "Quiz GTA #2: Vice City", "Solo los veteranos aciertan esto", "Vice City: ¿quién era el protagonista?"],
    "Quiz GTA #2: el protagonista de GTA Vice City (2002) era Tommy Vercetti. Carl Johnson protagonizó San Andreas y Niko Bellic, GTA IV.",
    ["Tommy Vercetti", "GTA Vice City", "quiz GTA"])

V29 = mk("V29", "Por_que_se_llama_GTA", SAGA, "¿Por qué se llama Grand Theft Auto?",
    ["¿Por qué se llama Grand Theft Auto?", "El significado de GTA", "¿Qué significa GTA?", "GTA: el nombre tiene explicación", "Grand Theft Auto, explicado"],
    [S("GRAFICO", "¿Sabes qué significa Grand Theft Auto? No es un nombre inventado.", rotulo="¿QUÉ SIGNIFICA GTA?", sfx="Golpe"),
     S("GRAFICO", "En Estados Unidos, grand theft auto es el término legal para el robo de vehículos.", rotulo="GRAND THEFT AUTO", items=["Término legal en EE. UU.", "= robo de vehículos"]),
     S("GRAFICO", "Grand theft es un robo grave, y auto, automóvil. O sea: el nombre de la saga es literalmente un delito.", rotulo="UN DELITO COMO NOMBRE", items=["Grand theft: robo grave", "Auto: automóvil"]),
     S("GRAFICO", "Por cierto, el primer juego estuvo a punto de llamarse Race'n'Chase. Menos mal que no.", rotulo="CASI SE LLAMA ASÍ", items=["Race'n'Chase"]),
     S("GRAFICO", "¿Lo sabías? Sígueme para más curiosidades de la saga.", rotulo="¿LO SABÍAS?", sfx="Sting")],
    dict(texto=["¿QUÉ", "SIGNIFICA?"], sub="GTA", estilo="lupa", concepto="Lupa."),
    "Grand Theft Auto es el término legal en EE. UU. para el robo de vehículos. Curiosidad: el primer juego tuvo como título de trabajo Race'n'Chase.",
    ["qué significa GTA", "Grand Theft Auto significado", "curiosidades GTA"], "📌 ¿Lo sabías? 👇")

V30 = quiz("V30", "Quiz_Liberty_City", 3, "Esta es de geografía. Tres segundos.",
    "¿EN QUÉ SE INSPIRA LIBERTY CITY?", "Liberty City, la ciudad de GTA 3 y GTA 4, ¿en qué ciudad real se inspira? A, Chicago. B, Nueva York. C, Boston.",
    ["Chicago", "Nueva York", "Boston"], 1,
    "¡La B! Nueva York. Por eso tiene su propia versión de la Estatua de la Libertad.", "Y LAS DEMÁS", "Vice City es Miami y Los Santos, Los Ángeles.", ["Vice City → Miami", "Los Santos → Los Ángeles"],
    ["Quiz: ¿en qué se inspira Liberty City?", "Liberty City es… ¿qué ciudad real?", "Quiz GTA #3: ciudades", "Geografía de GTA: ¿aciertas?", "¿Liberty City es Nueva York?"],
    "Quiz GTA #3: Liberty City (GTA III y GTA IV) se inspira en Nueva York. Vice City, en Miami; Los Santos, en Los Ángeles.",
    ["Liberty City", "ciudades GTA", "quiz GTA"])

V31 = mito("V31", "Mito_GTA5_1000_millones", 3, "GTA 5: 1.000 M$ EN 3 DÍAS",
    "GTA 5 ingresó mil millones de dólares en sólo tres días.", "VERDAD",
    "Según Take-Two, en 2013 GTA 5 superó los mil millones de dólares en sus tres primeros días: el producto de entretenimiento más rápido en lograrlo.",
    ["Septiembre de 2013", "3 días: 1.000 M$"], "Con estos precedentes, imagina lo que puede hacer GTA 6.",
    ["GTA 5 ganó 1.000 millones en 3 días: ¿verdad?", "El récord de GTA 5 que GTA 6 podría romper", "Mito o verdad: el récord de GTA 5", "GTA 5 y sus 1.000 millones", "¿GTA 6 batirá este récord?"],
    "Verdad: según Take-Two, GTA V superó los 1.000 millones de dólares de ingresos en sus tres primeros días (septiembre de 2013).",
    ["récord GTA 5", "GTA 5 ventas", "GTA 5 1000 millones"])

V32 = mk("V32", "De_Dundee_a_Leonida", SAGA, "De Dundee a Leonida: el estudio detrás de GTA",
    ["El estudio de GTA empezó haciendo Lemmings", "De Escocia a Leonida: la historia de GTA", "¿Dónde se hace GTA?", "Los creadores de GTA hicieron Lemmings", "El origen escocés de GTA"],
    [S("GRAFICO", "GTA, la saga más americana de los videojuegos, nació en Escocia.", rotulo="NACIÓ EN ESCOCIA", sfx="Golpe"),
     S("GRAFICO", "La creó DMA Design, un estudio de Dundee que antes ya había triunfado con un juego muy distinto: Lemmings.", rotulo="DMA DESIGN · DUNDEE", items=["Antes: Lemmings (1991)", "Después: GTA (1997)"]),
     S("GRAFICO", "Con los años, el estudio pasó a formar parte de Rockstar y hoy se llama Rockstar North, con sede en Edimburgo.", rotulo="HOY: ROCKSTAR NORTH", items=["Sede en Edimburgo"]),
     S("GRAFICO", "De los Lemmings a Leonida. No está mal.", rotulo="DE LEMMINGS A LEONIDA"),
     S("GRAFICO", "¿Jugaste a Lemmings? Comenta.", rotulo="¿JUGASTE A LEMMINGS?", sfx="Sting")],
    dict(texto=["NACIÓ EN", "ESCOCIA"], sub="GTA", estilo="paisaje", concepto="Atardecer."),
    "GTA nació en Dundee (Escocia) en DMA Design, el estudio de Lemmings (1991). Hoy es Rockstar North, con sede en Edimburgo.",
    ["Rockstar North", "DMA Design", "Lemmings", "historia GTA"], "📌 ¿Jugaste a Lemmings? 🐹")

V33 = quiz("V33", "Quiz_Lemmings", 4, "Pregunta trampa. Tres segundos.",
    "¿QUÉ HIZO ANTES EL ESTUDIO DE GTA?", "Antes de GTA, el estudio que lo creó triunfó con otro juego. ¿Cuál? A, Lemmings. B, Tetris. C, Pac-Man.",
    ["Lemmings", "Tetris", "Pac-Man"], 0,
    "¡La A! Lemmings, de 1991, creado por DMA Design, el estudio escocés que luego haría GTA.", "TETRIS Y PAC-MAN", "Tetris nació en la Unión Soviética y Pac-Man, en Japón. Nada que ver.", ["Tetris: URSS", "Pac-Man: Japón"],
    ["Quiz: ¿qué juego hicieron antes los creadores de GTA?", "Los creadores de GTA hicieron… ¿esto?", "Quiz GTA #4: pregunta trampa", "¿Sabías esto de los creadores de GTA?", "Lemmings y GTA: ¿aciertas?"],
    "Quiz GTA #4: antes de GTA, DMA Design (hoy Rockstar North) triunfó con Lemmings (1991).",
    ["Lemmings", "DMA Design", "quiz GTA"])

V34 = mk("V34", "Saga_Ciudades", SAGA, "Las 3 grandes ciudades de GTA y su versión real",
    ["Las ciudades de GTA y su versión real", "Liberty City, Vice City y Los Santos: ¿qué ciudades son?", "GTA y sus ciudades reales", "Las ciudades de GTA, explicadas", "¿Qué ciudad real es cada ciudad de GTA?"],
    [S("GRAFICO", "Cada gran ciudad de GTA es una ciudad real disfrazada. Estas son las tres de siempre.", rotulo="CIUDADES DISFRAZADAS", sfx="Golpe"),
     S("GRAFICO", "Liberty City es Nueva York: GTA 3 y GTA 4.", rotulo="LIBERTY CITY", items=["= Nueva York", "GTA III · GTA IV"]),
     S("GRAFICO", "Vice City es Miami: la de 2002 y, ahora, la de GTA 6.", rotulo="VICE CITY", items=["= Miami", "Vice City · GTA VI"]),
     S("GRAFICO", "Y Los Santos es Los Ángeles: San Andreas y GTA 5. En San Andreas, además, estaban San Fierro, que es San Francisco, y Las Venturas, que es Las Vegas.", rotulo="LOS SANTOS", items=["= Los Ángeles", "+ San Fierro", "+ Las Venturas"]),
     S("GRAFICO", "¿Cuál es tu ciudad favorita de la saga?", rotulo="¿TU CIUDAD?", sfx="Sting")],
    dict(texto=["CIUDADES", "REALES"], sub="GTA", estilo="mapa", concepto="Esquema."),
    "Las ciudades de GTA y su inspiración real: Liberty City (Nueva York), Vice City (Miami) y Los Santos (Los Ángeles); en San Andreas también San Fierro (San Francisco) y Las Venturas (Las Vegas).",
    ["ciudades GTA", "Liberty City", "Vice City", "Los Santos"], "📌 ¿Liberty, Vice o Los Santos? 🏙️")

V35 = mito("V35", "Mito_Race_n_Chase", 4, "GTA IBA A LLAMARSE «RACE'N'CHASE»",
    "El primer GTA iba a llamarse Race'n'Chase.", "VERDAD",
    "Ese era el título de trabajo del proyecto en DMA Design, antes de convertirse en Grand Theft Auto.",
    ["Título de trabajo", "Antes de 1997"], "Imagina decir: ¿has jugado al nuevo Race'n'Chase seis?",
    ["GTA iba a llamarse Race'n'Chase: ¿verdad?", "El nombre original de GTA", "Mito o verdad: el primer nombre de GTA", "GTA casi se llama así", "Race'n'Chase: el GTA que no fue"],
    "Verdad: Race'n'Chase fue el título de trabajo del proyecto que acabó siendo Grand Theft Auto (1997).",
    ["Race n Chase", "nombre original GTA", "curiosidades GTA"])

V36 = mk("V36", "Ciudad_o_Naturaleza", "ESTO O AQUELLO", "¿Ciudad o naturaleza? Elige tu Leonida",
    ["¿Ciudad o naturaleza? Elige tu zona de GTA 6", "GTA 6: ¿Vice City o Mount Kalaga?", "¿Qué tipo de jugador de GTA 6 eres?", "Elige tu Leonida", "GTA 6: ¿ciudad o campo?"],
    [S("GRAFICO", "En GTA 6 hay dos tipos de jugadores. ¿Cuál eres tú?", rotulo="¿CUÁL ERES?", sfx="Golpe"),
     S("GRAFICO", "Equipo ciudad: Vice City, neón, coches de lujo, playas y fiesta hasta el amanecer.", rotulo="EQUIPO CIUDAD", items=["Vice City", "Neón y playas"]),
     S("GRAFICO", "Equipo naturaleza: los pantanos de Grassrivers, el parque nacional de Mount Kalaga y los Cayos.", rotulo="EQUIPO NATURALEZA", items=["Grassrivers", "Mount Kalaga", "Cayos de Leonida"]),
     S("GRAFICO", "Escribe ciudad o naturaleza en comentarios. Veamos qué equipo gana.", rotulo="¿CIUDAD O NATURALEZA?", sfx="Sting")],
    dict(texto=["¿CIUDAD O", "NATURALEZA?"], sub="GTA 6", estilo="paisaje", concepto="Atardecer."),
    "Encuesta Mapa Abierto: ¿equipo ciudad (Vice City) o equipo naturaleza (Grassrivers, Mount Kalaga, Cayos de Leonida)?",
    ["Leonida", "Vice City", "Mount Kalaga", "Grassrivers"], "📌 Escribe CIUDAD o NATURALEZA 👇")

V37 = mk("V37", "GTA5_en_cifras", SAGA, "GTA 5 en cifras: el listón que tiene que superar GTA 6",
    ["GTA 5 en cifras: el listón de GTA 6", "Los números de GTA 5 son una locura", "GTA 5 en 3 datos", "¿Podrá GTA 6 superar esto?", "Las cifras de GTA 5"],
    [S("GRAFICO", "Este es el listón que tiene que superar GTA 6.", rotulo="EL LISTÓN", sfx="Golpe"),
     S("GRAFICO", "GTA 5 salió en septiembre de 2013 y en tres días ya había superado los mil millones de dólares.", rotulo="1.000 M$ EN 3 DÍAS"),
     S("GRAFICO", "Desde entonces ha vendido más de doscientos millones de copias, según Take-Two, y ha salido en tres generaciones de consolas.", rotulo="+200 MILLONES DE COPIAS", items=["Según Take-Two", "3 generaciones"]),
     S("GRAFICO", "Y su modo online, GTA Online, se lanzó en octubre de 2013 y sigue activo.", rotulo="GTA ONLINE · 2013", items=["Sigue activo"]),
     S("GRAFICO", "¿Crees que GTA 6 lo superará? Apuesta en comentarios.", rotulo="¿LO SUPERARÁ?", sfx="Sting")],
    dict(texto=["EL", "LISTÓN"], sub="GTA 5 EN CIFRAS", estilo="checklist", concepto="Checklist."),
    "GTA V en cifras: más de 1.000 millones de dólares en tres días (2013), más de 200 millones de copias vendidas según Take-Two y tres generaciones de consolas. GTA Online se lanzó en octubre de 2013.",
    ["GTA 5 ventas", "GTA 5 récords", "GTA Online"], "📌 ¿GTA 6 superará a GTA 5? Sí / No 👇")

V38 = quiz("V38", "Quiz_Protagonistas_GTA5", 5, "Fácil para unos, imposible para otros. Tres segundos.",
    "¿CUÁNTOS PROTAGONISTAS EN GTA 5?", "¿Cuántos protagonistas jugables tenía la historia de GTA 5? A, dos. B, tres. C, cuatro.",
    ["Dos", "Tres", "Cuatro"], 1,
    "¡La B! Tres: Michael, Franklin y Trevor, y podías cambiar entre ellos en cualquier momento.", "¿Y EN GTA 6?", "GTA 6 tendrá dos: Jason y Lucia.", ["GTA V: 3", "GTA VI: 2"],
    ["Quiz: ¿cuántos protagonistas tenía GTA 5?", "GTA 5 tenía… ¿cuántos protagonistas?", "Quiz GTA #5", "¿Aciertas esta de GTA 5?", "Michael, Franklin y… quiz GTA"],
    "Quiz GTA #5: GTA V tenía tres protagonistas jugables (Michael, Franklin y Trevor). GTA VI tendrá dos: Jason y Lucia.",
    ["protagonistas GTA 5", "Michael Franklin Trevor", "quiz GTA"])

V39 = mito("V39", "Mito_Vista_Cenital", 5, "EL PRIMER GTA SE VEÍA DESDE ARRIBA",
    "El primer GTA se jugaba con la cámara desde arriba.", "VERDAD",
    "GTA, de 1997, y GTA 2, de 1999, tenían vista cenital, desde arriba. La cámara en tercera persona llegó con GTA 3 en 2001.",
    ["1997 y 1999: cenital", "2001: tercera persona"], "Casi treinta años después, mira dónde estamos.",
    ["El primer GTA se veía desde arriba: ¿verdad?", "Así era el primer GTA", "Mito o verdad: el GTA de 1997", "GTA antes del 3D", "El GTA que nadie recuerda"],
    "Verdad: GTA (1997) y GTA 2 (1999) tenían vista cenital; la tercera persona llegó con GTA III (2001).",
    ["primer GTA", "GTA 1997", "GTA 2", "historia GTA"])

V40 = mk("V40", "Trailer_Record", SAGA, "El tráiler que rompió YouTube",
    ["El tráiler de GTA 6 que rompió YouTube", "El récord del primer tráiler de GTA 6", "90 millones en 24 horas: GTA 6", "Así batió récords el tráiler de GTA 6", "El vídeo más visto de un juego en 24 h"],
    [S("GRAFICO", "El primer tráiler de GTA 6 hizo algo que ningún vídeo de videojuegos había hecho.", rotulo="UN RÉCORD", sfx="Golpe"),
     S("GRAFICO", "Según los datos publicados entonces, superó los noventa millones de visualizaciones en sus primeras veinticuatro horas.", rotulo="+90 MILLONES EN 24 H", items=["Diciembre de 2023"]),
     S("GRAFICO", "Y eso que se publicó con prisas, antes de tiempo, porque se había filtrado la noche anterior.", rotulo="Y CON PRISAS", items=["Salió antes de tiempo"]),
     S("GRAFICO", "¿Tú lo viste en directo aquel día? Comenta.", rotulo="¿LO VISTE ESE DÍA?", sfx="Sting")],
    dict(texto=["UN", "RÉCORD"], sub="TRÁILER GTA 6", estilo="reloj", concepto="Reloj."),
    "El primer tráiler de GTA 6 (diciembre de 2023) superó los 90 millones de visualizaciones en 24 horas según los datos publicados entonces, pese a publicarse antes de tiempo por una filtración.",
    ["tráiler GTA 6", "récord YouTube", "GTA 6 trailer 1"], "📌 ¿Lo viste en directo? 👀")

SHORTS3 = [V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V31, V32, V33, V34, V35, V36, V37, V38, V39, V40]

# Calendario (hora peninsular). YouTube: huecos sin chocar con la tanda anterior; TikTok: desfasado.
# Lógica: picos de audiencia en España 13:00-15:30 y 19:00-23:30; Latinoamérica por la mañana-tarde española;
# más densidad el día del lanzamiento y el fin de semana; formatos interactivos (quiz) en horas de ocio.
SCHED3 = [
    ("V21", "2026-11-18", "13:15", "2026-11-18", "13:50"),
    ("V22", "2026-11-18", "15:30", "2026-11-18", "16:10"),
    ("V23", "2026-11-18", "19:30", "2026-11-18", "20:10"),
    ("V24", "2026-11-18", "23:15", "2026-11-18", "23:40"),
    ("V25", "2026-11-19", "09:30", "2026-11-19", "10:15"),
    ("V26", "2026-11-19", "14:30", "2026-11-19", "15:15"),
    ("V27", "2026-11-19", "16:30", "2026-11-19", "17:15"),
    ("V28", "2026-11-19", "21:30", "2026-11-19", "22:15"),
    ("V29", "2026-11-20", "10:30", "2026-11-20", "11:15"),
    ("V30", "2026-11-20", "15:30", "2026-11-20", "16:15"),
    ("V31", "2026-11-20", "20:30", "2026-11-20", "21:15"),
    ("V32", "2026-11-20", "22:30", "2026-11-20", "23:15"),
    ("V33", "2026-11-21", "11:00", "2026-11-21", "11:45"),
    ("V34", "2026-11-21", "16:30", "2026-11-21", "17:15"),
    ("V35", "2026-11-21", "21:00", "2026-11-21", "21:45"),
    ("V36", "2026-11-22", "11:00", "2026-11-22", "11:45"),
    ("V37", "2026-11-22", "14:30", "2026-11-22", "15:15"),
    ("V38", "2026-11-22", "18:30", "2026-11-22", "19:15"),
    ("V39", "2026-11-22", "21:30", "2026-11-22", "22:15"),
    ("V40", "2026-11-23", "13:30", "2026-11-23", "14:15"),
]

_DOW = {"2026-11-18": "Miércoles 18/11", "2026-11-19": "Jueves 19/11", "2026-11-20": "Viernes 20/11", "2026-11-21": "Sábado 21/11",
        "2026-11-22": "Domingo 22/11", "2026-11-23": "Lunes 23/11"}
for _v in SHORTS3:
    _r = next(r for r in SCHED3 if r[0] == _v["id"])
    _v["seo"]["fecha"] = f"YouTube: {_DOW[_r[1]]} · {_r[2]} · TikTok: {_DOW[_r[3]]} · {_r[4]}"
