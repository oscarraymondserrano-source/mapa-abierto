"""Estructuras comunes de contenido: estilos visuales (looks) para prompts de Pika y helper de escenas."""

# Estilo global del proyecto para TODOS los clips IA (coherencia visual)
STYLE = ("Photorealistic cinematic look, shot on 35mm anamorphic, subtle film grain, rich teal-and-magenta "
         "color grade with warm orange sunset highlights, shallow depth of field. No text, no captions, no logos, "
         "no brand names, no video game HUD, no recognizable real people or video game characters, "
         "anatomically correct hands and faces.")

NEGATIVE = ("text, letters, watermark, logo, HUD, minimap, deformed hands, extra fingers, distorted faces, "
            "warped cars, melting buildings, flicker, low resolution, cartoon")

# Cada look: sujeto, entorno, ángulo, movimiento, luz, atmósfera, composición, animación
LOOKS = {
    "drone_ciudad": dict(
        subject="a sprawling coastal Florida-style metropolis with art deco hotels and glass skyscrapers",
        env="oceanfront boulevard lined with palm trees, turquoise sea on one side",
        angle="high aerial drone shot", move="slow forward glide with gentle descending tilt",
        light="golden hour sunset, low sun flaring between towers, neon signs starting to glow",
        atmo="warm, glamorous, humid haze", comp="rule of thirds, coastline leading line from bottom left to top right",
        anim="traffic flowing on the boulevard, palm fronds swaying, waves rolling onto the beach"),
    "calle_neon": dict(
        subject="a wet nighttime street with pastel art deco buildings and glowing pink and cyan neon signs (no readable text)",
        env="tropical city at night after rain, puddles reflecting neon",
        angle="low angle at street level", move="slow dolly forward",
        light="neon magenta and cyan practical lights, deep blue night ambience",
        atmo="moody, electric, cinematic", comp="symmetrical one-point perspective down the street",
        anim="a classic convertible passes through frame, reflections ripple in puddles, light steam rises"),
    "reloj_neon": dict(
        subject="a retro digital alarm clock showing glowing segments (no readable numbers) on a bedside table",
        env="dark bedroom lit by a window with a neon city skyline at night",
        angle="close-up at table level", move="very slow push-in",
        light="magenta and cyan neon light spilling through blinds, venetian blind shadows",
        atmo="anticipation, late night, quiet tension", comp="clock in the right third, blurred skyline background",
        anim="blind shadows slowly drift, the clock segments pulse softly"),
    "consola_salon": dict(
        subject="a modern living room gaming setup with a large TV showing an abstract blue loading progress bar (no text, no logos)",
        env="cozy apartment at night, window overlooking a neon-lit coastal city",
        angle="medium wide shot from behind a sofa", move="slow lateral slide from left to right",
        light="cool TV glow mixed with warm lamp light and pink neon from the window",
        atmo="excited anticipation, late night", comp="TV centered, sofa silhouette in foreground",
        anim="progress bar slowly filling, city lights twinkling outside"),
    "almacenamiento": dict(
        subject="a close-up of a sleek internal NVMe SSD with glowing cyan circuitry traces",
        env="dark tech studio surface with subtle reflections",
        angle="macro close-up, 30 degree angle", move="slow orbit around the drive",
        light="cyan rim light and magenta back light, dark background",
        atmo="clean, technical, premium", comp="drive diagonal across frame, shallow focus",
        anim="light pulses travel along the circuit traces"),
    "puente_cayos": dict(
        subject="a very long two-lane bridge crossing turquoise ocean between small tropical islands",
        env="Florida Keys style archipelago with mangroves and white sand",
        angle="high aerial drone shot", move="smooth tracking shot following a convertible car crossing the bridge",
        light="late afternoon sun, sparkling water, soft pink clouds",
        atmo="freedom, open road, vacation", comp="bridge as a strong leading line to the horizon",
        anim="car moving across the bridge, gentle waves, seabirds gliding"),
    "pantano": dict(
        subject="an airboat gliding across a vast sawgrass swamp",
        env="Everglades-like wetlands with cypress trees and still water, an alligator partially submerged",
        angle="low angle just above the water surface", move="fast forward tracking behind the airboat",
        light="hazy sunrise, orange sun through mist",
        atmo="wild, humid, untamed", comp="airboat in the center, wake lines leading the eye",
        anim="water spraying, grass bending in the wind, birds taking off"),
    "puerto": dict(
        subject="an aging industrial port town with cranes, rusty warehouses and a retro roadside motel",
        env="Gulf coast shoreline, cloudy sky",
        angle="wide establishing shot from a hill", move="slow pan from left to right",
        light="overcast dusk with a stripe of orange light on the horizon, flickering motel sign glow (no readable text)",
        atmo="melancholic, gritty, forgotten", comp="cranes on the left third, motel in the right foreground",
        anim="cranes slowly moving, seagulls, a pickup truck driving by"),
    "rural": dict(
        subject="a large sugar refinery with smokestacks beside endless sugarcane fields",
        env="flat rural Florida countryside with a two-lane highway",
        angle="wide shot from the roadside", move="slow crane up revealing the fields",
        light="hot midday sun turning into golden afternoon light, heat shimmer",
        atmo="dusty, industrial, isolated", comp="refinery on the horizon line, highway as leading line",
        anim="smoke drifting from chimneys, a group of motorcycles riding along the road"),
    "parque_natural": dict(
        subject="a forested national park with a winding river and dirt off-road trail",
        env="dense pine and oak forest with hills and a lookout point",
        angle="aerial drone shot", move="slow forward flight over the treetops",
        light="early morning sun rays through mist (volumetric light)",
        atmo="peaceful, vast, adventurous", comp="river curving through the center",
        anim="mist drifting, a 4x4 truck kicking up dust on the trail, birds flying"),
    "playa_dia": dict(
        subject="a lively beach boardwalk with lifeguard towers in pastel colors",
        env="tropical beach with palm trees and an art deco skyline in the background",
        angle="medium wide shot at eye level", move="steady gimbal walk forward",
        light="bright sunny midday, crisp shadows, blue sky",
        atmo="energetic, sunny, carefree", comp="lifeguard tower on the left third",
        anim="people silhouettes jogging and skating (non-identifiable), waves, flags in the wind"),
    "sirenas": dict(
        subject="red and blue police lights reflecting on a glossy sports car at night",
        env="empty highway overpass in a tropical city",
        angle="low angle close to the asphalt", move="handheld slow push-in with slight shake",
        light="strobing red and blue lights, deep shadows",
        atmo="tense, chase, adrenaline", comp="car in the left third, lights bokeh on the right",
        anim="lights flashing, heat haze, light rain falling"),
    "mapa_mesa": dict(
        subject="an old paper road map of a fictional tropical state spread on a desk with pins and red string (no readable text)",
        env="detective-style desk lit by a lamp",
        angle="top-down overhead shot", move="slow rotation and push-in",
        light="warm desk lamp pool of light, dark surroundings",
        atmo="investigation, curiosity, mystery", comp="map filling the frame, pins on thirds",
        anim="dust particles floating, string slightly moving"),
    "lupa_secreto": dict(
        subject="a magnifying glass revealing a tiny hidden glowing detail on a dark textured surface",
        env="dark room with neon reflections",
        angle="extreme close-up", move="slow push-in through the lens",
        light="single cyan spotlight with magenta rim light",
        atmo="mystery, discovery, curiosity", comp="lens centered, detail in the focal point",
        anim="lens slowly moves, detail sparkles softly"),
    "atardecer_coche": dict(
        subject="a vintage convertible driving along a coastal highway at sunset",
        env="palm-lined ocean road with the sea on the right",
        angle="side tracking shot from a camera car", move="parallel tracking at matching speed",
        light="huge orange sun on the horizon, magenta sky",
        atmo="nostalgic, cinematic, romantic", comp="car in the lower third, sun in the background",
        anim="hair-like palm fronds moving, sun glints, road lines passing"),
    "mando": dict(
        subject="a generic modern game controller (no brand logos) held by two hands",
        env="dark room lit by a TV screen with abstract colorful light",
        angle="over-the-shoulder close-up", move="slow push-in",
        light="TV glow in cyan and magenta on the hands",
        atmo="focus, excitement", comp="controller centered, blurred TV background",
        anim="thumbs pressing buttons, light changing on the screen"),
}


def S(tipo, texto, rotulo="", visual="", look=None, extra="", cam="", trans="Corte", sfx="", cap=None,
      items=None, nota=""):
    """Escena.
    tipo: GRAFICO (motion graphics propio), OFICIAL (material oficial de Rockstar: tráiler, capturas, arte),
          IA (clip generado con Pika, rotulado como recreación), GAMEPLAY (grabación propia tras el lanzamiento).
    texto: narración (las *palabras* entre asteriscos se destacan en subtítulos).
    """
    return dict(tipo=tipo, texto=texto, rotulo=rotulo, visual=visual, look=look, extra=extra, cam=cam,
                trans=trans, sfx=sfx, cap=cap, items=items or [], nota=nota)
