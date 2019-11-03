from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print (self.path)
        self.send_response(200)
        self.end_headers()
        try:
            with open('{0}'.format(self.path[1:] ), 'r') as f:
                data = f.read()
                self.wfile.write( "{0}".format(data).encode() )
        except Exception as e:
            self.wfile.write( str(e).encode() )

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        print ("Received: {0}".format(body))
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()