# Línea de tiempo de edición · V49 · ¿GTA 6 tiene 6 estrellas de búsqueda?

**Proyecto:** 1080×1920 · 30 fps · duración total 00:24.532 · Short 9:16

## Pistas (de arriba abajo)
| Pista | Contenido |
|---|---|
| V4 | Rótulos y textos en movimiento (plantillas de marca) |
| V3 | Subtítulos (importar `.ass` en DaVinci/Premiere o `.srt` + estilo en CapCut) |
| V2 | Gráficos / etiquetas ('Fuente: Rockstar Games', 'Recreación IA', 'Gameplay propio') |
| V1 | Imagen principal: material oficial, gameplay, clips Pika o gráficos (PNG en `Imagenes/escenas/`) |
| A1 | Locución (final; la guía TTS sirve de referencia de tiempos) |
| A2 | Música de marca `05_RECURSOS_AUDIO/Musica/` a −22 dB bajo voz (ducking automático −6 dB) |
| A3 | Efectos de sonido (`05_RECURSOS_AUDIO/SFX/`) a −18 dB |

## Reglas de estilo de montaje
- Cambio visual cada 3-5 s como máximo (en Shorts, cada 1,5-3 s): alternar plano, zoom de énfasis o rótulo.
- Zoom cinematográfico: 100→108 % en planos estáticos; zoom de énfasis 100→115 % en 6 fotogramas sobre el detalle comentado.
- Transiciones: corte seco por defecto; whip pan solo en cambios de bloque; nada de transiciones 3D ni efectos de estrellas.
- Texto en pantalla: InterDisplay Black Italic, blanco con contorno negro; palabra clave en amarillo #FFD666.
- Material oficial: crédito 'Fuente: Rockstar Games' visible; fragmentos breves y siempre con comentario encima (uso informativo).
- Marca de agua: se configura en YouTube Studio (no incrustar). Pantalla final: —.

## Escenas

### Escena 1 · 0.00 s → 4.69 s (4.69 s) · `00:00.000`
| Campo | Detalle |
|---|---|
| Fuente | Motion graphics propio (marca) |
| Contenido visual |  |
| Cámara |  |
| Iluminación | Paleta de marca: degradado noche-púrpura-magenta, acentos neón cian/magenta, sol de atardecer naranja |
| Animaciones | Rótulo entra con escala 90→100 % y desenfoque de movimiento (8 fotogramas); ítems escalonados cada 0,3 s; palabras clave en amarillo |
| Transición de salida | Corte |
| Efectos de sonido | Golpe |
| Rótulo | **GTA 6 TIENE 6 ESTRELLAS DE BÚSQUEDA** |
| Narración | ¿Mito o verdad? GTA 6 tiene seis estrellas de búsqueda. |
| Subtítulos | ¿Mito o verdad? · GTA 6 tiene seis / estrellas de búsqueda. |
| Imagen de referencia | `Imagenes/escenas/V49_escena_01.png` |
| Prompt Pika | ver `Prompts_Pika/V49_prompts_pika.md` · escena 1 |

### Escena 2 · 4.69 s → 17.76 s (13.07 s) · `00:04.691`
| Campo | Detalle |
|---|---|
| Fuente | Motion graphics propio (marca) |
| Contenido visual |  |
| Cámara |  |
| Iluminación | Paleta de marca: degradado noche-púrpura-magenta, acentos neón cian/magenta, sol de atardecer naranja |
| Animaciones | Rótulo entra con escala 90→100 % y desenfoque de movimiento (8 fotogramas); ítems escalonados cada 0,3 s; palabras clave en amarillo |
| Transición de salida | Corte |
| Efectos de sonido | Sello |
| Rótulo | **GTA 6 TIENE 6 ESTRELLAS DE BÚSQUEDA** |
| Narración | ¡Verdad! En el Extended Look volvieron las seis estrellas, el máximo clásico de la saga. GTA 5 se quedaba en cinco. Y la policía ahora se fija en tu coche, tu ropa y tu descripción. |
| Subtítulos | ¡Verdad! · En el Extended Look / volvieron las seis · estrellas, el máximo / clásico de la saga. · GTA 5 se quedaba / en cinco. · Y la policía ahora / se fija en tu · coche, tu ropa y / tu descripción. |
| Imagen de referencia | `Imagenes/escenas/V49_escena_02.png` |
| Prompt Pika | ver `Prompts_Pika/V49_prompts_pika.md` · escena 2 |

### Escena 3 · 17.76 s → 24.53 s (6.77 s) · `00:17.761`
| Campo | Detalle |
|---|---|
| Fuente | Motion graphics propio (marca) |
| Contenido visual |  |
| Cámara |  |
| Iluminación | Paleta de marca: degradado noche-púrpura-magenta, acentos neón cian/magenta, sol de atardecer naranja |
| Animaciones | Rótulo entra con escala 90→100 % y desenfoque de movimiento (8 fotogramas); ítems escalonados cada 0,3 s; palabras clave en amarillo |
| Transición de salida | Corte |
| Efectos de sonido | Sting |
| Rótulo | **SÍGUEME** |
| Narración | Así que cambiar de ropa o de coche puede salvarte. Sígueme para más mitos y verdades de GTA. |
| Subtítulos | Así que cambiar de ropa o / de coche puede salvarte. · Sígueme para más mitos / y verdades de GTA. |
| Imagen de referencia | `Imagenes/escenas/V49_escena_03.png` |
| Prompt Pika | ver `Prompts_Pika/V49_prompts_pika.md` · escena 3 |

## Instrucciones por programa
**DaVinci Resolve:** Proyecto 1080×1920 30 fps → importar PNG de escenas y la locución → colocar según la tabla (Inicio_s) → Fusion: título 'Text+' con la fuente de marca → Fairlight: ducking con 'Sidechain' de A1 a A2 → File › Import › Subtitle (`.srt`) o usar el `.ass` quemado vía Fusion → Deliver: H.264, 1080×1920, 30 fps, 16-20 Mbps (largo) / 12 Mbps (Short), AAC 320 kbps.
**Premiere Pro:** Secuencia personalizada 1080×1920 30 fps → Archivo › Importar el CSV como referencia de marcadores (copiar Inicio_mmss) → Gráficos esenciales para rótulos → Subtítulos: importar `.srt` y aplicar estilo de marca → Audio esencial: Música con 'Atenuación' automática → Exportar H.264 'Coincidir con origen - Alta velocidad de bits'.
**CapCut:** Lienzo 9:16 → añadir PNG/clips en el orden de la tabla ajustando duraciones → Texto › Subtítulos automáticos (revisar con el `.srt`) o importar `.srt` → estilo: blanco, contorno negro 8, sombra → Audio: música −22 dB → Exportar 1080p, 30 fps, alta calidad.
