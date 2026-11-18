# Producción diaria automática · Mapa Abierto

Este repositorio contiene todo lo necesario para que una sesión de Claude Code produzca cada día una tanda nueva de Shorts listos para programar.

## Qué hace la tarea diaria
1. **Investiga** las novedades de GTA 6 del día (búsqueda web; vidIQ si está conectado). Solo usa datos verificables y marca lo no confirmado.
2. **Escribe** 6 Shorts nuevos en `_build/content/tanda_AAAAMMDD.py`, siguiendo el formato de `_build/content/shorts3.py`. Usa las series del canal: QUIZ GTA, MITO O VERDAD, LA SAGA EN 30 s, ESTO O AQUELLO, y NOTICIA (solo novedades confirmadas). No repite temas ya publicados (consultar `03_CALENDARIO/`).
3. **Renderiza** con la voz de Nico (ElevenLabs): `MA_VOICE=eleven ELEVENLABS_API_KEY=proxy-injected python3 _build/build_videos.py <IDs>`. La clave real la inyecta el proxy del entorno; nunca va en el código.
4. **Comprueba** la calidad: `python3 _build/qc.py`. Opcional: transcribir una muestra para verificar la voz.
5. **Genera** el Centro de Publicación de la tanda (`_build/build_centro.py`, adaptado a la tanda del día) y el ZIP `MAPA_ABIERTO_TANDA_AAAAMMDD.zip` con los MP4, subtítulos, SEO y portadas.
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
