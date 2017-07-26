import struct
import array

# data = "45 01 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1 02"
# data = "00 01 70 A4 14 02 7B E9 C4 4E 0A 00 00 01 00 01 0A 00 00 02 00 00 00 00 00 00 00 5A 0F"
# data = "00 01 70 A4 14 02 7B E9 C4 4E 0A 0B"
# data = "00 01 00 00 27 3F B1 37 AA 4B 0A 00 00 02 00 01 0A 00 00 02 00 00 00 00 00 00 00 5A 61 00 00 00 01 00 00"
data = "00 01 00 00 27 3F B1 37 AA 4B 0A 00 00 02 00 01 0A 00 00 02 00 00 00 00 00 00 00 5A 61 00 00 00 01 00 00 00 00"

def carry_around_add(a, b):
    c = a + b
    return (c & 0xffff) + (c >> 16)

def checksum(msg):
    s = 0
    print "len of message", len(msg)
    for i in range(0, len(msg), 2):
        if i+1 >= len(msg):
            w = ord(msg[i]) + (0x00 << 8)
        else:
            w = ord(msg[i]) + (ord(msg[i+1]) << 8)

        s = carry_around_add(s, w)
        # print "sum:", s, "word", w
    return ~s & 0xffff

if struct.pack("H",1) == "\x00\x01": # big endian
    def checksum2(pkt):
        if len(pkt) % 2 == 1:
            pkt += "\0"
        s = sum(array.array("H", pkt))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        s = ~s
        return s & 0xffff
else:
    def checksum2(pkt):
        if len(pkt) % 2 == 1:
            pkt += "\0"
        s = sum(array.array("H", pkt))
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        s = ~s
        return (((s>>8)&0xff)|s<<8) & 0xffff

if __name__ == '__main__':

    data = data.split()
    # print data
    data = map(lambda x: int(x,16), data)
    # print data
    data = struct.pack("%dB" % len(data), *data)
    # print data

    print ' '.join('%02X' % ord(x) for x in data)
    # print data
    print "Checksum: 0x%04x" % checksum(data)
    # print "Checksum2: 0x%04x" % checksum2(data)

    chksum = checksum(data)
    # print data
    data = data[:-2] + chr(chksum >> 8) + chr(chksum & 0xff)
    # print "Checksum", ' '.join('%02X' % ord(x) for x in chksum)
    # chksum2 = '' + chr(checksum2(data) >> 8) + chr(checksum2(data)&0x00ff)
    # print ' '.join('%02X' % ord(x) for x in chksum2)

    print ' '.join('%02X' % ord(x) for x in data)
    print "Checksum check: 0x%04x" % checksum(data)
    # print "Checksum2 check: 0x%04x" % checksum2(data + chksum2)
