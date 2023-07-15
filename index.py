import http.server


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Jesus Serrano", "utf-8"))

server = http.server.HTTPServer(('0.0.0.0', 5000), MyHandler)


server.serve_forever()