#import nmap
import os

#getting ip address
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_addr = s.getsockname()[0]
print(ip_addr)    #shows your ip address in the current network
ip = list(ip_addr.split("."))
ip.pop()
new_ip = ".".join(ip)
final= new_ip + ".1/24"

#scan phase
os.system("nmap -T4 -p- -A "+ final) #scans for every ports of devices in the network and gives all possible info
s.close()