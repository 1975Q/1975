#!/usr/bin/python
  
import socket 

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip = "31.13.69.35"

port = 443

if sock.connect_ex((ip , port))== 0:
  print ("port 443 is open")
else:
  print ("port 443 is closed")

