"""V86 · Primer vídeo largo con juego real: análisis del Extended Look oficial (16:9).
Todo lo narrado se ha comprobado mirando los planos del vídeo oficial (rk_dl / relay) o está confirmado por varias
fuentes (fecha de estreno, seis estrellas). Las deducciones se presentan como tales."""
from content.common import S

EL = "EL"


def E(*ts, vel=1.0):
    return [(EL, t, vel, 0.5) for t in ts]


def M(texto, clips, rotulo="", cap=None, items=None):
    return dict(S("GRAFICO", texto, rotulo=rotulo, cap=cap, items=items or [], visual="Montaje de planos del Extended Look oficial."), clips=clips, zoom=0.04)


def F(rel, texto, rotulo="", cap=None):
    return dict(S("GRAFICO", texto, rotulo=rotulo, cap=cap, visual="Detalle ampliado de un fotograma del Extended Look oficial."), foto="x_EL_stills/" + rel)


def G(texto, rotulo, items=None, cap=None):
    return S("GRAFICO", texto, rotulo=rotulo, cap=cap, items=items or [], visual="Gráfico de marca.")


ESCENAS = [
    M("Casi veintisiete minutos de juego real. Eso es lo que enseñó Rockstar en el *Extended Look* de GTA 6, y lo he revisado plano a plano.",
      E(862, 1138, 1066, 550), cap="Introducción"),
    M("Misiones, policía, armas, coches, actividades… y muchos detalles que se pasan por alto a la primera. Aquí tienes todo lo que se ve, explicado en español.",
      E(1222, 1030, 706, 1294)),
    M("Bienvenido a Mapa Abierto. Una norma de la casa: solo te cuento lo que se ve en el vídeo oficial o lo que han confirmado varias fuentes. Si algo es una opinión mía, te lo diré.",
      E(994, 1546, 1566)),

    M("Primero, el contexto. Rockstar estrenó el Extended Look el *27 de agosto de 2026*: primero en Netflix y, esa misma noche, en su canal de YouTube y en la web de GTA 6.",
      E(466, 490, 754), rotulo="¿QUÉ ES EL EXTENDED LOOK?", cap="Qué es el Extended Look"),
    M("La diferencia con los tráileres es clave: aquí el juego se ve *con la interfaz en pantalla*. Minimapa, munición, estrellas de búsqueda, cronómetros… Es decir, se ve cómo se juega, no solo cinemáticas.",
      E(514, 1066, 862, 1114)),

    M("El vídeo arranca de noche. *Jason y Lucia* llegan juntos a un edificio de apartamentos destartalado, con gente en la puerta y en los pasillos.",
      E(10, 22, 58, 82), rotulo="LA MISIÓN DE APERTURA", cap="La misión de apertura"),
    M("Suben hasta una habitación donde les espera un tipo con rastas y cadenas de oro, rodeado de gente que trabaja alrededor de una mesa.",
      E(94, 166, 178, 190)),
    M("La cosa se tuerce y acaba en un *tiroteo por los pasillos*. Fíjate en la interfaz: la munición aparece arriba a la derecha, y en el centro solo hay una retícula pequeña, muy discreta.",
      E(262, 274, 286, 334)),
    M("La huida no es por la puerta principal: en un momento se ve a Lucia trepando para escapar. Jason y Lucia, los dos protagonistas, comparten la acción desde la primera escena.",
      E(298, 346, 357)),

    M("Después cambia el ritmo. Lucia sale a correr por la ciudad, un coche clásico derrapa en una carretera y vemos a los protagonistas en casa: ropa, espejos, cocina y la tele encendida.",
      E(370, 382, 394, 418, 442), rotulo="LA VIDA DIARIA", cap="La vida diaria en Leonida"),
    M("En la tele, como siempre en GTA, hay programas inventados. Y vuelven los anuncios de parodia: aquí, una hamburguesa absurda con capas y capas de embutido, la *Prairie Sandwich*.",
      E(454, 478)),
    M("También hay naturaleza: un bosque con *animales salvajes*, como ciervos, pastando tranquilamente. Leonida no es solo ciudad.",
      E(466, 469, vel=1.5)),

    M("Jason coge un *descapotable rojo* y cruza Vice City de día: avenidas con palmeras, tráfico, rascacielos y un puente sobre el agua.",
      E(502, 514, 526, 538), rotulo="CONDUCIR POR VICE CITY", cap="Conducir por Vice City"),
    M("El minimapa sigue abajo a la izquierda, como en GTA 5. Y más tarde, al atardecer, hay otro trayecto por la autopista con el sol de frente que es de lo más bonito del vídeo.",
      E(520, 754, 766, 778)),

    M("En una terraza con vistas al centro, Jason se reúne con un hombre mayor con camisa hawaiana. En GTA, este tipo de escenas suele servir para presentar un encargo.",
      E(586, 598, 646, 670), rotulo="UN ENCUENTRO EN LA AZOTEA", cap="Un encuentro en la azotea"),
    M("La conversación sigue en el borde de la azotea, con Vice City de fondo. El vídeo no explica de qué trata exactamente, así que no me voy a inventar el resto.",
      E(682, 742, 610)),

    M("Y entonces llega el clásico: *un atraco a una tienda de barrio*, con los atracadores tapados con pañuelos.",
      E(708, 710, 718, 730), rotulo="EL ATRACO", cap="El atraco y las seis estrellas"),
    F("zoom_cerveza.jpg", "Primer detalle que se pasa por alto: los carteles de la tienda. 'Cerveza fría', 'bebidas'… Leonida tiene rótulos en español, igual que la Florida real.",
      rotulo="RÓTULOS EN ESPAÑOL"),
    F("zoom_estrellas.jpg", "Segundo detalle, y este es importante: arriba a la derecha hay *seis estrellas* de búsqueda. GTA 5 tenía cinco; GTA 6 recupera el máximo de seis.",
      rotulo="6 ESTRELLAS"),
    F("tienda_estrellas.jpg", "Debajo aparecen unos iconos: una cámara de vigilancia, dos caras, una percha, una silueta y una pistola. Por los dibujos, todo apunta a que muestran lo que la policía sabe de ti: cámaras, testigos, tu ropa, tu aspecto o tu arma. Varios análisis lo interpretan igual."),
    M("Después viene la persecución: un coche patrulla volcado en plena calle, disparos con rifle, un helicóptero encima y la huida en coche.",
      E(850, 862, 946, 898)),
    M("Y un detalle muy GTA: en un aparcamiento, una de las atracadoras prende fuego al coche que han usado. Cambiar de vehículo y borrar el rastro parece parte del juego.",
      E(952, 961, 964, 970)),

    F("menu_armas.jpg", "Justo antes, durante un segundo, se ve el *nuevo menú de armas*. Tiene dos pestañas, *armas* y *objetos*, y en el centro pone 'desarmado'.",
      rotulo="EL MENÚ DE ARMAS", cap="El nuevo menú de armas"),
    F("menu_armas.jpg", "Abajo a la izquierda hay consumibles con un contador, arriba a la izquierda tres barras de estado y arriba a la derecha dos cantidades de dinero distintas. Rockstar no explica qué significa cada una, así que lo dejamos ahí."),
    M("Por cierto, si te está sirviendo este repaso, suscríbete a Mapa Abierto: cada día subo novedades de GTA 6, contadas sin humo.",
      E(1546, 994), rotulo="SUSCRÍBETE"),

    M("Ahora, las actividades. Hay paseos en *hidrodeslizador* por los pantanos, motos de agua y gimnasio con banco de pesas.",
      [(EL, 1030, 2.5, 0.5), (EL, 1045, 2.5, 0.5), (EL, 1042, 1.0, 0.5)], rotulo="QUÉ MÁS SE PUEDE HACER", cap="Actividades"),
    M("Hay *carreras en circuito*, con vueltas y cronómetro, y *carreras callejeras de noche* con coches tuneados y luces de neón.",
      [(EL, 1066, 1.0, 0.5), (EL, 1222, 1.4, 0.5), (EL, 1226, 1.4, 0.5)]),
    F("zoom_dianas.jpg", "Y una *prueba de tiro* contra dianas, con un contador de objetivos y un tiempo de referencia que batir."),
    M("También se ve una zona de tiendas, motos por la ciudad, alguien haciéndose un selfi con el móvil, una explosión de noche y un *salto en paracaídas* sobre Vice City.",
      E(1078, 1090, 1102, 1126, 1138)),

    M("Luego llega la parte más elegante del vídeo: una reunión con ropa de gala en un edificio de lujo junto al agua, que termina de noche en un muelle.",
      E(1150, 1162, 1186, 1198), rotulo="LUJO Y VIDA NOCTURNA", cap="Lujo y vida nocturna"),
    M("Y de ahí, a un *club nocturno*: luces de neón, cola en la puerta, globos de colores y una anfitriona que les recibe dentro.",
      E(1234, 1246, 1258, 1282)),

    M("El bloque final es el más intenso: una *infiltración de noche en un rascacielos*. Ascensor, oficinas a oscuras y gente trabajando tras los cristales.",
      E(1294, 1306, 1342, 1390), rotulo="EL GOLPE FINAL", cap="El golpe del rascacielos"),
    F("zoom_mensaje.jpg", "En plena tensión aparece en pantalla un *mensaje de Lucia*. Se lee a medias: habla de tipos con armas automáticas y explosivos, y dice que suenan a militares."),
    M("Llegan los guardias armados, se ve la *planta veintiséis* y estalla el tiroteo entre oficinas. El vídeo se despide con la ciudad iluminada de noche.",
      E(1438, 1450, 1474, 1522, 1546)),

    G("Ojo con lo que *no* aparece. El vídeo no da el tamaño del mapa ni cuántas horas dura la historia. Si ves cifras como 'el doble que GTA 5' u '80 horas', no salen del Extended Look.",
      "LO QUE NO ENSEÑA", items=["Tamaño del mapa: no lo dice", "Horas de historia: no lo dice"], cap="Lo que no enseña"),
    G("Y tampoco explica cada mecánica: lo de los iconos de la policía o las dos cantidades de dinero son deducciones a partir de lo que se ve. Ahora que el juego ya está a la venta, iremos comprobando cada detalle aquí.",
      "DEDUCCIONES, NO DATOS", items=["Iconos de la policía", "Las dos cantidades de dinero"]),

    M("Mi opinión: lo que más me ha llamado la atención es lo vivo que se siente todo. Rótulos en español, anuncios absurdos, animales, carreras, atracos… Es un GTA con muchísimas cosas que hacer entre misión y misión.",
      E(1558, 994, 382, 1066), rotulo="MI CONCLUSIÓN", cap="Conclusión"),
    G("Y a ti, ¿qué es lo que más te ha llamado la atención? Te leo en comentarios. Si quieres seguir explorando, aquí tienes más vídeos. Nos vemos en Leonida.",
      "SIGUE EXPLORANDO"),
]

DESC = """Análisis en español del Extended Look de GTA 6: casi 27 minutos de juego real que Rockstar estrenó el 27 de agosto de 2026. Lo he revisado plano a plano: la misión de apertura con Jason y Lucia, la vida diaria en Leonida, conducir por Vice City, el atraco con las seis estrellas de búsqueda, el nuevo menú de armas, las actividades (hidrodeslizador, carreras, prueba de tiro, paracaídas…), la vida nocturna y el golpe del rascacielos.

Aquí solo cuento lo que se ve en el vídeo oficial o lo que confirman varias fuentes. Las deducciones (como el significado de los iconos de la policía) se indican como tales.

{CAPITULOS}

Imágenes y vídeo: © Rockstar Games (material oficial de su web de descargas, incluido el Extended Look), con fines informativos y de análisis. La voz está generada con IA. Mapa Abierto es un canal no oficial.

#GTA6 #GTAVI #ExtendedLook"""

V86 = dict(
    id="V86", carpeta="VIDEO_86_Largo_Extended_Look_Analisis", formato="largo", modo="final", oficial=True,
    tema="GTA 6 Extended Look: todo lo que se ve del juego real",
    concepto=dict(
        tematica="Análisis plano a plano del Extended Look oficial (27/08/2026) con el propio material de Rockstar.",
        publico="Jugadores de GTA 6 en España y Latinoamérica que quieren saber qué enseña el juego y qué detalles se les escaparon.",
        intencion="'gta 6 extended look' (≈86.000 búsquedas/mes en ES según vidIQ), 'extended look gta 6', 'gta 6 gameplay español', 'curiosidades gta 6'.",
        clic="Promesa concreta (todo lo que se ve) + detalles verificados en pantalla (seis estrellas, rótulos en español, menú de armas).",
        duracion="7-9 minutos",
        objetivo="Primer vídeo largo con juego real: horas de visualización para el Programa de Socios y destino de los Shorts.",
    ),
    titulos=[
        "GTA 6 Extended Look: todo lo que se ve del juego real (análisis en español)",
        "Revisé el Extended Look de GTA 6 plano a plano: esto es lo que enseña",
        "GTA 6: 27 minutos de juego real explicados",
        "Los detalles del Extended Look de GTA 6 que se te pasaron",
        "GTA 6 gameplay: análisis completo del Extended Look",
    ],
    elegido=0,
    justificacion="La palabra clave más buscada ('GTA 6 Extended Look') al principio, promesa clara y 'en español' para la búsqueda local.",
    escenas=ESCENAS,
    miniaturas=[
        dict(texto=["27 MINUTOS", "DE JUEGO REAL"], sub="GTA 6", estilo="oficial", concepto="Fotograma del tiroteo junto al coche patrulla volcado + texto."),
        dict(texto=["6 ESTRELLAS", "Y MÁS"], sub="GTA 6", estilo="oficial", concepto="Ampliación de las seis estrellas con los iconos de la policía."),
        dict(texto=["TODO LO QUE", "SE VE"], sub="EXTENDED LOOK", estilo="oficial", concepto="Salto en paracaídas sobre Vice City."),
    ],
    mini_elegida=0, mini_motivo="Acción + número concreto; el texto promete exactamente el contenido.",
    seo=dict(descripcion=DESC, keywords=["gta 6 extended look", "gta 6 gameplay español"],
             tags=["GTA 6", "GTA VI", "GTA 6 Extended Look", "Extended Look GTA 6", "GTA 6 gameplay", "GTA 6 gameplay español",
                   "GTA 6 análisis", "curiosidades GTA 6", "GTA 6 detalles", "Jason y Lucia", "Vice City", "Leonida", "Mapa Abierto"],
             hashtags=["#GTA6", "#GTAVI", "#ExtendedLook"],
             comentario="📌 ¿Qué detalle se te había pasado? Yo no me había fijado en los rótulos en español hasta revisarlo plano a plano 👀",
             categoria="Videojuegos (Gaming)", playlist="GTA 6 · Análisis", fecha="Sábado 21/11/2026 · 12:00"),
)

SHORTS = [V86]
