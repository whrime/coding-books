#!/usr/bin/env python

from socket import *

HOST = 'www.cnblogs.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)  #接收到的缓存内容
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
