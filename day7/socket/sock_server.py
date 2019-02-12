#!/usr/bin/python
# -*-coding:utf-8-*-

import socket
import subprocess

ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

'''
windows version
 
while True:
    print('server is weating....')
    conn,addr = sk.accept()

    clist_date =  conn.recv(1024)
    print(str(clist_date,'utf8'))
    #conn.sendall(bytes,('不要回答，不要回答，不要回答','utf8'))
    conn.sendall(bytes('不要回答，不要回答','utf8'))
    while True:
        try:
            clist_date == conn.recv(1024)
            print(str(clist_date,'utf8'))
        except Exception:
            print('client closed ,break')
            break
        conn.send(clist_date)
    conn.close()

'''

#linux version
while True:
    print('server wating .....')
    conn,addr = sk.accept()

    client_date = conn.recv(1024)
    print(str(client_date,'utf8'))
    conn.sendall(bytes('不要回答，不要回答，不要回答','utf8'))
    while True:
        client_date = conn.recv(1024)
        print('recv:',str(client_date,'utf8'))
        if not client_date:break
        conn.send(client_date)
    conn.close()