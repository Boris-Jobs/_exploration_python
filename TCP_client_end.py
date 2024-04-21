# -*- coding: utf-8 -*-
"""
Created on 2024-04-21 10:07:11

@author: Boris Jobs, Chairman of FrameX Inc.

Our mission is as same as xAi's, 'Understand the Universe'.

AI that benefits all humanity is all you need.
"""

import socket

# (1) create socket object
client_socket = socket.socket()

# (2) IP addr and client port, send requests to server

ip = '127.0.0.1'
port = 8888
client_socket.connect((ip, port))

# (3) send data
for i in range(1000):
    client_socket.send(f'We sent the data {i} by utf-8 \n'.encode('utf-8'))

# (4) close
client_socket.close()
print('done')