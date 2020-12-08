import nmap

scanner = nmap.PortScanner()

print("Welcome to my first port scanner")
print("........................................")

ip_addr = input("please enter the ip address: ")
print("The ip that you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\n Please choose scan option:
                1)SYN Scan
                2)UDP Scan
                3)Comprehensive scan\n""")
print("Your selected option is: ",resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2': 
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '21-443', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udb'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")