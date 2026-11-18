"""Versiones FINALES sin gameplay ni material oficial: cada escena se resuelve con gráficos animados propios.
Clave = rótulo de la escena. Valores: items (aparecen uno a uno), chip (etiqueta bajo el rótulo), esquema (región a resaltar)."""

FINAL_IDS = ["V01", "V02", "V03", "V04", "V05", "V06", "V07"] + [f"V{i}" for i in range(11, 41)]

OV = {
    "V01": {
        "GTA 6 · JUEVES 19": dict(items=["Jueves 19 de noviembre", "PS5 · Xbox Series X|S"]),
        "19 NOV 2026 · PS5 · XBOX SERIES": dict(items=["Anunciado en Rockstar Newswire", "Fecha anterior: 26 de mayo de 2026", "PC: sin anunciar"]),
        "MEDIANOCHE EN TU PAÍS": dict(items=["España: 00:00 del jueves", "EE. UU.: la tienda usa la hora del este"]),
        "PRECARGA: ABIERTA DESDE EL 10 NOV": dict(items=["Solo versión digital", "Desde el 10/11 (según medios)", "No permite jugar antes"]),
        "SERIES S: HAZ HUECO HOY": dict(items=["Espacio útil reducido", "Borra juegos antes del miércoles"]),
        "JASON & LUCIA · LEONIDA": dict(items=["Leonida ≈ Florida", "Vice City ≈ Miami", "Jason Duval y Lucia Caminos"]),
        "LUCIA CAMINOS": dict(items=["Aprendió a pelear de niña", "Penitenciaría de Leonida", "Ahora: solo jugadas inteligentes"], chip="SEGÚN SU FICHA OFICIAL"),
        "JASON DUVAL": dict(items=["Creció entre timadores", "Pasó por el ejército", "Trabaja en los Cayos"], chip="SEGÚN SU FICHA OFICIAL"),
        "EL REPARTO": dict(items=["Cal Hampton · amigo de Jason", "Boobie Ike · figura de Vice City"]),
        "EMPIEZAN DESDE ABAJO": dict(items=["Coches baratos", "Cerraduras sencillas"], chip="FUENTE: THE GUARDIAN · NOV. 2026"),
        "LA RELACIÓN SE CUIDA... O SE PIERDE": dict(items=["Si la descuidas, se pierden gestos", "Recuperarlos cuesta esfuerzo"]),
        "EMPATÍA OPCIONAL · CAOS INTACTO": dict(items=["Mecánicas opcionales", "Ej.: acariciar a un perro", "El caos de siempre sigue ahí"]),
        "OFICIAL ≠ RUMOR": dict(items=["OFICIAL: lo dice Rockstar", "RUMOR: te lo avisamos"]),
        "SUSCRÍBETE": dict(items=["Primeras impresiones", "Guía de primeras horas", "Secretos y Easter eggs"]),
    },
    "V03": {
        "6 REGIONES": dict(items=["1 gran ciudad", "5 regiones más", "Inspiración: Florida"]),
        "LEONIDA": dict(esquema="ALL"),
        "VICE CITY": dict(esquema="VICE CITY", chip="INSPIRACIÓN: MIAMI"),
        "MIAMI · OCEAN DRIVE": dict(items=["Playas y paseo marítimo", "Puertos deportivos", "Autopistas elevadas", "Barrios residenciales"]),
        "CAYOS DE LEONIDA": dict(esquema="CAYOS DE LEONIDA", chip="INSPIRACIÓN: CAYOS DE FLORIDA"),
        "TEORÍA: CONTENIDO ACUÁTICO": dict(items=["Barcos", "Pesca", "Motos de agua"], chip="SUPOSICIÓN · SIN CONFIRMAR"),
        "GRASSRIVERS": dict(esquema="GRASSRIVERS", chip="INSPIRACIÓN: EVERGLADES"),
        "LA ZONA MÁS SALVAJE": dict(items=["Pantanos", "Hierba alta", "Caimanes"]),
        "PORT GELLHORN": dict(esquema="PORT GELLHORN", chip="LA COMUNIDAD LO SITÚA EN EL PANHANDLE"),
        "MENOS GLAMOUR, MÁS GRIETAS": dict(items=["Puerto industrial", "Moteles de carretera", "Aire decadente"]),
        "AMBROSIA": dict(esquema="AMBROSIA", chip="REFINERÍA DE AZÚCAR · ZONA RURAL"),
        "MOUNT KALAGA": dict(esquema="MOUNT KALAGA", chip="PARQUE NACIONAL"),
        "UNA CIUDAD VIVA": dict(items=["Clubes", "Gimnasios en la playa", "Fiestas"]),
        "MÁS VARIEDAD QUE NUNCA": dict(items=["Islas", "Humedales", "Costa industrial", "Campo y montaña"]),
        "TAMAÑO: SIN CIFRA OFICIAL": dict(items=["Mapas de fans = estimaciones", "Sin kilómetros oficiales"]),
        "¿TODO ABIERTO DESDE EL INICIO?": dict(items=["GTA 5: casi todo desde pronto", "GTA 6: sin confirmar"]),
        "RECORRIDO REAL MUY PRONTO": dict(items=["Capturas reales", "Esquema actualizado"]),
    },
    "V05": {
        "3 DATOS": dict(items=["Tráiler 1 · dic. 2023", "Tráiler 2 · may. 2025"]),
        "1 · SALIÓ ANTES DE TIEMPO": dict(items=["Se filtró la noche antes", "Rockstar lo publicó ya"]),
        "2 · CAPTURADO EN PS5": dict(items=["Según Rockstar", "Mitad juego", "Mitad cinemáticas"]),
        "3 · LA MÚSICA": dict(items=["T1 · Love Is a Long Road", "Tom Petty", "T2 · Hot Together", "The Pointer Sisters"]),
    },
    "V06": {
        "JASON & LUCIA": dict(items=["Pareja protagonista", "Leonida · Vice City"]),
        "LUCIA CAMINOS": dict(items=["Pelea desde niña", "Penitenciaría de Leonida"]),
        "JASON DUVAL": dict(items=["Creció entre timadores", "Ejército → los Cayos"]),
        "UNA PRIMERA VEZ": dict(items=["Primera protagonista", "desde los años 90"]),
    },
    "V07": {
        "HAZ ESTO ANTES": dict(items=["5 ajustes", "5 minutos"]),
        "1 · SUBTÍTULOS": dict(items=["Ajustes → Idioma", "Subtítulos: activados"]),
        "2 · BRILLO Y HDR": dict(items=["Pantalla de calibración", "Negros bien ajustados"]),
        "3 · MODO GRÁFICO": dict(items=["¿Calidad?", "¿Rendimiento?", "Elige antes de empezar"]),
        "4 · MANDO": dict(items=["Invertir ejes", "Vibración", "Sensibilidad"]),
        "5 · CERO SPOILERS": dict(items=["Notificaciones en silencio"]),
    },
}

PIE_FINAL = ("Vídeo realizado con gráficos propios de Mapa Abierto: no contiene imágenes del juego. "
             "GTA VI es una marca de Rockstar Games; Mapa Abierto es un canal no oficial.")

SEO_EXTRA = {
    "V01": ("Fuentes: Rockstar Newswire, soporte de Rockstar Games y medios especializados (enlaces en el comentario fijado).",
            "Fuentes:\n• Rockstar Newswire (fecha de lanzamiento): https://www.rockstargames.com/newswire/article/ak3ak31a49a221/grand-theft-auto-vi-is-now-set-to-launch-november-19-2026\n"
            "• Hora, precarga y tamaño (3DJuegos): https://www.3djuegos.com/event/lanzamiento-de-gta-6-precarga-a-que-hora-se-puede-jugar-tamano-de-la-descarga-y-todo-lo-que-necesitas-sobre-el-estreno-de-grand-theft-auto-6\n"
            "• Entrevista de The Guardian (resumen en Vice): https://www.vice.com/en/article/gta-6-gameplay-details-guardian-interview/"),
    "V07": ("Grabado en [PS5/Xbox Series X] con la versión [x.xx].", "Consejos válidos para PS5 y Xbox Series X|S."),
}

THUMB_FIX = {
    "V01": {2: "paisaje"},
    "V03": {2: "paisaje"},
    "V05": {0: "lupa"},
    "V06": {0: "lupa"},
}
