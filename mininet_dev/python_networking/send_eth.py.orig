<<<<<<< HEAD
from socket import *

def send_ether(src, dst, type, payload, interface="eth0"):
  # 48-bit Ethernet addresses
  assert(len(src) == len(dst) == 6)

  # 16-bit Ethernet type
  assert(len(type) == 2) # 16-bit Ethernet type

  s = socket(AF_PACKET, SOCK_RAW)
  s.bind((interface, 0))
  return s.send(dst + src + type + payload)

  
=======
from scapy.all import *
from COPE_packet_classes import *

pkt = Ether(dst="12:23:34:45:56:67", type=0x7123)/COPE_packet()/"HelloWorld"

pkt.show2()


sendp(pkt, iface="h1-eth0")
>>>>>>> 14d454b270b1ee84d36bfc36c0feaba14a88cffc
