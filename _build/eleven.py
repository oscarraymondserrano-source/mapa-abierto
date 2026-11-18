"""Locución con ElevenLabs (voz Nico - History & Documentary, castellano peninsular).
La clave NO está en el código: el SDK lee ELEVENLABS_API_KEY del entorno."""
import os, re, hashlib, subprocess, wave
from elevenlabs import ElevenLabs, VoiceSettings

VOICE_ID = "FXn3GKRRt9FCEyTbrkaL"  # Nico - History & Documentary
MODEL_ID = "eleven_v4"
TEMPO = float(os.environ.get("MA_TEMPO", "1.0"))  # ajuste de ritmo en postproducción (v4 no admite 'speed')
CACHE = "/tmp/claude-0/eleven_cache"
_client = None


def client():
    global _client
    if _client is None:
        _client = ElevenLabs()
    return _client


def clean(text):
    t = text.replace("*", "")
    t = re.sub(r"\[([^\]]*)\]", lambda m: m.group(1).lower(), t)
    return t


def synth(text, out_wav, prev_text=None, next_text=None):
    """Genera la locución de una escena y devuelve su duración en segundos."""
    os.makedirs(CACHE, exist_ok=True)
    t = clean(text)
    key = hashlib.md5(f"{VOICE_ID}|{MODEL_ID}|{t}|{prev_text}|{next_text}".encode()).hexdigest()[:16]
    mp3 = os.path.join(CACHE, key + ".mp3")
    if not os.path.exists(mp3):
        kw = dict(text=t, voice_id=VOICE_ID, model_id=MODEL_ID, language_code="es", output_format="mp3_44100_128",
                  voice_settings=VoiceSettings(stability=0.5, similarity_boost=0.75))
        if prev_text:
            kw["previous_text"] = clean(prev_text)
        if next_text:
            kw["next_text"] = clean(next_text)
        audio = client().text_to_speech.convert(**kw)
        with open(mp3 + ".part", "wb") as f:
            for chunk in audio:
                f.write(chunk)
        os.replace(mp3 + ".part", mp3)
    af = ("silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
          + (f"atempo={TEMPO}," if abs(TEMPO - 1) > 1e-3 else "") + "aresample=48000")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-af", af, "-ac", "1", out_wav], check=True)
    with wave.open(out_wav) as w:
        return w.getnframes() / w.getframerate()
