from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs
from page_ops import PageOperations

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = urlparse(self.path)

        print(self.request)

        if(url.path == '/index'):
            self.page_handle(url.path)
        elif(url.path == '/login'):
            self.page_handle(url.path)
        elif(url.path == '/profile'):
            self.page_handle(url.path)
        else:
            self.send_error(HTTPStatus.INTERNAL_SERVER_ERROR)

        print(self.responses)
    
    def do_POST(self):
        pass

    def do_PUT(self):
        pass

    def do_DELETE(self):
        pass

    def do_HEAD(self):
        pass

    def page_handle(self, path):
        path = path + '.html'
        if(not PageOperations.page_exists(path)):
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        content = PageOperations.get_page(path)
        self.send_page(HTTPStatus.OK, content)

    def send_page(self, status, content):
        self.send_response(status)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(content) 