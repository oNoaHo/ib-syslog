#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1514        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        s.connect((HOST, PORT))
        send_data = input("Type some text to send => ")
        s.sendall(b''+send_data.encode('utf-8'))
        # print("\n\n 1. Server sent : ", send_data, "\n\n")
        # s.sendall(b'Hello, world')
        # data = s.recv(1024)
# print('Received', repr(data))
