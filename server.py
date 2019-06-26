#!/usr/bin/env python3

from http.server import HTTPServer, CGIHTTPRequestHandler


class MyCGIHTTPRequestHandler(CGIHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        CGIHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Content-Type", "text/html")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")


def main():
    handler = MyCGIHTTPRequestHandler
    handler.cgi_directories = ["/cgi-bin"]

    httpd = HTTPServer(("", 80), handler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()


if __name__ == "__main__":
    main()
