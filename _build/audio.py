"""Audio: TTS guía (Piper), música original sintetizada y efectos de sonido. Todo libre de derechos."""
import os, re, subprocess, wave, hashlib
import numpy as np

VOICE = "/tmp/claude-0/voices/voice-es-carlfm-x-low/es-carlfm-x-low.onnx"
SR = 48000

PRON = [
    (r"\bGTA\b", "ge te a"), (r"\bXbox\b", "équis box"), (r"\bM\.2\b", "eme punto dos"), (r"\bUSB\b", "u ese be"),
    (r"\bSSD\b", "ese ese de"), (r"\bHDR\b", "hache de erre"), ("79,99", "setenta y nueve con noventa y nueve"),
    ("99,99", "noventa y nueve con noventa y nueve"), (r"Vice City", "Vais Síti"), (r"\bJason\b", "Yéison"),
    (r"\bLucia\b", "Lusía"), (r"Grassrivers", "Gras Ríver"), (r"Port Gellhorn", "Port Guélhorn"), (r"Mount Kalaga", "Maunt Kalága"),
    (r"The Guardian", "de Guárdian"), (r"Love Is a Long Road", "Lov is a long roud"), (r"Hot Together", "Jot tuguéder"),
    (r"Tom Petty", "Tom Péti"), (r"The Pointer Sisters", "de Póinter Sísters"), (r"Ocean Drive", "Óushen Dráiv"),
    (r"South Beach", "Sáuz Bich"), (r"Cal Hampton", "Cal Jámpton"), (r"Boobie Ike", "Búbi Áik"), (r"Ultimate", "Últimeit"),
    (r"spoilers", "espóilers"), (r"Panhandle", "Panjándel"), (r"Everglades", "Évergleids"), (r"Chiliad", "Chíliad"),
    (r"Red Dead Redemption", "Red Ded Ridémshon"), (r"\bonline\b", "onláin"), (r"Rockstar", "Rókstar"), (r"PlayStation", "Pléisteishon"),
    (r"Series S", "Síries Ese"), (r"Series X", "Síries Équis"), (r"Series", "Síries"), (r"Duval", "Duvál"),
]


def tts_text(text):
    t = text.replace("*", "")
    t = re.sub(r"\[([^\]]*)\]", lambda m: m.group(1).lower().replace("/", ", o "), t)
    for a, b in PRON:
        t = re.sub(a, b, t)
    return t


def synth(text, out_wav, cache_dir):
    """Genera la locución guía de una escena. Devuelve duración (s)."""
    os.makedirs(cache_dir, exist_ok=True)
    t = tts_text(text)
    h = hashlib.md5(t.encode()).hexdigest()[:12]
    raw = os.path.join(cache_dir, f"{h}.wav")
    if not os.path.exists(raw):
        tmp = raw + ".tmp.wav"
        subprocess.run(["python3", "-m", "piper", "-m", VOICE, "--sentence-silence", "0.22", "--noise-scale", "0.6",
                        "-f", tmp], input=t.encode(), check=True, capture_output=True)
        # tempo 1.1 (≈155 ppm), limpieza de graves, ligera presencia, 48 kHz
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-af",
                        "silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.45:stop_silence=0.3:stop_threshold=-45dB,highpass=f=80,equalizer=f=3000:t=q:w=1.2:g=2,aresample=48000",
                        "-ac", "1", raw], check=True)
        os.remove(tmp)
    subprocess.run(["cp", raw, out_wav], check=True)
    with wave.open(out_wav) as w:
        return w.getnframes() / w.getframerate()


# ---------- MÚSICA ORIGINAL (synthwave) ----------
def _lowpass(x, cutoff):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / (1 + (f / cutoff) ** 4)
    return np.fft.irfft(X, len(x))


def _saw(freq, t):
    return 2 * ((t * freq) % 1.0) - 1


def music_bed(seconds, out_wav, bpm=96, seed=0):
    rng = np.random.default_rng(seed)
    beat = 60 / bpm
    bar = beat * 4
    # Am - F - C - G (2 compases cada uno)
    chords = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
    loop_len = bar * 8
    n = int(loop_len * SR)
    t = np.arange(n) / SR
    pad = np.zeros(n); bass = np.zeros(n); drums = np.zeros(n); arp = np.zeros(n)
    m2f = lambda m: 440 * 2 ** ((m - 69) / 12)
    for ci, ch in enumerate(chords):
        s, e = int(ci * 2 * bar * SR), int((ci + 1) * 2 * bar * SR)
        tt = t[s:e] - t[s]
        env = np.minimum(1, tt / 0.4) * np.minimum(1, (2 * bar - tt) / 0.4)
        for m in ch:
            for det in (-0.08, 0.08):
                pad[s:e] += _saw(m2f(m) * (1 + det / 100 * 12), tt) * env * 0.08
        # bajo en corcheas
        for k in range(16):
            bs = s + int(k * beat / 2 * SR); be = bs + int(beat / 2 * SR * 0.9)
            tb = np.arange(be - bs) / SR
            bass[bs:be] += np.sign(np.sin(2 * np.pi * m2f(ch[0] - 12) * tb)) * np.exp(-tb * 6) * 0.22
        # arpegio
        for k in range(32):
            a_s = s + int(k * beat / 4 * SR); a_e = a_s + int(beat / 4 * SR)
            ta = np.arange(a_e - a_s) / SR
            note = ch[k % 3] + 12
            arp[a_s:a_e] += np.sin(2 * np.pi * m2f(note) * ta) * np.exp(-ta * 14) * 0.08
    for b in range(int(loop_len / beat)):
        ks = int(b * beat * SR); tk = np.arange(int(0.25 * SR)) / SR
        kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-tk * 30)) * tk) * np.exp(-tk * 9) * 0.5
        drums[ks:ks + len(tk)] += kick[:max(0, min(len(tk), n - ks))]
        hs = ks + int(beat / 2 * SR)
        if hs < n:
            th = np.arange(int(0.05 * SR)) / SR
            hat = rng.standard_normal(len(th)) * np.exp(-th * 80) * 0.05
            drums[hs:hs + len(th)] += hat[:max(0, min(len(th), n - hs))]
        if b % 2 == 1:
            th = np.arange(int(0.2 * SR)) / SR
            snare = rng.standard_normal(len(th)) * np.exp(-th * 18) * 0.12
            drums[ks:ks + len(th)] += snare[:max(0, min(len(th), n - ks))]
    pad = _lowpass(pad, 1400); bass = _lowpass(bass, 300); drums = _lowpass(drums, 9000)
    loop = pad + bass + drums + arp
    reps = int(np.ceil(seconds / loop_len)) + 1
    full = np.tile(loop, reps)[: int(seconds * SR)]
    fade = int(2 * SR)
    full[-fade:] *= np.linspace(1, 0, fade)
    full[:int(0.5 * SR)] *= np.linspace(0, 1, int(0.5 * SR))
    full = full / (np.max(np.abs(full)) + 1e-9) * 0.8
    st = np.stack([full, np.roll(full, 240)], axis=1)  # ligera amplitud estéreo
    _write(out_wav, st)


def whoosh(out_wav, dur=0.5, seed=1):
    rng = np.random.default_rng(seed)
    n = int(dur * SR)
    noise = rng.standard_normal(n)
    env = np.sin(np.linspace(0, np.pi, n)) ** 2
    x = _lowpass(noise, 2500) * env
    x = x / np.max(np.abs(x)) * 0.6
    _write(out_wav, np.stack([x, x], 1))


def sting(out_wav, dur=2.2):
    t = np.arange(int(dur * SR)) / SR
    m2f = lambda m: 440 * 2 ** ((m - 69) / 12)
    x = np.zeros_like(t)
    for m in [57, 64, 69, 72, 76]:
        x += _saw(m2f(m), t) * 0.1
    x = _lowpass(x, 2200) * np.exp(-t * 1.6) * np.minimum(1, t / 0.02)
    kick = np.sin(2 * np.pi * (45 + 120 * np.exp(-t * 25)) * t) * np.exp(-t * 6) * 0.7
    x = x + kick
    x = x / np.max(np.abs(x)) * 0.85
    _write(out_wav, np.stack([x, x], 1))


def _write(path, st):
    st = np.clip(st, -1, 1)
    data = (st * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(data.tobytes())
