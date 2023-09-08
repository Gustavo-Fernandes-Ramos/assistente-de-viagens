from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs
import os

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = urlparse(self.path)

        print(f'ele está chegando até aqui: {url.path}')

        if(url.path == '/index.html'):
            self.page_handle(url.path)
        elif(url.path == '/login.html'):
            self.page_handle(url.path)
        elif(url.path == '/profile.html'):
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

    def page_handle(self, file):
        if(PageOperations.file_exists(file)):
            content = PageOperations.get_file(file)
            self.send_page(HTTPStatus.OK, content)
        else:
            print('erro no meu codigo')
            self.send_error(HTTPStatus.NOT_FOUND)

    def send_page(self, status, content):
        self.send_response(status)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(content) 

class PageOperations():

    def file_exists(file):
        return os.path.exists(file)

    def get_file(file):
        try:
            file = open(file[1:])
            content = file.read().encode('utf-8')
            file.close()
            return content
        except IOError:
            return None