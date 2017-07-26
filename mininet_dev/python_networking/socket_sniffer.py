import socket, struct, os, array
from scapy.all import *
import sys
from coding_utils import *

packet_count = 0
 
try: 
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x003))
except socket.error, msg:
    print 'Socket could not be created. Error Code: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit(1)

while True:
    try:
        packet = s.recvfrom(65565)

        # Get packet from tuple
        packet = packet[0]
        # print_hex("Raw packet", packet)

        scapy_pkt = Ether(packet)
        # packet_count += 1
        if scapy_pkt.haslayer(UDP):
            # print scapy_pkt[UDP].len
        # if scapy_pkt.type == 0x7123:
            # scapy_pkt.show2()
            if scapy_pkt[UDP].len >= 1470:
                packet_count += 1
                print scapy_pkt[UDP].len
        # else:
        #     print "Non COPE packet"
    except KeyboardInterrupt:
        print "Closing graciously", "receive count", packet_count
        if s:
            s.close()
        break

    # finally:
        




