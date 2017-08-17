#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os


# host to listen on 
host = '192.168.11.247'

# create raw socket and bind it to public interface
if os.name == 'nt':
    socket_protocal = socket.IPPROTO_TP
else:
    socket_protocal = socket.IPPROTO_TCP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocal)

sniffer.bind((host, 0))

# include ip headers in capture
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# send IOCTL to set up promiscuous mode on windows
if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# read a single packet
print(sniffer.recvfrom(65565))

# turn off promiscous mode if on windows
if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
