Tanda diaria automática de Mapa Abierto (v2.1, según ESTRATEGIA.md; largos en pausa). Hazla de principio a fin sin pedir nada al propietario, salvo lo marcado como APROBACIÓN. Sigue AUTOMATIZACION.md, ESTRATEGIA.md y TAREA_DIARIA.md del repo oscarraymondserrano-source/mapa-abierto (si /home/user/mapa-abierto no existe, vuelve a clonarlo con add_repo; igual con mapa-abierto-media; pip install -q elevenlabs).

REGLAS NO NEGOCIABLES:
- Solo material oficial de la web de descargas de Rockstar, sin su audio, y gráficos propios.
- Nunca clips, imágenes ni voz de otros creadores o streamers sin permiso por escrito; nada descargado de YouTube ni de Twitch.
- Nada de pagar por crecimiento.
- Cada dato en 2 o más fuentes fiables, citadas en la descripción; si no se puede verificar, no se publica. Las deducciones se dicen como tales; la voz solo describe lo que se ve.
- Voz IA declarada en la descripción; tono neutro con personas reales; claves de API nunca en el chat ni en el código.

RITMO:
- 4 Shorts al día en YouTube (10:00, 13:30, 16:00, 18:00, hora de Madrid), separados 2,5 h o más, TODOS los días.
- VÍDEOS LARGOS EN PAUSA desde el 24/11 (aprobado por el propietario): el largo del Extended Look tuvo 2 visualizaciones en 3 días. No se preparan largos hasta que el propietario lo reactive.
- TikTok en pausa: pasa a borrador cualquier publicación de TikTok no borrador de los próximos 5 días y avisa si algún vídeo de @gta674915 empieza a tener visualizaciones.

PASOS:
0) Arranca el relay del Extended Look con Bash en segundo plano (run_in_background: python3 _build/rk_relay.py 8765) y ejecuta bash _build/assets_rockstar.sh.
1) DATOS: vidiq_channel_videos si hay créditos (vidiq_balance, gratis); si no, Metricool getAnalyticsDataByMetrics (YTVP02, YTVP17, YTVP06, YTVP07 por vídeo; YTEV01, YTEV02 por día; llegan con 1–3 días de retraso).
   - Calcula la mediana de visualizaciones a 48 h y los KPIs de ESTRATEGIA.md sección h.
   - Señal de frenazo: un Short con menos de 20 visualizaciones a las 6 h, con la mediana de los 3 anteriores por encima de 100; o la mediana del día a 24 h por debajo del 40 % de la de los 7 días anteriores. Si salta, aplica la sección e: al día siguiente 3 Shorts; si se repite 2 días, 2 al día durante 3 días. Esta reducción de ritmo NO necesita aprobación; anótala en el registro.
2) NOVEDADES: python3 _build/rk_novedades.py y WebSearch de noticias oficiales de GTA 6. Si hay algo nuevo y verificado, 1–2 Shorts con prioridad. Puedes mover lo menos prioritario del calendario a días posteriores; anótalo en el registro.
3) PRODUCCIÓN: rellena los huecos libres de YouTube de los próximos 3 días con las ideas de ESTRATEGIA.md sección b (Shorts 1–18), en este orden:
   - primero las de más búsqueda que se puedan verificar;
   - luego la serie NOTICIAS semanal (lunes) y LA COMUNIDAD (2–3 por semana);
   - después QUIZ y MITO O VERDAD rehechos con juego real.
   No repitas un tema ya publicado sin un ángulo y datos nuevos. Varía estructura, duración y gráficos entre series. Aplica las fórmulas y el experimento A/B activo de la sección d (alterna las variantes y anota cuál lleva cada vídeo).
4) VÍDEOS LARGOS: en pausa; no prepares ninguno. En la revisión semanal, informa de cuántas visualizaciones lleva el largo del Extended Look (vídeo l1F78rTsfu8).
5) MONTAJE: clips=mezcla(...) de content.rk_pool, primer segundo en movimiento, rótulos cortos.
   - Renderiza con MA_VOICE=eleven ELEVENLABS_API_KEY=proxy-injected.
   - Pasa qc.py y revisa una hoja de fotogramas de cada vídeo antes de subirlo (sin logotipos, sin rótulos de Rockstar y con la imagen coherente con la voz).
6) PUBLICACIÓN: sube los MP4 a mapa-abierto-media/tandas/<fecha>/, comprueba que la URL raw devuelve 200 y programa con createScheduledPost (type short, public, GAMING, madeForKids false), con descripción con fuentes y créditos y firstCommentText con una pregunta.
7) REGISTRO: añade cada cambio con fecha y motivo al "Registro de cambios" de ESTRATEGIA.md. Haz commit y push de los dos repositorios.
8) DOMINGOS: revisión semanal con el formato fijo de la sección h. Decide los experimentos con los umbrales fijados.
9) RESUMEN: corto y en castellano para el propietario:
   - visualizaciones de lo publicado (mediana a 48 h y mejores);
   - KPIs fuera de umbral y lo que has hecho;
   - qué has programado;
   - qué necesitas del propietario.

APROBACIÓN NECESARIA (pregunta y no lo hagas hasta que te contesten):
- Cualquier gasto.
- Crear cuentas (TikTok o Instagram).
- Cambiar este ritmo hacia arriba (más de 4 Shorts al día) o reactivar los vídeos largos.
- Borrar vídeos publicados.
- Cambiar estas instrucciones.
