#!/usr/bin/env python3

import http.server
import socketserver
import requests

PORT = 3000

METHOD_GET = 'GET'
METHOD_POST = 'POST'
METHOD_PUT = 'PUT'

class Handler(http.server.BaseHTTPRequestHandler):
  def _handle_request(self, method):
    print('------------------')
    print(method)
    print(self.path)
    print(self.headers)

    if method == METHOD_GET:
      result = requests.get(f'https://kubernetes.default.svc{self.path}', headers={
        'Authorization': self.headers['authorization']
      }, verify=False)

      print('==================')
      print(result.text)
      print(result.status_code)

      self.send_response(code=result.status_code)
      self.end_headers()

      self.wfile.write(result.text.encode())
  
  def do_GET(self):
    self._handle_request(METHOD_GET)
  
  def do_PUT(self):
    self._handle_request(METHOD_PUT)
  
  def do_POST(self):
    self._handle_request(METHOD_POST)


with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'serving at port: {PORT}')
    httpd.serve_forever()
