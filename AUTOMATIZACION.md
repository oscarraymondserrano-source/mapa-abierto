# Producción diaria automática · Mapa Abierto

Este repositorio contiene todo lo necesario para que una sesión de Claude Code produzca cada día una tanda nueva de Shorts listos para programar.

## Qué hace la tarea diaria
1. **Investiga** las novedades de GTA 6 del día (búsqueda web; vidIQ si está conectado). Solo usa datos verificables y marca lo no confirmado.
2. **Escribe** 6 Shorts nuevos en `_build/content/tanda_AAAAMMDD.py`, copiando el formato de `_build/content/shorts3.py` (helpers `mk`, `quiz`, `mito`). El archivo debe definir `SHORTS` (lista de vídeos), `SCHED` (filas `(id, fecha_yt, hora_yt, fecha_tt, hora_tt)`) y `TANDA` (p. ej. "Tanda 2026-11-20"). Los IDs continúan desde el mayor `VIDEO_XX` existente; la carpeta es `VIDEO_XX_Short_<Slug>`. Comprueba que los textos de los ítems caben (≤ 820 px a 66 px de Inter Bold). Usa las series del canal: QUIZ GTA, MITO O VERDAD, LA SAGA EN 30 s, ESTO O AQUELLO, y NOTICIA (solo novedades confirmadas). No repite temas ya publicados (consultar `03_CALENDARIO/`).
3. **Renderiza** con la voz de Nico (ElevenLabs): `MA_VOICE=eleven ELEVENLABS_API_KEY=proxy-injected python3 _build/build_videos.py <IDs>`. La clave real la inyecta el proxy del entorno; nunca va en el código.
4. **Comprueba** la calidad: `python3 _build/qc.py`. Opcional: transcribir una muestra para verificar la voz.
5. **Genera** el Centro de Publicación: `python3 _build/build_centro.py CENTRO_PUBLICACION_<TANDA>.html content.tanda_AAAAMMDD` y el ZIP `MAPA_ABIERTO_TANDA_AAAAMMDD.zip` con los MP4, subtítulos, SEO y portadas.
6. **Entrega** el ZIP y la página al usuario y hace commit de los guiones (no de los MP4) en este repositorio.

## Reglas editoriales (no negociables)
- Nada de gameplay inventado ni imágenes generadas presentadas como del juego.
- Cada dato debe ser oficial o estar atribuido ("según…"); lo no confirmado se dice.
- Castellano de España. Títulos sin clickbait engañoso.
- Horarios: picos de España 13:00–15:30 y 19:00–23:30; TikTok, unos 40 minutos después de YouTube; mínimo 45 minutos entre posts de la misma red.

## Requisitos del entorno
- Credencial de ElevenLabs guardada para `api.elevenlabs.io` (cabecera `xi-api-key`).
- `pip install elevenlabs` (y `sherpa-onnx` si se quiere verificar la voz).
- Fuentes Inter y JetBrains Mono (vienen en el entorno por defecto).

## Archivos que NO están en el repositorio
MP4 y WAV (se regeneran) e imágenes de escena. Las entregas finales están en los ZIP enviados al usuario.

## Publicación en Metricool (probado el 18/11/2026)
- Marca `blogId` 8199011, zona `Europe/Madrid`; redes: YouTube y TikTok.
- Vídeos alojados en el repo público `mapa-abierto-media` (`tandas/<fecha>/VXX_FINAL_1080x1920.mp4`); Metricool los copia a su servidor al programar.
- Un post por red y hora. YouTube: `youtubeData` con `type: "short"`, `privacy: "public"`, `category: "GAMING"`, `madeForKids: false`.
- **TikTok exige `tiktokData.title`** (si falta: "TikTok title is required"). Usar el título del vídeo; `isAigc: true` (voz sintética).

## Material oficial de Rockstar (desde el 19/11/2026)
- Fuente única de imágenes del juego: la web de descargas de prensa de Rockstar (capturas 4K + tráiler de lanzamiento). **Nunca** gameplay de otros creadores ni descargas de YouTube.
- Descarga: `bash _build/assets_rockstar.sh` (se guarda en `/tmp/claude-0/rk_dl`, efímero: ejecutar al inicio de cada tanda).
- En los guiones: `foto="Places/Vice City/Vice_City_01.jpg"` (+ `fx` 0–1 para el encuadre) o `clip=("GTAVI_Launch_Trailer.mp4", segundo)`. El motor recorta las bandas negras del tráiler, quita su audio (Content ID) y pone el crédito "Imagen/Vídeo: Rockstar Games".
- Momentos útiles del tráiler: 6–12 s yate, 18 s coches, 27 s pantano, 36–45 s Jason y Lucia, 48 s club, 51 s moto, 54 s playa. Evitar 24 s (logo) y 81 s en adelante (rótulos finales).
- En el guion marcar `V["oficial"] = True` y terminar la descripción con: "Imágenes y vídeo: © Rockstar Games (material oficial de su web de descargas), con fines informativos. Mapa Abierto es un canal no oficial."
- Ejemplo: `_build/content/tanda_20261119_oficial.py` (V59).

### Juego real: Extended Look (desde el 19/11/2026)
- `assets_rockstar.sh` arranca `rk_relay.py`, un relay local que deja a ffmpeg leer por rangos el Extended Look oficial (27 min, 4K, PS5) sin bajar los 14 GB.
- En los guiones: `clip=("EL", segundo, velocidad)` (+ `fx` para encuadrar el recorte vertical). Sin audio.
- Tramos útiles (segundo de inicio · duración aprox.): 506 descapotable por Vice City (28 s) · 760 carretera al atardecer (9 s) · 849 tiroteo con la policía (7 s) · 925 persecución en callejón (8 s) · 1003 Jason y Lucia en la furgoneta (6 s) · 1030 hidrodeslizador (2,5 s, usar vel 2,5) · 1045 moto de agua (2,5 s) · 1133 paracaídas sobre Vice City (6 s) · 1222 carrera nocturna (5 s) · 1571 atardecer sobre Vice City (2,5 s). Evitar 374 (logo VI) y 1585 en adelante (rótulos finales).
- Etiqueta de serie para estos vídeos: "JUEGO REAL". Ejemplos: `content/tanda_20261119_gameplay.py` (V66–V75).

## Ritmo de publicación (decidido el 19/11/2026 con datos)
- Con 10–12 Shorts al día los de un mismo día se quedaban en 0–30 visualizaciones; el quiz de las 9:30 llegó a ~500. YouTube reparte poco alcance a un canal nuevo: menos vídeos y mejores.
- **YouTube: máximo 4 al día** (10:00, 13:30, 16:00, 18:00). **TikTok: 3 al día** (10:30, 12:30, 18:30). Son las horas con más audiencia según getBestTimeToPostByNetwork; por la noche (21–23 h) hay la mitad o menos.
- Formatos prioritarios: QUIZ y MITO O VERDAD con juego real; preguntas directas ("¿A qué hora…?", "¿Sale en…?"). Los vídeos largos y los resúmenes rinden poco.
- El calendario de Metricool se redistribuyó así el 19/11 (hasta el 28/11 en YouTube y el 1/12 en TikTok). La tanda diaria solo produce si quedan franjas libres.
- Metricool: el usuario contrató el plan Starter el 19/11 (el gratuito permitía 20 publicaciones al mes).

## Novedades diarias y montaje dinámico (desde el 19/11/2026)
- `python3 _build/rk_novedades.py` lee la web de descargas de Rockstar, compara con `_build/rk_assets_vistos.txt` y descarga lo nuevo (vídeos de hasta 1,5 GB y paquetes de capturas). Si hay material nuevo, se hace un Short con él ese mismo día (prioridad sobre lo programado) y se añaden sus mejores planos a `content/rk_pool.py`.
- El relay del Extended Look debe quedar vivo durante el render: arrancarlo con la herramienta Bash en segundo plano (`python3 _build/rk_relay.py 8765`), no con nohup (se cierra al acabar el comando).
- Montaje dinámico: en los guiones usar `clips=mezcla("conducir", "noche", n=3)` (de `content.rk_pool`) para que cada escena tenga 2–3 cortes de ~1,5–2,5 s con un empuje de zoom suave. El primer plano tiene que tener movimiento (nada de pantallas negras ni logos). Rótulos cortos (que quepan en una línea o dos).
- Si no hay huecos ni novedades, rehacer Shorts antiguos de gráficos (quiz y mito de las tandas 2–3, que el usuario dejó en privado en YouTube) con juego real de fondo y subirlos como nuevos cuando haya franjas libres.

## Vídeos largos (desde el 20/11/2026)
Objetivo: horas de visualización para el Programa de Socios (4.000 h) y un canal menos "plantilla" ante la revisión manual de YouTube.
- Ritmo: 1–2 largos por semana (sábado 12:00 y/o miércoles 19:00), 7–10 min, 16:9.
- Módulo: `_build/content/tanda_AAAAMMDD_largo.py` con `formato="largo"`, `modo="final"`, `oficial=True`. Helpers: `M(texto, clips)` montaje del Extended Look, `F(still, texto)` detalle ampliado, `G(texto, rotulo, items)` gráfico. Primera escena de cada capítulo con `cap=` y `rotulo=` (los demás sin rótulo: velo suave).
- Verificación: antes de narrar, sacar hojas de contacto (`ffmpeg -ss T -frames:v 1` cada 12 s vía relay) y comprobar cada afirmación en el plano. Evitar EL 359–362 ("Rockstar Games presents"), 1575+ (créditos). El menú de armas con "UNARMED" está en 958.0–958.2.
- Fotogramas de detalle en `/tmp/claude-0/rk_dl/x_EL_stills/` (efímeros: regenerarlos con ffmpeg si faltan).
- Miniaturas: `python3 _build/thumbs_largo.py` (fotograma oficial + capa de texto). Capítulos: `python3 _build/capitulos.py <carpeta>` → pegar en la descripción (sustituye `{CAPITULOS}`).
- Alojamiento: el MP4 pesa ~300 MB → repo `mapa-abierto-media`, carpeta `largos/` con **Git LFS**; URL pública `https://media.githubusercontent.com/media/oscarraymondserrano-source/mapa-abierto-media/main/largos/<archivo>.mp4`. (Las releases de GitHub no están permitidas en esta sesión.)
- Publicación: Metricool `createScheduledPost` con `youtubeData.type="video"`, título, etiquetas, categoría GAMING, `madeForKids=false`; miniatura no se puede subir por la API → el usuario la sube en Studio (o se deja la automática).

## Serie "LA COMUNIDAD" (desde el 20/11/2026)
Shorts sobre lo que pasa con GTA 6 entre streamers y jugadores (récords, cifras, descubrimientos), para captar búsquedas como "illojuan gta 6" o "rubius gta 6".
- NUNCA imágenes, voz ni clips de los streamers (Content ID, contenido reutilizado, normas de YouTube/Twitch). Solo material oficial de Rockstar y gráficos propios; pie: "No se usan imágenes de los streamers mencionados".
- Solo datos confirmados por 2 o más medios fiables (Streams Charts, SullyGnome, medios de videojuegos). Citar las fuentes en la descripción. Descartar lo que solo publica una web (p. ej., el 20/11 se descartaron "311.000 espectadores de Rubius el día del lanzamiento", "nido de huevos en la torre" y "Bigfoot").
- Tono neutro con personas reales: cifras y hechos, sin opiniones sobre ellas ni polémicas sin confirmar.
- Ritmo: 2–3 por semana como 5.º Short del día (20:30), dentro de la prueba de subir el ritmo.
- Si un streamer da permiso por escrito para usar un clip suyo, guardar la captura del permiso en `02_INVESTIGACION/permisos/` antes de usarlo.
