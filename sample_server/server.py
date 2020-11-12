import http.server, ssl

# https://github.com/cloudflare/cfssl
# https://medium.com/@brendankamp757/setting-up-local-tls-on-mac-using-cloudflares-cfssl-b905a7bcf3e0
# https://medium.com/@brendankamp757/using-intermediate-certificates-on-localhost-for-mac-f4e310caa5bb

server_address = ('localhost', 8443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               keyfile='https/localhost/localhost-key.pem',
                              #  certfile='https/localhost/localhost.pem',
                               certfile='https/localhost-chain.pem',
                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()
