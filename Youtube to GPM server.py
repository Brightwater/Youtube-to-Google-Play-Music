# Jeremiah Spears
# Youtube to GPM server
#
# This python script is a simple server that listens for
# post messages sent from the Chrome extension
# It receives the youtube link to download and
# stores it in a file
# It then starts the Youtube to GPM process

import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import subprocess
import os
import sys

class HandleRequests(BaseHTTPRequestHandler):
	def _set_response(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		self._set_response()
		self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
		post_data = self.rfile.read(content_length)  # <--- Gets the data itself
		self._set_response()
		self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
		msg = post_data.decode('utf-8')

		file = open("link.txt", "w")
		print(msg)
		file.write(msg)
		file.close()

		path = os.path.dirname(os.path.realpath(__file__))
		subprocess.Popen(path + "\Youtube to GPM.exe",
						 creationflags=subprocess.CREATE_NEW_CONSOLE)

port = 8000

handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", port), HandleRequests)

print (f"serving at {port}")
httpd.serve_forever()

