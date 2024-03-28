from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # Set index.html as default home page

        # Get the file extension
        _, file_extension = os.path.splitext(self.path)

        # Define content types for different file extensions
        content_types = {
            '.html': 'text/html',
            '.htm': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.jpg': 'image/jpeg',
            '.jfif':'image/jfif',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif'
        }

        # Set the Content-Type header based on the file extension
        if file_extension in content_types:
            self.send_response(200)
            self.send_header('Content-type', content_types[file_extension])
            self.end_headers()
        else:
            # If the file extension is not recognized, send a 404 response
            self.send_error(404, 'File Not Found: {}'.format(self.path))
            return

        # Serve the requested file
        return super().do_GET()

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost:{}'.format(port))
    httpd.serve_forever()


