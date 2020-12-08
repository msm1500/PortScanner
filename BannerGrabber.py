import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))

def main():
    ip = input("please enter the ip: ")
    port = str(input("please enter the port: "))
    banner(ip, port)

main()
#192.168.178.73
