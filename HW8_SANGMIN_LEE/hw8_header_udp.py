import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!HHHH', self.src_port, self.dst_port, self.length, self.checksum)
        return packed

def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8])
    return unpacked

def getSrcPort(udpheader):
    return udpheader[0]

def getDstPort(udpheader):
    return udpheader[1]

def getLength(udpheader):
    return udpheader[2]

def getChecksum(udpheader):
    return udpheader[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udp = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udp))

unpacked_udp = unpack_Udphdr(packed_udp)
print(unpacked_udp)
print('Source Port:{} Destination Port:{} length:{} Checksum:{}'.format(getSrcPort(unpacked_udp), getDstPort(unpacked_udp), getLength(unpacked_udp), getChecksum(unpacked_udp)))
