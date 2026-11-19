# Línea de tiempo de edición · V83 · ¿Hay hidrodeslizadores en GTA 6? Mito o verdad

**Proyecto:** 1080×1920 · 30 fps · duración total 00:18.862 · Short 9:16

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

### Escena 1 · 0.00 s → 5.62 s (5.62 s) · `00:00.000`
| Campo | Detalle |
|---|---|
| Fuente | Motion graphics propio (marca) |
| Contenido visual |  |
| Cámara |  |
| Iluminación | Paleta de marca: degradado noche-púrpura-magenta, acentos neón cian/magenta, sol de atardecer naranja |
| Animaciones | Rótulo entra con escala 90→100 % y desenfoque de movimiento (8 fotogramas); ítems escalonados cada 0,3 s; palabras clave en amarillo |
| Transición de salida | Corte |
| Efectos de sonido | Golpe |
| Rótulo | **PASEOS POR EL PANTANO** |
| Narración | ¿Mito o verdad? En GTA 6 puedes ir en hidrodeslizador por los pantanos. |
| Subtítulos | ¿Mito o verdad? · En GTA 6 / puedes ir en · hidrodeslizador / por los pantanos. |
| Imagen de referencia | `Imagenes/escenas/V83_escena_01.png` |
| Prompt Pika | ver `Prompts_Pika/V83_prompts_pika.md` · escena 1 |

### Escena 2 · 5.62 s → 13.90 s (8.28 s) · `00:05.617`
| Campo | Detalle |
|---|---|
| Fuente | Motion graphics propio (marca) |
| Contenido visual |  |
| Cámara |  |
| Iluminación | Paleta de marca: degradado noche-púrpura-magenta, acentos neón cian/magenta, sol de atardecer naranja |
| Animaciones | Rótulo entra con escala 90→100 % y desenfoque de movimiento (8 fotogramas); ítems escalonados cada 0,3 s; palabras clave en amarillo |
| Transición de salida | Corte |
| Efectos de sonido | Sello |
| Rótulo | **PASEOS POR EL PANTANO** |
| Narración | ¡Verdad! Se vio en el Extended Look: hidrodeslizador por Grassrivers, la versión de los Everglades. Y también motos de agua. |
| Subtítulos | ¡Verdad! · Se vio en el / Extended Look: · hidrodeslizador / por Grassrivers, · la versión de / los Everglades. · Y también motos de agua. |
| Imagen de referencia | `Imagenes/escenas/V83_escena_02.png` |
| Prompt Pika | ver `Prompts_Pika/V83_prompts_pika.md` · escena 2 |

### Escena 3 · 13.90 s → 18.86 s (4.96 s) · `00:13.901`
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
| Narración | Y cuidado con los caimanes. Sígueme para más mitos y verdades de GTA. |
| Subtítulos | Y cuidado con / los caimanes. · Sígueme para más mitos / y verdades de GTA. |
| Imagen de referencia | `Imagenes/escenas/V83_escena_03.png` |
| Prompt Pika | ver `Prompts_Pika/V83_prompts_pika.md` · escena 3 |

## Instrucciones por programa
**DaVinci Resolve:** Proyecto 1080×1920 30 fps → importar PNG de escenas y la locución → colocar según la tabla (Inicio_s) → Fusion: título 'Text+' con la fuente de marca → Fairlight: ducking con 'Sidechain' de A1 a A2 → File › Import › Subtitle (`.srt`) o usar el `.ass` quemado vía Fusion → Deliver: H.264, 1080×1920, 30 fps, 16-20 Mbps (largo) / 12 Mbps (Short), AAC 320 kbps.
**Premiere Pro:** Secuencia personalizada 1080×1920 30 fps → Archivo › Importar el CSV como referencia de marcadores (copiar Inicio_mmss) → Gráficos esenciales para rótulos → Subtítulos: importar `.srt` y aplicar estilo de marca → Audio esencial: Música con 'Atenuación' automática → Exportar H.264 'Coincidir con origen - Alta velocidad de bits'.
**CapCut:** Lienzo 9:16 → añadir PNG/clips en el orden de la tabla ajustando duraciones → Texto › Subtítulos automáticos (revisar con el `.srt`) o importar `.srt` → estilo: blanco, contorno negro 8, sombra → Audio: música −22 dB → Exportar 1080p, 30 fps, alta calidad.
