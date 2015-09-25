import struct


class PacketReader(object):

    def process(self, arr):
        data = bytes(bytearray(arr))
        self.data = data[2:]
        self.opcode = struct.unpack_from('<H', data)[0]
        self.pos = 0
        return self

    def read_string(self, length):
        arr = [chr(self.read_byte()) for _ in xrange(length)]
        return ''.join(arr)

    def read_short(self):
        return self.read('H', 2)

    def read_int(self):
        return self.read('I', 4)

    def read_byte(self):
        byte = struct.unpack_from('<B', self.data, self.pos)[0]
        self.pos += 1
        return byte

    def read(self, format, length):
        out = struct.unpack_from('<' + format, self.data, self.pos)[0]
        self.pos += length
        return out

    def read_maplestring(self):
        return self.read_string(self.read_short())

    def skip(self, num):
        struct.unpack_from('<%sB' % num, self.data, self.pos)
        self.pos += num
        return None

    @property
    def bytes_available(self):
        return len(self.data) - self.pos
