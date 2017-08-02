#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = 'www.google.com'
port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
client.connect((host, port))

# send some data
client.send('GET /HTTP/1.1\r\nHost: google.com\r\n\r\n')

# recieve data
response = client.recv(4096)
print(response)
