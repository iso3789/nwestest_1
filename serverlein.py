#!/usr/bin/env python3
import sys
import socket

HOST = ''                 
PORT = 8080              
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            #print('Connected by', addr)
            outdata = "HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hi BULME</h1></body></html>"
            print(outdata)
            conn.sendall(outdata)
