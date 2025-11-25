from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
def start():
    web_dir = 'molecules/html'
    os.chdir(web_dir)  

    PORT = 8000
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    print(f"Serving HTTP on port {PORT} from {web_dir}...")
    httpd.serve_forever()