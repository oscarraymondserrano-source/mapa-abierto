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
