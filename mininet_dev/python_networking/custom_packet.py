from scapy.all import *
import sys

class Test(Packet):

	name = "Test packet"
	fields_desc = [ShortField("test1", 1), ShortField("test2", 2)]

def make_test(x,y):
	return Ether()/IP()/Test(test1=x, test2=y)

if __name__ == '__main__':

	interface = "eth0"
	dest_ip = "10.0.0.1"
	if len(sys.argv) >= 2:
		interface = sys.argv[1]

	if len(sys.argv) >= 3:
		dest_ip = sys.argv[2]


	sendp(Ether()/IP(dst=dest_ip)/Test(test1=3,test2=4), iface=interface, inter=0.5, loop=1)