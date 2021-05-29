from re import VERBOSE
from socket import timeout
from scapy.all import *
from scapy.layers.l2 import ARP, Ether

for l in range(1,254):
    ip= "192.168.1.{}".format(l)
    arpreq= Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    arpres= srp1(arpreq, timeout=1, verbose= 0)

    if arpres:
        print(f"IP:{ip}, MAC:{arpres.hwsrc}")