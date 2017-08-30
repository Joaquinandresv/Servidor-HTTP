import socket
import requests
import json
from nose.tools import *

class Server:

	def __init__(self, port = 9100):
		self.host = '127.0.0.1'
		self.port = port

	def activate_server(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.host, self.port))
		self._connection()

	def _headers(self, code):
		h = ' '
		if (code == 200):
			h = 'HTTP/1.1 200 OK'
		elif(code == 404):
			h = 'HTTP/1.1 404 Not Found'
		return h

	def _connection(self):
		while True:
			self.socket.listen(1)
			conn, addr = self.socket.accept()
			data = conn.recv(1024)
			string = bytes.decode(data)
			request_method = string.split(' ')[0]
			print("\n*******************************************************************************")
			print("Method:", request_method)
			print("Request body: ", string)
			if (request_method == 'GET') | (request_method == 'HEAD'):
				file_requested = string.split(' ')
				file_requested = file_requested[1]
				file_requested = file_requested.split('?')[0]
				if (file_requested == '/'):
					file_requested = '/index.html'
				file_requested = "c:/Sites/Taller/documentRoot" + file_requested
				print("Pagina solicitada [",file_requested,"]")
				try:
					file_handler = open(file_requested,'rb')
					if (request_method == 'GET'):
						response_content = file_handler.read()
						print(response_content)
						print("\n")
					file_handler.close()
					response_headers = self._headers(200)
					print("HTTP/1.1 200 OK")
					print("Aqui va Json Araos")
					print("*******************************************************************************")
				except Exception, e:
					print("\nHTTP/1.1 404 Not Found")
					print("Json Araos")
					response_headers = self._headers(404)
					if (request_method == 'GET'):
						response_content = b"<html><body><p>Error 404: File not foud</p></body></html>"
				server_response = response_headers.encode()
				if(request_method == 'GET'):
					server_response += response_content
				
				conn.send(server_response)
				conn.close()
			else:
				print("Unknown HTTP request method:", request_method)
			
			



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
    
    

