from http.server import ThreadingHTTPServer
from handler import Handler


class Server():
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self.instance = None
        
    def run(self):
        try:
            print(f'servidor escutando no endereço: {self.host} : {self.port} ...')

            self.instance = ThreadingHTTPServer((self.host, self.port), Handler)
            self.instance.serve_forever()
        except:
            print ("Ocorreu uma exceção")
        finally:
            print ("servidor foi finalizado!")
            self.instance.server_close()

if __name__ == "__main__":
    server = Server()
    server.run()
    
