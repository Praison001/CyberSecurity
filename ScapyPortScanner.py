from socket import timeout
from scapy.all import *
from scapy.layers.inet import *
import random

target = "IP"
for dp in range(0,100):
    sp = random.randint(1, 65534)
    res= sr1(IP(dst=target)/TCP(sport=sp,dport=dp, flags="S"), timeout=1, verbose=0)
    if(res.haslayer(TCP)):
        if(res.getlayer(TCP).flags == 0x12):
            close_connection = sr(IP(dst=target)/TCP(sport=sp, dport=dp, flags="R"), timeout=1, verbose=0)
            print(f"port {dp} is open.")