from scapy.all import *
import network_utils
import time

pkt_count = 0

def main():
    global pkt_count

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
            if scapy_pkt.type == 0x7123:
                print "Packet payload: ", scapy_pkt.payload
                pkt_count += 1

        except KeyboardInterrupt:
            
            break

if __name__ == '__main__':
    main()

