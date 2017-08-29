import socket
import requests
import json
from nose.tools import *

class Server:
	"""docstring for ClassName"""
	def __init__(self, port = 9100):
		self.host = '127.0.0.1'
		self.port = port
		self.www_dir = 'www'
	def activate_server(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.host, self.port))
		self.socket.listen(1)
		self._wait_for_connections()

	def _gen_headers(self, code):
		h = ' '
		if (code == 200):
			h = 'HTTP/1.1 200 OK'
		elif(code == 404):
			h = 'HTTP/1.1 404 Not Found'
		return h

	def _wait_for_connections(self):
		while True:
			conn, addr = self.socket.accept()
			data = conn.recv(1024)
			string = bytes.decode(data)
			request_method = string.split(' ')[0]
			print("Method: ", request_method)
			print("Request body: ", string)
			if (request_method == 'GET') | (request_method == 'HEAD'):
				file_requested = string.split(' ')
				file_requested = file_requested[1]
				file_requested = file_requested.split('?')[0]
				if (file_requested == '/'):
					file_requested = '/index.html'
				file_requested = 'c:/Sites/Taller1/documentRoot'+file_requested
				try:
					file_handler = open(file_requested,'rb')
					if (request_method == 'GET'):
						response_content = file_handler.read()
						status_header = self._gen_headers(200)
						print(response_content)
						print(status_header)
					else:
						status_header = self._gen_headers(404)
						print(status_header)
					file_handler.close()
				except Exception, e:
					raise
				else:
					pass
				finally:
					pass
			response_headers = self._gen_headers(200)
			conn.sendall(response_headers)
			conn.close()



print("Servidor HTTP")
s = Server(9100)
s.activate_server()

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.bind(('127.0.0.1', 9100))
#s.listen(1)

#while True:
#    client_connection, client_address = s.accept()
#    request = client_connection.recv(1024)
#    print(response.status_code)
#    client_connection.sendall("HTTP/1.1 200 OK")
#    client_connection.close()
    
    

