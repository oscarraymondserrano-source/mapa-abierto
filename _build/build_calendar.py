import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "03_CALENDARIO")
os.makedirs(OUT, exist_ok=True)

# (fecha, hora, id, título, formato, estado de producción, tarea de producción ese día)
PUB = [
    ('2026-11-17', '17:30', 'V02', '¿A qué hora sale GTA 6 en España? ⏰', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-17', '18:30', 'V01', 'GTA 6: todo lo que debes saber antes de jugar (hora, precarga, espacio y más)', 'Largo', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-17', '20:00', 'V14', 'Lo que NO sabemos de GTA 6 (a 2 días)', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-17', '21:15', 'V13', '13 años esperando GTA 6, en 45 segundos', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-17', '22:30', 'V04', 'GTA 6: cómo precargarlo y cuánto ocupa', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-18', '09:30', 'V15', '¿Tienes Xbox Series S? Mira esto antes de GTA 6', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-18', '11:00', 'V11', '¿Cuándo sale GTA 6 en PC?', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-18', '14:00', 'V05', '3 cosas de los tráileres de GTA 6 que casi nadie sabe', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-18', '16:30', 'V17', '¿Cuánto mide el mapa de GTA 6? La verdad', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-18', '18:30', 'V03', 'El mapa de GTA 6 explicado: las 6 regiones de Leonida', 'Largo', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-18', '20:30', 'V06', '¿Quiénes son Jason y Lucia en GTA 6?', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-18', '22:30', 'V18', '3 errores que vas a cometer esta noche con GTA 6', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-19', '11:00', 'V07', 'Haz esto ANTES de empezar GTA 6', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-19', '18:00', 'V12', 'Vice City vuelve: de 1986 a hoy', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-20', '13:00', 'V19', 'El caimán más famoso de GTA 6', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-20', '18:00', 'V08', 'GTA 6: primeras impresiones sin spoilers — ¿merece la pena?', 'Largo', 'Grabar jue 19 (lista de grabación), rellenar huecos del guion; envíame las grabaciones y lo monto'),
    ('2026-11-21', '13:00', 'V20', 'Leonida es Florida: cada zona explicada', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-21', '19:00', 'V16', 'GTA 6 vs GTA 5: 3 cambios confirmados', 'Short', 'FINAL con voz Nico: listo para subir'),
    ('2026-11-22', '12:00', 'V09', 'GTA 6: guía para principiantes — 12 consejos para tus primeras horas', 'Largo', 'Verificar cada consejo en partida (vie-sáb); envíame las grabaciones y lo monto'),
    ('2026-11-23', '19:00', 'V10', 'El primer secreto de GTA 6 que tienes que ver', 'Short', 'Publicar en cuanto haya un secreto verificado en partida propia'),
]

PLAN = [
    ("Mar 17/11", "Crear el canal (perfil, banner, marca de agua, descripción, listas) y programar en YouTube Studio TODOS los vídeos terminados de esta tabla (V01-V07 y V11-V20): así se publican solos. Si ya subiste V01/V02 ayer, sáltalos."),
    ("Mié 18/11", "Responder comentarios en la primera hora de cada publicación. Verificar precarga al 100 % y preparar la grabación (≥ 200 GB libres en el PC o capturadora). 23:30: post de Comunidad con cuenta atrás."),
    ("Jue 19/11", "00:00 desbloqueo → grabar sesión 1 (lista de grabación de V08). Tarde: segunda sesión (V08/V09). Enviar las grabaciones para montar V08."),
    ("Vie 20/11", "Seguir verificando los consejos de V09 en partida. Apuntar cualquier secreto encontrado (V10)."),
    ("Sáb 21/11", "Grabar el secreto para V10 y enviar las grabaciones de V09."),
    ("Dom 22/11", "Revisar analíticas: CTR de miniaturas y retención media; qué Shorts funcionan mejor para repetir formato."),
    ("Lun 23/11", "Planificar la segunda tanda con gameplay (dinero, coches, recorrido por Vice City, secretos)."),
]

md = ["# Calendario de publicación · semana de lanzamiento de GTA 6\n",
      "Horas en **hora peninsular española (CET)**. Lanzamiento: **jueves 19/11/2026, 00:00**.\n",
      "## Publicaciones\n", "| Fecha | Hora | Vídeo | Título | Formato | Estado / qué falta |", "|---|---|---|---|---|---|"]
dias = {"2026-11-16": "Lun 16/11", "2026-11-17": "Mar 17/11", "2026-11-18": "Mié 18/11", "2026-11-19": "Jue 19/11", "2026-11-20": "Vie 20/11", "2026-11-21": "Sáb 21/11",
        "2026-11-22": "Dom 22/11", "2026-11-23": "Lun 23/11"}
for d, h, i, t, f, e in PUB:
    md.append(f"| {dias[d]} | {h} | **{i}** | {t} | {f} | {e} |")
md += ["\n## Por qué este orden",
       "- **Antes del lanzamiento (17-18/11):** 2 largos + 10 Shorts que responden a las búsquedas urgentes (hora, precarga, qué saber, mapa, personajes). Se publica 1 largo por la tarde (18:00-19:00, máxima audiencia en España tras el trabajo/clases) y un Short por la noche (21:30).",
       "- **Día del lanzamiento (19/11):** un Short con gameplay real de menús (rápido de grabar y editar) a mediodía, cuando la gente que no jugó a medianoche busca cómo empezar.",
       "- **Después (20-23/11):** primeras impresiones el viernes (pico de indecisos antes del fin de semana), guía el domingo a mediodía (sesiones largas de juego) y secretos cuando estén verificados.",
       "- Nunca dos vídeos largos el mismo día; separación mínima de 1,5 h entre publicaciones del mismo día. Los Shorts se reparten de mañana a noche para llenar el feed durante la semana de máximo interés.\n",
       "## Plan de producción diario\n", "| Día | Tareas |", "|---|---|"]
md += [f"| {d} | {t} |" for d, t in PLAN]
md += ["\n## Material que solo se puede conseguir después del desbloqueo",
       "- V08: sesión completa de primeras horas + rendimiento (ver `VIDEO_08_*/Montaje/V08_lista_de_grabacion.md`).",
       "- V09: verificación de cada consejo (ver `VIDEO_09_*/Montaje/V09_lista_de_grabacion.md`).",
       "- V10: secreto verificado (ver `VIDEO_10_*/Montaje/V10_lista_de_grabacion.md`).\n",
       "Importa `calendario_publicacion.ics` en Google Calendar / Outlook para tener avisos."]
open(os.path.join(OUT, "calendario_publicacion.md"), "w").write("\n".join(md) + "\n")

with open(os.path.join(OUT, "calendario_publicacion.csv"), "w") as fh:
    fh.write("fecha,hora,video,titulo,formato,estado\n")
    for r in PUB:
        fh.write(",".join('"' + x.replace('"', "'") + '"' for x in r) + "\n")

ics = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//MapaAbierto//Calendario//ES", "CALSCALE:GREGORIAN",
       "BEGIN:VTIMEZONE", "TZID:Europe/Madrid", "BEGIN:STANDARD", "DTSTART:19701025T030000", "TZOFFSETFROM:+0200", "TZOFFSETTO:+0100",
       "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU", "END:STANDARD", "END:VTIMEZONE"]
for d, h, i, t, f, e in PUB:
    ds = d.replace("-", "") + "T" + h.replace(":", "") + "00"
    hh, mm = map(int, h.split(":"))
    end = f"{d.replace('-', '')}T{(hh + (mm + 30) // 60):02d}{(mm + 30) % 60:02d}00"
    ics += ["BEGIN:VEVENT", f"UID:{i}-mapaabierto-2026", "DTSTAMP:20261116T120000Z", f"DTSTART;TZID=Europe/Madrid:{ds}", f"DTEND;TZID=Europe/Madrid:{end}",
            f"SUMMARY:Publicar {i} ({f}) · {t[:60]}", f"DESCRIPTION:{e}", "BEGIN:VALARM", "TRIGGER:-PT60M", "ACTION:DISPLAY", "DESCRIPTION:Publicar en 1 hora",
            "END:VALARM", "END:VEVENT"]
ics += ["BEGIN:VEVENT", "UID:lanzamiento-gta6-mapaabierto", "DTSTAMP:20261116T120000Z", "DTSTART;TZID=Europe/Madrid:20261119T000000",
        "DTEND;TZID=Europe/Madrid:20261119T030000", "SUMMARY:🔓 Desbloqueo GTA 6 · grabar sesión 1 (V08)", "END:VEVENT", "END:VCALENDAR"]
open(os.path.join(OUT, "calendario_publicacion.ics"), "w").write("\r\n".join(ics) + "\r\n")
print("calendario ok")
