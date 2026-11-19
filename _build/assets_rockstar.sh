#!/usr/bin/env bash
# Descarga el material oficial de prensa de Rockstar (capturas + tráiler de lanzamiento) a $MA_RK.
# Hosts necesarios en el entorno: media-rockstargames-com.akamaized.net (ya permitido).
set -euo pipefail
RK="${MA_RK:-/tmp/claude-0/rk_dl}"; B="https://media-rockstargames-com.akamaized.net/VI/downloads"
mkdir -p "$RK"; cd "$RK"
[ -f GTAVI_Launch_Trailer.mp4 ] || curl -fsSL -o GTAVI_Launch_Trailer.mp4 "$B/videos/GTAVI_Launch_Trailer/GTAVI_Launch_Trailer.mp4"
if [ ! -d x_GTAVI_Screenshots ]; then curl -fsSL -o s.zip "$B/screenshots/GTAVI_Screenshots.zip"; mkdir -p x_GTAVI_Screenshots; unzip -q s.zip -d x_GTAVI_Screenshots; rm s.zip; fi
if [ ! -d x_GTAVI_Videos ]; then curl -fsSL -o v.zip "$B/videos/GTAVI_Videos.zip"; mkdir -p x_GTAVI_Videos; unzip -q v.zip -d x_GTAVI_Videos; rm v.zip; fi
echo "OK: $RK"
# Relay local para extraer fragmentos del Extended Look (27 min de juego real, 14 GB) sin descargarlo entero.
if ! curl -s -o /dev/null -r 0-1 http://127.0.0.1:8765/GTAVI_An_Extended_Look/GTAVI_An_Extended_Look.mp4; then
  (cd "$(dirname "$0")" && nohup python3 rk_relay.py 8765 >/tmp/rk_relay.log 2>&1 &); sleep 2
fi
echo "Relay Extended Look: http://127.0.0.1:8765"
