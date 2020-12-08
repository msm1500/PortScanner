

import socket

cleintsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

cleintsocket.connect(('192.168.178.73', port))

message = cleintsocket.recv(1024)

cleintsocket.close() 

print(message.decode('ascii'))
