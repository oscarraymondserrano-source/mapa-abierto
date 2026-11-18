"""Genera el Centro de Publicación (tanda 3) y el calendario/captions de la tanda."""
import os, sys, glob, io, base64, json
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
from build_videos import VIDEOS, apply_final, FO
from content.shorts3 import SHORTS3, SCHED3
from content import tiktok
import build_calendar as cal

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = sys.argv[1]
DOW = {"2026-11-17": "Martes 17/11", "2026-11-18": "Miércoles 18/11", "2026-11-19": "Jueves 19/11", "2026-11-20": "Viernes 20/11",
       "2026-11-21": "Sábado 21/11", "2026-11-22": "Domingo 22/11", "2026-11-23": "Lunes 23/11"}
SERIE_TT = {"QUIZ": ("🧠", "#quiz #quizgta #trivia"), "MITO": ("🔍", "#mitooverdad #mitos"), "LA SAGA": ("📼", "#historiagta #nostalgia"),
            "LANZAMIENTO": ("⏰", "#lanzamiento #parati"), "ESTO": ("⚔️", "#encuesta #parati")}
TT_BASE = "#gta6 #gtavi #gta #videojuegos #gaming"

for v in SHORTS3:
    apply_final(v)
posts, csv_rows = [], []
for v in SHORTS3:
    vid = v["id"]; base = os.path.join(ROOT, v["carpeta"])
    r = next(x for x in SCHED3 if x[0] == vid)
    mp4 = os.path.basename(glob.glob(os.path.join(base, "Video_Final", "*FINAL*.mp4"))[0])
    desc = open(glob.glob(os.path.join(base, "SEO", "*_descripcion_youtube.txt"))[0]).read().strip()
    im = Image.open(glob.glob(os.path.join(base, "Miniatura", "*portada*.png"))[0]).convert("RGB"); im.thumbnail((300, 300))
    b = io.BytesIO(); im.save(b, "JPEG", quality=74)
    img = "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()
    title = v["titulos"][v["elegido"]]
    key = next(k for k in SERIE_TT if v["serie"].startswith(k))
    emo, ttags = SERIE_TT[key]
    cta = v["seo"]["comentario"].replace("📌", "").strip()
    caption = f"{title} {emo}\n{cta}\n\n{TT_BASE} {ttags}"
    common = dict(id=vid, title=title, short=v["escenas"][0]["rotulo"].title() if False else title[:42], serie=v["serie"], folder=v["carpeta"], mp4=mp4, img=img)
    d1, h1, d2, h2 = r[1], r[2], r[3], r[4]
    dd = lambda d: f"{d[8:10]}/{d[5:7]}/{d[:4]}"
    posts.append(dict(common, key=vid + "-yt", plat="yt", day=d1, dayLabel=DOW[d1], time=h1, iso=f"{d1}T{h1}:00+01:00",
                      srt=f"{vid}_subtitulos.srt", playlist=v["seo"]["playlist"], preview=desc,
                      copies=[["Copiar título", title], ["Copiar descripción", desc], ["Copiar etiquetas", ", ".join(v["seo"]["tags"])],
                              ["Copiar comentario fijado", v["seo"]["comentario"]], ["Copiar fecha y hora", f"{dd(d1)} {h1}"]]))
    posts.append(dict(common, key=vid + "-tt", plat="tt", day=d2, dayLabel=DOW[d2], time=h2, iso=f"{d2}T{h2}:00+01:00", srt="", playlist="",
                      preview=caption, copies=[["Copiar texto del post", caption], ["Copiar fecha y hora", f"{dd(d2)} {h2}"]]))
    csv_rows.append((vid, title, v["serie"], d1, h1, d2, h2, caption.replace("\n", " ")))
posts.sort(key=lambda p: (p["iso"], p["plat"]))

# mapa de calor de la semana (todas las tandas, YouTube + TikTok)
days = ["2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
hours = list(range(9, 24))
cnt = {(d, h): 0 for d in days for h in hours}
def add(d, t):
    h = int(t[:2])
    if (d, h) in cnt:
        cnt[(d, h)] += 1
for r in cal.PUB: add(r[0], r[1])
for r in tiktok.TT: add(r[0], r[1])
for r in SCHED3: add(r[1], r[2]); add(r[3], r[4])
heat = dict(hours=hours, rows=[dict(label=DOW[d], cells=[cnt[(d, h)] for h in hours]) for d in days])
why = [
    ["Picos de España", "La audiencia hispana de gaming se concentra entre las 13:00-15:30 (comida) y las 19:00-23:30. Ahí van los quizzes y los mitos, que piden participar."],
    ["Guiño a Latinoamérica", "El Short de la hora en Latinoamérica sale a las 15:30 en España: mañana temprano en México y mediodía en Argentina."],
    ["Día de lanzamiento", "El jueves concentra más publicaciones: es el día de más búsquedas. La de las 23:15 del miércoles llega justo antes del desbloqueo."],
    ["Sin solaparse", "Nunca se publica a menos de 45 minutos de otro vídeo de la misma red, y TikTok va siempre desfasado respecto a YouTube."],
    ["Series reconocibles", "Cada serie lleva su etiqueta y su formato. Quien ve un quiz y acierta quiere el siguiente: eso dispara suscripciones."],
    ["Barra de progreso", "Todos los Shorts nuevos llevan una barra animada arriba: ver cuánto falta anima a terminar el vídeo y mejora la retención."],
]
series = [["QUIZ GTA (5)", "Pregunta, 3 opciones y 3 segundos para pensar antes de la respuesta."],
          ["MITO O VERDAD (5)", "Una afirmación y un sello rojo o verde. Corto y muy compartible."],
          ["LA SAGA EN 30 s (6)", "Historia y curiosidades de GTA, de 1997 a Leonida."],
          ["LANZAMIENTO (2)", "Hora en Latinoamérica y qué hacer si a las 00:00 no te deja jugar."],
          ["ESTO O AQUELLO (2)", "Encuestas en comentarios: PS5 o Xbox, ciudad o naturaleza."]]
data = dict(posts=posts, heat=heat, why=why, series=series)
t = open(os.path.join(os.path.dirname(__file__), "centro_template.html")).read()
open(OUT, "w").write(t.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))

# calendario de la tanda (md + csv + ics)
cd = os.path.join(ROOT, "03_CALENDARIO")
md = ["# Tanda 3 · 20 Shorts (YouTube + TikTok)\n", "| Vídeo | Serie | YouTube | TikTok | Título |", "|---|---|---|---|---|"]
for vid, title, serie, d1, h1, d2, h2, cap in csv_rows:
    md.append(f"| {vid} | {serie} | {DOW[d1]} · {h1} | {DOW[d2]} · {h2} | {title} |")
open(os.path.join(cd, "calendario_tanda3.md"), "w").write("\n".join(md) + "\n")
import csv as _csv
with open(os.path.join(cd, "calendario_tanda3.csv"), "w", newline="") as fh:
    w = _csv.writer(fh); w.writerow(["video", "titulo", "serie", "youtube_fecha", "youtube_hora", "tiktok_fecha", "tiktok_hora", "texto_tiktok"])
    w.writerows(csv_rows)
print(len(posts), "posts")
