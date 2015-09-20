class PacketBuilder:
    def __init__(self):
        self.arr = []

    def write_short(self, val):
        self.arr.extend((val & 0xFF, val >> 8 & 0xFF))
        return self

    def write(self, val):
        self.arr.append(val)
        return self

    def write_string(self, string, prepend_length=True):
        if prepend_length:
            self.write_short(len(string))
        self.arr.extend((ord(c) for c in string))
        return self

    def write_array(self, arr):
        self.arr.extend(arr)
        return self

    def write_int(self, val):
        self.arr.extend(
            (
                val & 0xFF,
                val >> 8 & 0xFF,
                val >> 16 & 0xFF,
                val >> 24 & 0xFF
            )
        )
        return self

    def write_string_rightpad(self, string, pad, length):
        self.write_string(
          string + pad * (length - len(string)),
          prepend_length=False
        )
        return self

    def write_long(self, val):
        self.arr.extend(
            (
                val & 0xFF,
                val >> 8 & 0xFF,
                val >> 16 & 0xFF,
                val >> 24 & 0xFF,
                val >> 32 & 0xFF,
                val >> 40 & 0xFF,
                val >> 48 & 0xFF,
                val >> 56 & 0xFF
            )
        )
        return self

    def get_packet(self):
        return self.arr
