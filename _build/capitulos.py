"""Genera los capítulos de YouTube (00:00 Título) a partir del guion renderizado de un vídeo largo."""
import re, sys, glob, os
def capitulos(carpeta):
    g = glob.glob(os.path.join(os.path.dirname(__file__), "..", carpeta, "Guion", "*.md"))[0]
    txt = open(g, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"### (.+?)\n+\*\*\[(\d+:\d+)[.\d]*\]", txt):
        out.append(f"{m.group(2)} {m.group(1)}")
    if out and not out[0].startswith("00:00"):
        out[0] = "00:00 " + out[0].split(" ", 1)[1]
    return "\n".join(out)
if __name__ == "__main__":
    print(capitulos(sys.argv[1]))
