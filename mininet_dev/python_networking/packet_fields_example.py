from scapy.all import *

class TestPkt2(Packet):
	name="TestPkt2"
	fields_desc = [ IntField("pkt_id",101),
	IPField("next_hop","0.0.0.0") ]
	
	def extract_padding(self, p):
		return "", p

class TestSLF(Packet):
	fields_desc=[ FieldLenField("len", None, length_of="data"),
				  StrLenField("data", "", length_from=lambda pkt:pkt.len) ]

class TestPLF(Packet):
	fields_desc=[ FieldLenField("len", None, count_of="plist"),
					PacketListField("plist", None, IP, count_from=lambda pkt:pkt.len) ]

class TestPLF3(Packet):
	fields_desc=[ FieldLenField("len", None, count_of="plist"),
					PacketListField("plist", None, TestPkt2, count_from=lambda pkt:pkt.len) ]

class TestFLF(Packet):
	fields_desc=[
		FieldLenField("the_lenfield", None, count_of="the_varfield"),
		FieldListField("the_varfield", ["1.2.3.4"], IPField("", "0.0.0.0"),
		count_from = lambda pkt: pkt.the_lenfield) ]

class TestPkt(Packet):
	fields_desc = [ ByteField("f1",65),
	ShortField("f2",0x4244) ]
	
	def extract_padding(self, p):
		return "", p

class TestPLF2(Packet):
	fields_desc = [ FieldLenField("len1", None, count_of="plist",fmt="H", adjust=lambda pkt,x:x+2),
					FieldLenField("len2", None, length_of="plist",fmt="I", adjust=lambda pkt,x:(x+1)/2),
					PacketListField("plist", None, TestPkt2, length_from=lambda x:(x.len2*2)/3*3) ]

pkt = TestPkt2(pkt_id=123, next_hop="192.168.0.3")
# pkt.show2()

cope_pkt = TestPLF2()
print type(cope_pkt.plist)
cope_pkt.plist.append(pkt)

cope_pkt.show()
cope_pkt.show2()
# pkt = TestPLF2("\x00\x02ABCDEFGHIJKLMNO")
# pkt.show2()