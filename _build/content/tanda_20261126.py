"""V94 · NOTICIAS: la filtración de CyberLeek y los ports de GTA 6 a PC (pedido por el propietario el 26/11).
Solo noticia: no se muestra nada filtrado ni se dice dónde está. Datos en 2+ fuentes:
- CyberLeek publicó el ejecutable de una versión filtrada de Xbox (LevelUp, Kotaku, Notebookcheck, XDA, TweakTown).
- Modders intentan convertirla en un port de PC (Kotaku, XDA, LevelUp).
- El Discord de Project Leonida y otros proyectos de port se han cerrado; varios medios lo atribuyen a Rockstar
  (LevelUp, Dexerto, Screen Rant, Decrypt); Rockstar no lo ha comentado en público (Notebookcheck).
- Take-Two pidió en agosto a Discord y Microsoft datos para identificar a CyberLeek (Notebookcheck, PC Gamer, Hypebeast).
- Rockstar no ha anunciado versión de PC (PC Gamer, Sportskeeda, Beebom; ver V91).
NO SE AFIRMA: que el port arranque o sea jugable (las fuentes no coinciden)."""
from content.common import S
from content.shorts3 import mk
from content.rk_pool import mezcla

PIE = "\n\nNo se muestra ningún material filtrado: imágenes y vídeo © Rockstar Games (material oficial de su web de descargas, incluido el Extended Look), con fines informativos. La voz está generada con IA. Mapa Abierto es un canal no oficial."


def M(clips, t, r, items=None, sfx=None):
    return dict(S("GRAFICO", t, rotulo=r, items=items or [], **({"sfx": sfx} if sfx else {})), clips=clips)


def G(t, r, items=None, sfx=None, **kw):
    return dict(S("GRAFICO", t, rotulo=r, items=items or [], **({"sfx": sfx} if sfx else {})), **kw)


def oficial(v, fuentes):
    v["seo"]["descripcion"] = v["seo"]["descripcion"].split("\n\nVídeo realizado")[0] + "\n\nFuentes: " + fuentes + PIE
    v["oficial"] = True
    return v


V94 = oficial(mk("V94", "Filtracion_PC", "NOTICIAS", "La filtración de GTA 6 y los ports a PC",
    ["GTA 6 en PC por una filtración: lo que ha pasado", "La filtración de CyberLeek y GTA 6 en PC", "¿GTA 6 en PC por la filtración? Esto es lo que hay", "Rockstar contra los ports de GTA 6 a PC", "GTA 6 filtrado para PC: la verdad"],
    [M(mezcla("persecucion", "noche", n=3), "¿Se puede jugar GTA 6 en PC gracias a una filtración? Esto es lo que ha pasado.", "¿GTA 6 EN PC?", sfx="Golpe"),
     G("El grupo que lleva meses filtrando GTA 6, conocido como CyberLeek, ha publicado archivos de una versión filtrada de Xbox.", "LA FILTRACIÓN", items=["Versión de Xbox filtrada", "Sin nada oficial"]),
     G("Con eso, algunos modders empezaron a intentar convertirla en una versión de PC no oficial.", "PORTS NO OFICIALES"),
     M(mezcla("persecucion", n=2), "Pero varios de esos proyectos ya se han cerrado. Según varios medios, por presión de Rockstar, que no lo ha comentado en público.", "PROYECTOS CERRADOS", items=["Según varios medios", "Rockstar no comenta"]),
     G("Y ojo: no hay GTA 6 oficial para PC. Descargar una copia pirateada es ilegal y te la juegas.", "SIN PC OFICIAL", items=["Solo PS5 y Xbox Series", "Lo pirateado es ilegal"]),
     M(mezcla("atardecer", "aire", n=2), "¿Esperarás a la versión oficial de PC? Te leo.", "¿ESPERAS?", sfx="Sting")],
    dict(texto=["FILTRACIÓN", "EN PC"], sub="GTA 6", estilo="stamp", concepto="Noticia."),
    "CyberLeek, el grupo detrás de varias filtraciones de GTA 6, ha publicado archivos de una versión filtrada de Xbox, y algunos modders empezaron a intentar convertirla en una versión de PC no oficial. Varios de esos proyectos se han cerrado; distintos medios lo atribuyen a Rockstar, que no lo ha comentado en público. Rockstar no ha anunciado GTA 6 para PC: hoy solo está en PS5 y Xbox Series X|S, y descargar copias pirateadas es ilegal.",
    ["GTA 6 filtración", "GTA 6 PC", "CyberLeek GTA 6"], "📌 ¿Esperarás a la versión oficial de PC? 👇",
    objetivo="Noticia de la semana pedida por el propietario; búsquedas 'gta 6 pc' y 'filtración gta 6'."),
    "Kotaku, LevelUp, Notebookcheck, XDA Developers, Dexerto, Decrypt.")

SHORTS = [V94]
SCHED = []
