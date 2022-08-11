# Python 3 server example
import http.server as server
import os
import webbrowser
hostName = "localhost"
serverPort = 8000

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = "docs/" + self.path[1:]
        if os.path.isfile(path):
            self.send_response(200)
            self.send_header("Content-type", self.guess_type(path))
            self.end_headers()
            f = open(path, 'rb')
            if f:
                try:
                    self.copyfile(f, self.wfile)
                finally:
                    f.close()
        elif os.path.isfile(path + ".html"):
            self.send_response(200)
            self.send_header("Content-type", self.guess_type(path  + ".html"))
            self.end_headers()
            f = open(path  + ".html", 'rb')
            if f:
                try:
                    self.copyfile(f, self.wfile)
                finally:
                    f.close()
        elif os.path.isdir(path):
            self.send_response(200)
            self.send_header("Content-type", self.guess_type(path  + "/index.html"))
            self.end_headers()
            f = open(path  + "/index.html", 'rb')
            if f:
                try:
                    self.copyfile(f, self.wfile)
                finally:
                    f.close()
        elif os.path.isfile("docs/404.html"):
            self.send_response(200)
            self.send_header("Content-type", self.guess_type("docs/404.html"))
            self.end_headers()
            f = open("docs/404.html", 'rb')
            if f:
                try:
                    self.copyfile(f, self.wfile)
                finally:
                    f.close()
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers() 
            self.wfile.write(bytes(path + " does not exist", "latin-1"))

if __name__ == '__main__':
    server.test(HandlerClass=HTTPRequestHandler)