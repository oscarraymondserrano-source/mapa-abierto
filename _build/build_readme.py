import os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
meta = json.load(open(os.path.join(ROOT, "_build", "meta.json")))
rows = []
for m in meta:
    d = m["dur"]
    rows.append(f"| {m['id']} | {m['titulo']} | {'Largo 16:9' if m['formato'] == 'largo' else 'Short 9:16'} | {int(d // 60)}:{int(d % 60):02d} | "
                f"{'✅ **FINAL** (motion graphics)' if m['modo'] == 'final' else '🎬 Animatic + todos los recursos'} | {m['fecha']} | `{m['carpeta']}/` |")
txt = f"""# GTA6_CANAL_YOUTUBE · Paquete de producción del canal **MAPA ABIERTO**

Canal en castellano de España sobre GTA VI (lanzamiento: **jueves 19/11/2026**). Fecha de preparación: lunes 16/11/2026.

## Empieza aquí
1. `01_IDENTIDAD_VISUAL/guia_de_marca.md` → nombre, descripción, palabras clave, colores, voz. Sube perfil, banner y marca de agua.
2. `03_CALENDARIO/calendario_publicacion.md` → qué publicar y cuándo (importa el `.ics`).
3. Cada `VIDEO_XX/` → guion, locución, prompts, montaje, subtítulos, miniaturas, SEO y vídeo.
4. `04_CONTROL_CALIDAD/informe_control_calidad.md` → comprobaciones y ajustes de exportación.

## Los 10 vídeos
| # | Título definitivo | Formato | Duración | Estado | Publicación | Carpeta |
|---|---|---|---|---|---|---|
{chr(10).join(rows)}

**FINAL** = MP4 publicable (gráficos propios, música original, subtítulos). Recomendado sustituir la voz guía por la voz definitiva.
**Animatic** = MP4 con tiempos, voz guía, música y subtítulos definitivos y una tarjeta por escena que indica el material que va en ese hueco (material oficial de Rockstar, clip Pika o gameplay propio). No se ha simulado ninguna imagen del juego.

## Estructura
```
GTA6_CANAL_YOUTUBE/
├── 00_LEEME.md
├── 01_IDENTIDAD_VISUAL/  Logotipo/ Perfil/ Banner/ Marca_de_agua/ Plantillas/ Intro_Outro/ guia_de_marca.md
├── 02_INVESTIGACION/     informe_investigacion_mercado.md (20 oportunidades, competencia, fuentes)
├── 03_CALENDARIO/        calendario_publicacion.md · .csv · .ics
├── 04_CONTROL_CALIDAD/   informe_control_calidad.md · prueba_legibilidad_movil_miniaturas.png
├── 05_RECURSOS_AUDIO/    Musica/ (pista original) · SFX/ (whoosh, sting)
├── VIDEO_01_…/ … VIDEO_10_…/
│   ├── Guion/          XX_guion_completo.md (concepto, 5 títulos, guion palabra por palabra)
│   ├── Locucion/       texto limpio · texto ElevenLabs · ficha de voz · locución guía .wav
│   ├── Imagenes/       escenas/ (una imagen por escena) + gráficos específicos
│   ├── Prompts_Pika/   prompts por escena (.md) + copiar-pegar (.txt)
│   ├── Subtitulos/     .srt (YouTube) + .ass (estilo de marca para incrustar)
│   ├── Miniatura/      propuestas A/B/C (la elegida lleva _ELEGIDA) + capas de texto
│   ├── Montaje/        línea de tiempo (.md y .csv), capítulos, lista de grabación
│   ├── SEO/            título, descripción, etiquetas, hashtags, comentario fijado…
│   └── Video_Final/    MP4 + LEEME
└── _build/             scripts que generan todo (reproducible: `python3 build_videos.py`)
```

## Qué no se ha podido hacer aquí y cómo terminarlo
| Falta | Motivo | Alternativa entregada / cómo completarlo |
|---|---|---|
| Clips de Pika | No hay acceso a Pika desde este entorno | Prompts listos por escena; generar e insertar según la línea de tiempo |
| Material oficial de Rockstar (tráileres, arte) | Red del entorno bloqueada para descargar | Huecos marcados con descripción exacta del plano; descargar de rockstargames.com/VI y del canal oficial |
| Gameplay real | El juego se desbloquea el 19/11 | Listas de grabación precisas + guiones con huecos [ ] marcados |
| Voz de calidad de emisión | Sin acceso a ElevenLabs u otro servicio | Locución guía TTS con tiempos reales + texto preparado para ElevenLabs + ficha de voz |
| Volúmenes de búsqueda (Trends, autocompletar) | Bloqueado por la red | Valoraciones cualitativas claramente marcadas; método para comprobar antes de publicar |
"""
open(os.path.join(ROOT, "00_LEEME.md"), "w").write(txt)
print("leeme ok")
