import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_error(404)

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 18080
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()
