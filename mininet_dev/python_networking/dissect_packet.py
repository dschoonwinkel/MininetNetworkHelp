from scapy.all import *

class Test(Packet):
	name="Test packet"
	field_desc = [ ShortField("ENCODED_NUM", 1), XByteField("minnie", 3)]


pkt = Ether()/IP()/UDP()/Test()/"HelloWorld!"

# print pkt[Test].underlayer
print pkt.show()