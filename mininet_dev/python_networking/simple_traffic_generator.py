from scapy.all import *
import sys
import network_utils

interface = "eth0"
dest_ip = "10.0.0.1"

def main():
  global interface, dest_ip
  if len(sys.argv) >= 2:
  	interface = sys.argv[1]

  if len(sys.argv) >= 3:
  	dest_ip = sys.argv[2]

  src_ip = network_utils.get_first_IPAddr()

  # for i in range(100):
  # send_COPE_packet(src_ip, dest_ip, "\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00", interface)
  for i in range(20):
	send_pkt = Ether(dst="ff:ff:ff:ff:ff:ff", type=0x7123)/Raw(str(i))
	sendp(send_pkt, iface=interface)

if __name__ == '__main__':
  main()
