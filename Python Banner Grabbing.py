#!/usr/bin/python3

import socket

s = socket.socket()

ip = input("Enter the IP address: ")

port = str(input("Enter the Port: "))

s.connect((ip, int(port)))
print(s.recv(1024))