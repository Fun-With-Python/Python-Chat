#!/usr/bin/env python

from socket import *

IP = ''
PORT = 23456
ADS = (IP, PORT)

tcpsoc = socket(AF_INET, SOCK_STREAM)
tcpsoc.connect(ADS)

while 1:
	data = raw_input("msg>>")
	if not data : break
	tcpsoc.send(data)
	data = tcpsoc.recv(1024)
	if not data: break
	print data
tcpsoc.close()

