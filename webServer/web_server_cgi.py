from wsgiref.simple_server import make_server
from  application import app

httpd = make_server('0.0.0.0', 8000, app)
print("serving at port", httpd.server_port)
httpd.serve_forever()