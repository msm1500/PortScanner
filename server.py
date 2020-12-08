

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serversocket.bind(('192.168.178.73', port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    
    print("recived connection from %s " % str(address))
    
    message = 'hello! thank you for connecting to the server,,,, 2nd' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()