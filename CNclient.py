import time
import socket as s
import sys
 
client_socket = s.socket()
server_host = s.gethostname()
ip = s.gethostbyname(server_host)
port = 8080
 
print('This is your IP address: ',ip)
server_host = input('Enter IP address of other person:')
name = input('Enter name: ')
 
 
client_socket.connect((server_host, port))
 
client_socket.send(name.encode())
server_name = client_socket.recv(1024)
server_name = server_name.decode()
 
print(server_name,' joined.......')
while True:
    message = (client_socket.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    client_socket.send(message.encode())  
