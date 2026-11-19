# Estado del proyecto · Mapa Abierto (traspaso entre sesiones)

Última actualización: 18/11/2026. Si eres una sesión nueva de Claude: lee este archivo y `AUTOMATIZACION.md` antes de hacer nada.

## Qué es
Canal de YouTube + TikTok en castellano de España sobre GTA 6 (lanzamiento 19/11/2026, PS5 y Xbox Series X|S). Marca **Mapa Abierto** (identidad en `01_IDENTIDAD_VISUAL/`). Promesa editorial: separar siempre lo oficial de los rumores; nada de gameplay inventado ni imágenes de IA presentadas como del juego.

## Cuentas y servicios
| Servicio | Estado | Detalle |
|---|---|---|
| YouTube | Conectado vía Metricool | canal `UCXpwmvTrqiRvk-bVAcJUt7A` |
| TikTok | Conectado vía Metricool | `@gta674915` |
| Metricool | Conector de Claude | marca `blogId` 8199011, zona `Europe/Madrid` |
| vidIQ | Conector de Claude | investigación de palabras clave (datos reales de búsquedas) |
| ElevenLabs | Credencial guardada en el entorno (proxy) | voz **Nico – History & Documentary** (`FXn3GKRRt9FCEyTbrkaL`), modelo `eleven_v4`; plan Creator |
| GitHub | `mapa-abierto` (privado, código y guiones) · `mapa-abierto-media` (público, MP4 para Metricool) | |

## Vídeos producidos
| Tanda | Vídeos | Estado |
|---|---|---|
| 1 | V01–V10 | V01–V07 finales con voz Nico; programados a mano por el usuario. V08–V10 son borradores: necesitan gameplay real |
| 2 | V11–V20 | Shorts finales; programados a mano por el usuario |
| 3 | V21–V40 | 20 Shorts en 5 series; programados a mano (YouTube + TikTok) |
| 4 | V41–V47 | Programados por Claude en Metricool (14 posts, 19–20/11). Temas elegidos con vidIQ |

Los MP4 no se guardan en este repositorio (ver `.gitignore`); se regeneran con el motor. La tanda 4 está en `mapa-abierto-media/tandas/2026-11-19/`.

## Motor de producción (`_build/`)
- `build_videos.py <IDs>`: voz → subtítulos → escenas → montaje → MP4 + SEO + miniaturas. Con `MA_VOICE=eleven ELEVENLABS_API_KEY=proxy-injected` usa ElevenLabs.
- Formatos disponibles: rótulos e ítems animados, QUIZ (opciones + cuenta atrás + revelado), MITO O VERDAD (sello), etiqueta de serie y barra de progreso.
- Guiones: `_build/content/` (`shorts3.py` tiene los helpers `mk`, `quiz`, `mito`; cada tanda nueva es `tanda_AAAAMMDD.py` con `SHORTS`, `SCHED`, `TANDA`).
- `build_centro.py <salida.html> content.tanda_X`: página de publicación de la tanda.
- `qc.py`: control de calidad.

## Automatización
- Tarea programada diaria a las 7:37 (Europe/Madrid): "Mapa Abierto · tanda diaria con publicación". Está vinculada a la sesión donde se creó. **Si esa sesión ya no existe, hay que volver a crearla desde la sesión nueva** (las tareas que abren sesiones nuevas no pueden llevar conectores en esta organización).
- Permisos: `.claude/settings.json` (solo se aplica en sesiones con un único repositorio) + modo Automático.

## Pendiente
- Pasar la operación a una sesión con un solo repositorio (hacer público `mapa-abierto` y alojar ahí los MP4) para no tener que aprobar acciones.
- V08–V10: montar cuando el usuario envíe grabaciones del juego (o rehacer con material oficial de Rockstar).
- Desde el 19/11: los Shorts pueden usar capturas y tráiler oficiales de Rockstar (ver AUTOMATIZACION.md). V59 es la prueba (20/11 17:00 YT, 17:40 TikTok).
- Revisar analíticas en Metricool tras las primeras publicaciones y ajustar horarios y series.
