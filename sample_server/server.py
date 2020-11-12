import http.server, ssl

server_address = ('localhost', 8443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               keyfile='https/localhost/localhost-key.pem',
                              #  certfile='https/localhost/localhost.pem',
                               certfile='https/localhost-chain.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()
