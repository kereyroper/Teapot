import BaseHTTPServer
from mimetypes import types_map
import os


HOST_NAME = ""
PORT_NUMBER = 8080


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()

	def do_GET(s):
		if s.path == "/":
			s.path = "/index.html"
		ext = os.path.splitext(s.path)[1]
		try:
			f = open(s.path[1:])
		except IOError:
			s.send_response(404)
			s.end_headers()
			return
		s.send_response(200)
		s.send_header('Content-type', types_map[ext])
		s.end_headers()
		s.wfile.write(f.read())
		f.close()

	def do_POST(s):
		s.do_BREW()

	def do_BREW(s):
		s.send_response(418)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		f = open("teapot.html")
		s.wfile.write(f.read())
		f.close()


if __name__ == '__main__':
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
