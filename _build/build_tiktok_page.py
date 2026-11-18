import os, sys, glob, io, base64, json
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
from build_videos import VIDEOS
from content.tiktok import TT, TAGS
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
V = {v["id"]: v for v in VIDEOS}
DOW = {"2026-11-17": "Martes 17/11", "2026-11-18": "Miércoles 18/11", "2026-11-19": "Jueves 19/11", "2026-11-20": "Viernes 20/11", "2026-11-21": "Sábado 21/11"}
items, md = [], ["# TikTok · textos y calendario\n", "Mismos MP4 verticales de los Shorts. Programa desde el ordenador en tiktok.com/tiktokstudio/upload (permite programar hasta 10 días antes).\n",
                 "| Día | Hora | Vídeo | Archivo | Texto para pegar |", "|---|---|---|---|---|"]
for fecha, hora, vid, texto, extra in TT:
    v = V[vid]; base = os.path.join(ROOT, v["carpeta"])
    mp4 = os.path.basename(glob.glob(os.path.join(base, "Video_Final", "*FINAL*.mp4"))[0])
    cap = f"{texto}\n\n{TAGS} {extra}"
    im = Image.open(glob.glob(os.path.join(base, "Miniatura", "*portada*.png"))[0]).convert("RGB"); im.thumbnail((240, 240))
    b = io.BytesIO(); im.save(b, "JPEG", quality=72)
    when = f"{DOW[fecha]} · {hora}"
    items.append(dict(id=vid, fecha=fecha, when=when, titulo=v["titulos"][v["elegido"]], formato="Short", carpeta=v["carpeta"], mp4=mp4,
                      vertical=True, img="data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode(), buttons=[["Copiar texto del post", cap]], preview=cap))
    md.append(f"| {DOW[fecha]} | {hora} | {vid} | `{v['carpeta']}/{mp4}` | {cap.replace(chr(10), ' ')} |")
os.makedirs(os.path.join(ROOT, "06_TIKTOK"), exist_ok=True)
open(os.path.join(ROOT, "06_TIKTOK", "tiktok_textos_y_calendario.md"), "w").write("\n".join(md) + "\n")
t = open(os.path.join(os.path.dirname(__file__), "upload_page_template.html")).read()
R = [("<title>Subidas Mapa Abierto</title>", "<title>TikTok Mapa Abierto</title>"),
     ("Plan de subidas · semana GTA 6", "Plan de TikTok · semana GTA 6"),
     ("17 vídeos listos: súbelos y prográmalos", "15 Shorts para TikTok: prográmalos"),
     ("Cada ficha tiene todo lo que pide YouTube Studio. Arrastra el MP4 de la carpeta indicada, pulsa los botones de copiar, pega en su campo y marca la casilla al terminar. Las horas son de la España peninsular.",
      "Son los mismos MP4 verticales de los Shorts. Desde el ordenador puedes programarlos todos ahora: TikTok permite programar hasta 10 días antes. Las horas son de la España peninsular."),
     ("Antes de empezar (solo la primera vez)", "Antes de empezar (solo la primera vez)"),
     ('''      <li>Entra en <b>studio.youtube.com</b> y crea el canal <b>Mapa Abierto</b>.</li>
      <li><b>Personalización → Imagen de marca:</b> sube la foto, el banner y la marca de agua de la carpeta <code>IMAGENES_DEL_CANAL</code>.</li>
      <li><b>Personalización → Información básica:</b> pega la descripción del canal de <code>guia_de_marca.md</code>.</li>
      <li>Verifica tu teléfono en <b>youtube.com/verify</b> para poder subir miniaturas.</li>
      <li><b>Contenido → Listas:</b> crea "GTA 6 · Lanzamiento", "GTA 6 · Mapa y mundo abierto" y "GTA 6 · Shorts".</li>''',
      '''      <li>Crea la cuenta <b>@mapaabierto</b> (o la variante libre más parecida) y usa como foto <code>MapaAbierto_perfil_800x800.png</code>.</li>
      <li>Biografía: <b>Noticias, guías y secretos de GTA 6 🌴 Lo oficial, separado de los rumores.</b></li>
      <li>Pon el enlace a tu canal de YouTube en el perfil cuando TikTok te lo permita.</li>'''),
     ('''    <li><b>Crear → Subir vídeos</b> y arrastra el MP4.</li>
    <li>Pega <b>título</b> y <b>descripción</b>. En los largos, sube la <b>miniatura</b>.</li>
    <li>Elige la <b>lista</b> y marca <b>"No es para niños"</b>. En <b>Mostrar más</b>, pega las <b>etiquetas</b>.</li>
    <li><b>Subtítulos → Subir archivo → Con sincronización</b>: el archivo .srt.</li>
    <li><b>Visibilidad → Programar</b> con el día y la hora de la ficha.</li>
    <li>Al publicarse, pega el <b>comentario</b> y fíjalo (⋮ → Fijar).</li>''',
      '''    <li>Entra en <b>tiktok.com/tiktokstudio/upload</b> desde el ordenador y arrastra el MP4.</li>
    <li>Pega el <b>texto del post</b> en la descripción (ya lleva los hashtags).</li>
    <li>Portada: elige el fotograma con el <b>título grande</b> del principio.</li>
    <li>Activa <b>Programar</b> y pon el día y la hora de la ficha.</li>
    <li>Pulsa <b>Programar</b>. Al publicarse, responde a los primeros comentarios.</li>'''),
     ('''        el("div", {}, "Subtítulos: ", el("code", { text: it.srt })),
        el("div", {}, "Lista: ", el("code", { text: it.playlist })));''', '''        it.srt ? el("div", {}, "Subtítulos: ", el("code", { text: it.srt })) : null,
        it.playlist ? el("div", {}, "Lista: ", el("code", { text: it.playlist })) : null);'''),
     ('''          el("div", { class: "btns" },
            copyBtn("Copiar título", it.titulo, holder),
            copyBtn("Copiar descripción", it.desc, holder),
            copyBtn("Copiar etiquetas", it.tags, holder),
            copyBtn("Copiar comentario", it.comentario, holder)),''', '''          el("div", { class: "btns" }, ...it.buttons.map(([l, t]) => copyBtn(l, t, holder))),'''),
     ('''      const desc = el("details", { class: "desc" }, el("summary", { text: "Ver descripción" }), el("pre", { text: it.desc }));''',
      '''      const desc = el("details", { class: "desc", open: "" }, el("summary", { text: "Texto del post" }), el("pre", { text: it.preview }));'''),
     ('''"Programado en YouTube"''', '''"Programado en TikTok"'''),
     ('''const KEY = "ma-subidas-v1";''', '''const KEY = "ma-tiktok-v1";'''),
     ('''"Vídeo largo" }''', '''"Vídeo largo" }'''),
]
for a, b2 in R:
    assert a in t, a[:60]
    t = t.replace(a, b2)
out = sys.argv[1]
open(out, "w").write(t.replace("__DATA__", json.dumps(items, ensure_ascii=False).replace("</", "<\\/")))
print(len(items), "posts")
