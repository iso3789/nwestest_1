#!/usr/bin/env python3

#Dzido Ivan

import socket

HOST = ''
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Fehlermeldung verhindern
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            outdata = "HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hi BULME</h1></body></html>" + str (addr)
            antwort = outdata.encode()
            print("Serverantwort:", antwort, "an", addr)
            conn.sendall(antwort)
            conn.close()