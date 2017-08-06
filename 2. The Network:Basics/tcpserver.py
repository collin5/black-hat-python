#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading

bind_ip = '0.0.0.0'
port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, port))
server.listen(5)

print("[*] Server listening  on {}:{}".format(bind_ip, port))

def handle(client_socket):
    request = client_socket.recv(1024)
    print("[*] Recieved {} ".format(request))

    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print("[*] Accepted connection from {}:{}".format(addr[0], addr[1]))

    handler = threading.Thread(target=handle, args=(client,))
    handler.start()
    


