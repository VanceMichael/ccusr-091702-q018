import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

SERVICE_NAME = "student_custody"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        payload = json.dumps({"status": "ok", "service": SERVICE_NAME}, ensure_ascii=False).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        return

def create_server(host=None, port=None):
    return ThreadingHTTPServer((host or os.getenv("HOST", "0.0.0.0"), int(port if port is not None else os.getenv("PORT", "8080"))), Handler)

if __name__ == "__main__":
    create_server().serve_forever()