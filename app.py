
import os
import socketserver
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# --- Config ---
HTML_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "isl-translator.html")
PORT = 8000


class ISLHandler(BaseHTTPRequestHandler):
    """Serves the ISL translator HTML on every route."""

    def _serve_html(self):
        with open(HTML_FILE, "rb") as f:
            content = f.read()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        self._serve_html()

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def log_message(self, format, *args):
        pass  # quiet console


if __name__ == "__main__":
    if not os.path.exists(HTML_FILE):
        raise FileNotFoundError(
            f"Could not find '{os.path.basename(HTML_FILE)}'. "
            "Put this .py file in the same folder as your HTML file."
        )

    with ThreadingHTTPServer(("0.0.0.0", PORT), ISLHandler) as server:
        print("=" * 45)
        print("  ISL AI - Indian Sign Language Translator")
        print(f"  Serving: {os.path.basename(HTML_FILE)}")
        print(f"  Open in browser:  http://localhost:{PORT}")
        print("  Press Ctrl+C to stop")
        print("=" * 45)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")