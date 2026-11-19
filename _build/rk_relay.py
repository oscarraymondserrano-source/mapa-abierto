"""Relay HTTP local -> descargas oficiales de Rockstar (con rangos), para que ffmpeg extraiga fragmentos sin bajar el archivo entero."""
import http.server, socketserver, sys, requests
BASE = "https://media-rockstargames-com.akamaized.net/VI/downloads/videos/"
S = requests.Session()
class H(http.server.BaseHTTPRequestHandler):
    def _go(self, head=False):
        h = {k: v for k, v in self.headers.items() if k.lower() in ("range",)}
        r = (S.head if head else S.get)(BASE + self.path.lstrip("/"), headers=h, stream=True, timeout=60)
        self.send_response(r.status_code)
        for k in ("Content-Length", "Content-Range", "Content-Type", "Accept-Ranges"):
            if k in r.headers: self.send_header(k, r.headers[k])
        self.end_headers()
        if not head:
            try:
                for c in r.iter_content(1 << 16): self.wfile.write(c)
            except (BrokenPipeError, ConnectionResetError): pass
        r.close()
    def do_GET(self): self._go()
    def do_HEAD(self): self._go(True)
    def log_message(self, *a): pass
class T(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads = True
T(("127.0.0.1", int(sys.argv[1]) if len(sys.argv) > 1 else 8765), H).serve_forever()
