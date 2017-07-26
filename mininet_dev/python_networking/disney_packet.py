from scapy.all import *

class Disney(Packet):
    name = "DisneyPacket "
    fields_desc=[ ShortField("mickey",5),
                 XByteField("minnie",3) ,
                  ]

d=Disney()
ls(d)

pkt = Ether()/IP()/UDP()/Disney()/"HelloWorld!"
ls(pkt)

sendp(pkt, iface="h1-eth0", inter=0.2, loop=1)