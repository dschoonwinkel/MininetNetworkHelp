from scapy.packet import Packet
from scapy.fields import *

class RepeatingGroupedSequence(Packet):
    name = "Simple group of two fields"

    fields_desc = [IntField('field1', 1), 
                   IPField('nexthop', "0.0.0.0")]

    def extract_padding(self, s):
    	return '',s

class TopLayer(Packet):
    name = "Storage for Repeating Sequence"

    fields_desc = [FieldLenField("length", None, count_of='rep_seq'),
                   PacketListField('rep_seq', None, RepeatingGroupedSequence, 
                                   count_from = lambda pkt: pkt.length),
                  ]

#Now here is the problem that I have with assembling PacketListField: 

#craft TopLayer packet
p = TopLayer()

#add two "repeated sequences"
# p.rep_seq = [ RepeatingGroupedSequence(), RepeatingGroupedSequence() ]
p.rep_seq = list()
p.rep_seq.append(RepeatingGroupedSequence(field1=3, nexthop='10.0.0.1'))

#both sequences can observed
p.show()

print "\n\n"
# #but the underlying structure of the repeated sequence is #Raw# at this stage
p.show2()

print p.rep_seq[0].field1

# #length is 2
# print p.rep_seq, 'length:', len(p.rep_seq)

# #but the cloned packet has only one "repeated sequence", the rest is raw
# clone = TopLayer(str(p))
# clone.show()