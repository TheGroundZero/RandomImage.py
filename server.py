#!/usr/bin/env python3

from http.server import HTTPServer, CGIHTTPRequestHandler

server = HTTPServer
handler = CGIHTTPRequestHandler
server_address = ("", 80)
handler.cgi_directories = ["/cgi-bin"]

httpd = HTTPServer(server_address, handler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
