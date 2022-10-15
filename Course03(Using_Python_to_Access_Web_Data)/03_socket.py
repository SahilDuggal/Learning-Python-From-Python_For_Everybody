# Introduction to nectworking ------- Book for Network Architecture.
  
# COMMON TCP PORTS:- ..................
# Telnet (LOGIN) --> Port 23
# SSH (Secure LOGIN) --> Port 22
# HTTP (Web Server) --> Port 80
# HTTPS (Secure Web Server) --> Port 443
# SMTP (Mail) --> Port 25
# IMAP (Mail Retrieval) --> Port (143/220/993)
# POP (Mail Retrieval) --> Port (109/110)
# DNS (Domain Name) --> Port 53
# FTP (File Transfer) --> Port 21
# (Commonly these are the ports, they can be on different ports as well.)

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect( ("data.pr4e.org", 80) )
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n' .encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysocket.close()

