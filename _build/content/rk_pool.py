"""Biblioteca de planos oficiales de Rockstar por tema, para montar escenas con cortes rápidos.
Cada plano: (fuente, segundo, velocidad, encuadre_x). Fuente "EL" = Extended Look (vía relay), "OUT" = vídeo Out Now,
o un MP4 de RK_DIR. Revisados a mano el 19/11/2026 (sin logos, rótulos ni pantallas negras). OUT: el logo empieza en 21,5 s; no leer más allá de 21 s."""
POOL = {
    "conducir": [("EL", 506, 1, .4), ("EL", 512, 1, .4), ("EL", 518, 1, .45), ("EL", 524, 1, .45), ("EL", 530, 1, .4),
                 ("EL", 760, 1, .5), ("EL", 764, 1, .5), ("OUT", 19.2, 1.8, .5)],
    "persecucion": [("EL", 925, 1, .45), ("EL", 929, 1, .45), ("EL", 849, 1.2, .35), ("EL", 852, 1.2, .4)],
    "noche": [("EL", 1222, 1.4, .5), ("OUT", 19.2, 1.8, .5), ("OUT", 3.3, 1.4, .5), ("OUT", 19.9, 2.5, .5)],
    "agua": [("EL", 1030, 2.5, .5), ("EL", 1045, 2.5, .45), ("OUT", 11.3, 1.2, .5)],
    "aire": [("EL", 1133, 1, .5), ("EL", 1136, 1, .5)],
    "gente": [("EL", 1003, 1, .45), ("EL", 1006, 1, .45), ("OUT", 5.4, 1.3, .5), ("OUT", 9.2, 1.8, .45)],
    "atardecer": [("EL", 1571, 2.5, .5), ("EL", 760, 1, .5), ("EL", 763, 1, .5)],
    "club": [("OUT", 3.3, 1.4, .5), ("OUT", 19.9, 2.5, .5)],
}
_rot = {}

def mezcla(*temas, n=3):
    """Devuelve n planos distintos alternando temas, sin repetir entre llamadas mientras queden."""
    out = []
    k = 0
    while len(out) < n and k < 50:
        t = temas[k % len(temas)]
        lst = POOL[t]
        i = _rot.get(t, 0)
        p = lst[i % len(lst)]
        _rot[t] = i + 1
        if p not in out:
            out.append(p)
        k += 1
    return out
