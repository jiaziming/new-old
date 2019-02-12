#!/usr/bin/python
# -*-coding:utf-8-*-

import socketserver

class Mytcphanele(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            print('New conn:',self.client_address)
            data = self.request.recv(1024)
            if not data:break
            print('client says:',data.decode())
            self.request.send(data)


if __name__ == "__main__":
    HOST,POST = 'localhost',50007

    server = socketserver.ThreadingTCPServer((HOST,POST),Mytcphanele)

    server.serve_forever()