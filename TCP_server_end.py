# -*- coding: utf-8 -*-
"""
Created on 2024-04-21 09:48:07

@author: Boris Jobs, Chairman of FrameX Inc.

Our mission is as same as xAi's, 'Understand the Universe'.

AI that benefits all humanity is all you need.
"""

from socket import socket, AF_INET, SOCK_STREAM

# AF_INET 用于Internet之间的进程通信
# SOCK_STREAM 表示用TCP协议编程

# (1) create a socket object
server_socket = socket(AF_INET, SOCK_STREAM)

# (2) bind IP addr and port
ip = '127.0.0.1'
port = 8888
server_socket.bind((ip, port))

# (3) listen by listen()
server_socket.listen(5)
print('server started')

# (4) wait for client to connect
client_socket, client_addr = server_socket.accept()
# 解包赋值

while True:
    # (5) receive data from client
    data = client_socket.recv(1024)
    if not data:
        break
    print('data sent from client is:', data.decode('utf-8'))

# (6) close client socket
client_socket.close()