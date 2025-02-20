#!/usr/bin/python3
"""Module for RequestHandler class"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):
    """a simple HTTP server"""
    def send_text(self, data, status=200):
        """Helper function to send plain text responses"""
        self.send_response(status)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

    def send_json(self, data, status=200):
        """Helper function to send JSON responses"""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        """method to handle GET requests"""
        if self.path == '/':
            self.send_text("Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == '/status':
            self.send_text("OK")
        elif self.path == '/info':
            self.send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
                })
        else:
            self.send_text("Endpoint not found", 404)


if __name__ == "__main__":
    server_address = ("localhost", 8000)
    server = HTTPServer(server_address, RequestHandler)
    print("serving at http://{}:{}".format(*server_address))
    server.serve_forever()
