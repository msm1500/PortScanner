

import nmap

scanner = nmap.PortScanner()

print("Wilcome to my first port scanner")
print("...............................")

ip_addr = input("please enter the ip address: ")
print("The ip that you entered is: ", ip_addr)
type(ip_addr)

resp = input(" Please choose scan option")
