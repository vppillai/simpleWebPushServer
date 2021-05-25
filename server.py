from http.server import HTTPServer, BaseHTTPRequestHandler,SimpleHTTPRequestHandler,CGIHTTPRequestHandler
import ssl
import logging

port = 4443

httpd = HTTPServer(('0.0.0.0', port), CGIHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile="ECC_prime256v1.cer", keyfile="ECC_prime256v1.key", server_side=True)

print("Server running on https://0.0.0.0:" + str(port))

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.socket.close()
