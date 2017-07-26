import struct
import crcmod

# data = "45 01 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1"
# data = "00 01 70 A4 14 02 7B E9 C4 4E 0A 00 00 01 00 01 0A 00 00 02 00 00 00 00 00 00 00 5A 0F"
data = "00 01 70 A4 14 02 7B E9 C4 4E A2"

crc16 = crcmod.mkCrcFun(0x18005, rev="True", initCrc=0xFFFF, xorOut=0x0000)


def crc_checksum(msg):
    
    # Ignore last two bytes, i.e. checksum field
    return crc16(msg[:-2])

if __name__ == '__main__':

	data = data.split()
	print data
	data = map(lambda x: int(x,16), data)
	# print data
	data = struct.pack("%dB" % len(data), *data)
	# print data

	print ' '.join('%02X' % ord(x) for x in data)
	# print data
	print "Checksum: 0x%04x" % crc_checksum(data)