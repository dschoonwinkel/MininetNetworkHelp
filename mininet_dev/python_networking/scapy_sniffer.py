from scapy.all import *

import sys

filter = sys.argv[1]

def Responder():

    def getPacket(pkt):
        if Raw in pkt:  print pkt[Raw]

    return getPacket

sniff(filter=filter, prn=Responder())