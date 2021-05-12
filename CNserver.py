from time import *
import socket as s
import sys

server_socket = s.socket()
h_name = s.gethostname()
print("The hostname is:", h_name)
print("   ")
ip = s.gethostbyname(h_name)
port = 8080
server_socket.bind((h_name, port))
print("*******Binding between host and port successful******")
print("   ")
print("Your IP address: ", ip)
print("       ")
 
name = input('Enter your name: ')
 
server_socket.listen(2) 
c, a = server_socket.accept()
 
print("Received connection from ", a[0])
print('Connection done. Connected from: ',a[0])
 
client = (c.recv(1024)).decode()
print(client + ' has connected.')
 
c.send(name.encode())
while True:
    message = input('Me : ')
    c.send(message.encode())
    message = c.recv(1024)
    message = message.decode()
    print(client, ':', message)