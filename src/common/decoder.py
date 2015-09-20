import random
import struct
from Crypto.Cipher import AES
from . import bitutils


aeskey = [
    0x13, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00,
    0xB4, 0x00, 0x00, 0x00, 0x1B, 0x00, 0x00, 0x00, 0x0F, 0x00, 0x00, 0x00,
    0x33, 0x00, 0x00, 0x00, 0x52, 0x00, 0x00, 0x00
]
update_matrix = [
    0xEC, 0x3F, 0x77, 0xA4, 0x45, 0xD0, 0x71, 0xBF, 0xB7, 0x98, 0x20, 0xFC,
    0x4B, 0xE9, 0xB3, 0xE1, 0x5C, 0x22, 0xF7, 0x0C, 0x44, 0x1B, 0x81, 0xBD,
    0x63, 0x8D, 0xD4, 0xC3, 0xF2, 0x10, 0x19, 0xE0, 0xFB, 0xA1, 0x6E, 0x66,
    0xEA, 0xAE, 0xD6, 0xCE, 0x06, 0x18, 0x4E, 0xEB, 0x78, 0x95, 0xDB, 0xBA,
    0xB6, 0x42, 0x7A, 0x2A, 0x83, 0x0B, 0x54, 0x67, 0x6D, 0xE8, 0x65, 0xE7,
    0x2F, 0x07, 0xF3, 0xAA, 0x27, 0x7B, 0x85, 0xB0, 0x26, 0xFD, 0x8B, 0xA9,
    0xFA, 0xBE, 0xA8, 0xD7, 0xCB, 0xCC, 0x92, 0xDA, 0xF9, 0x93, 0x60, 0x2D,
    0xDD, 0xD2, 0xA2, 0x9B, 0x39, 0x5F, 0x82, 0x21, 0x4C, 0x69, 0xF8, 0x31,
    0x87, 0xEE, 0x8E, 0xAD, 0x8C, 0x6A, 0xBC, 0xB5, 0x6B, 0x59, 0x13, 0xF1,
    0x04, 0x00, 0xF6, 0x5A, 0x35, 0x79, 0x48, 0x8F, 0x15, 0xCD, 0x97, 0x57,
    0x12, 0x3E, 0x37, 0xFF, 0x9D, 0x4F, 0x51, 0xF5, 0xA3, 0x70, 0xBB, 0x14,
    0x75, 0xC2, 0xB8, 0x72, 0xC0, 0xED, 0x7D, 0x68, 0xC9, 0x2E, 0x0D, 0x62,
    0x46, 0x17, 0x11, 0x4D, 0x6C, 0xC4, 0x7E, 0x53, 0xC1, 0x25, 0xC7, 0x9A,
    0x1C, 0x88, 0x58, 0x2C, 0x89, 0xDC, 0x02, 0x64, 0x40, 0x01, 0x5D, 0x38,
    0xA5, 0xE2, 0xAF, 0x55, 0xD5, 0xEF, 0x1A, 0x7C, 0xA7, 0x5B, 0xA6, 0x6F,
    0x86, 0x9F, 0x73, 0xE6, 0x0A, 0xDE, 0x2B, 0x99, 0x4A, 0x47, 0x9C, 0xDF,
    0x09, 0x76, 0x9E, 0x30, 0x0E, 0xE4, 0xB2, 0x94, 0xA0, 0x3B, 0x34, 0x1D,
    0x28, 0x0F, 0x36, 0xE3, 0x23, 0xB4, 0x03, 0xD8, 0x90, 0xC8, 0x3C, 0xFE,
    0x5E, 0x32, 0x24, 0x50, 0x1F, 0x3A, 0x43, 0x8A, 0x96, 0x41, 0x74, 0xAC,
    0x52, 0x33, 0xF0, 0xD9, 0x29, 0x80, 0xB1, 0x16, 0xD3, 0xAB, 0x91, 0xB9,
    0x84, 0x7F, 0x61, 0x1E, 0xCF, 0xC5, 0xD1, 0x56, 0x3D, 0xCA, 0xF4, 0x05,
    0xC6, 0xE5, 0x08, 0x49
]


def AESencrypt(data):
    cipher = AES.new(bytes(bytearray(aeskey)))
    return struct.unpack('!16B', cipher.encrypt(bytes(bytearray(data))))


class Decoder:
    def __init__(self):
        self.send = [82, 48, 120, random.randint(1, 122)]
        self.receive = [70, 114, 122, random.randint(1, 122)]
        self.receive_mapleversion = 83
        self.send_mapleversion = 0xFFFF - 83
        self.send_mapleversion = (
                ((self.send_mapleversion >> 8) & 0xFF) |
                ((self.send_mapleversion << 8) & 0xFF00)
        )
        self.receive_mapleversion = (
                ((self.receive_mapleversion >> 8) & 0xFF) |
                ((self.receive_mapleversion << 8) & 0xFF00)
        )

    def encode(self, data):
        header = self.get_packet_header(len(data))
        # Maple custom encryption
        for j in xrange(0, 6):
            remember = 0
            data_length = len(data) & 0xFF
            if j % 2 == 0:
                for i in xrange(len(data)):
                    cur = data[i]
                    cur = bitutils.roll_left(cur, 3)
                    cur += data_length
                    cur ^= remember
                    remember = cur
                    cur = bitutils.roll_right(cur, data_length & 0xFF)
                    cur = ~cur & 0xFF
                    cur += 0x48
                    data_length -= 1
                    data[i] = cur
            else:
                for i in reversed(xrange(len(data))):
                    cur = data[i]
                    cur = bitutils.roll_left(cur, 4)
                    cur += data_length
                    cur ^= remember
                    remember = cur
                    cur ^= 0x13
                    cur = bitutils.roll_right(cur, 3)
                    data_length -= 1
                    data[i] = cur

        data = self.maple_aes(data, self.send)
        self.encodeUpdate()
        return header + data

    def maple_aes(self, data, iv):
        remaining = len(data)
        length = 1456
        start = 0
        while remaining > 0:
            receive = iv * 4
            if remaining < length:
                length = remaining
            for x in xrange(start, start+length):
                if (x - start) % len(receive) == 0:
                    receive = AESencrypt(receive)
                data[x] ^= receive[(x - start) % len(receive)]
            start += length
            remaining -= length
            length = 0x5B4
        return data

    def decode(self, data):
        data = list(struct.unpack('!%sB' % len(data), data))
        data = self.maple_aes(data, self.receive)
        self.decodeUpdate()

        # Maple Custom Decryption
        for j in range(1, 7):
            remember = 0
            data_length = len(data) & 0xFF
            next_remember = 0
            if j % 2 == 0:
                for i in xrange(len(data)):
                    cur = data[i]
                    cur -= 0x48
                    cur = ~cur & 0xFF
                    cur = bitutils.roll_left(cur, data_length & 0xFF)
                    next_remember = cur
                    cur ^= remember
                    remember = next_remember
                    cur -= data_length
                    cur = bitutils.roll_right(cur, 3)
                    data[i] = cur
                    data_length -= 1
            else:
                for i in reversed(xrange(len(data))):
                    cur = data[i]
                    cur = bitutils.roll_left(cur, 3)
                    cur ^= 0x13
                    next_remember = cur
                    cur ^= remember
                    remember = next_remember
                    cur -= data_length
                    cur = bitutils.roll_right(cur, 4)
                    data[i] = cur
                    data_length -= 1
        return data

    def encodeUpdate(self):
        self.updateIV(self.send)

    def decodeUpdate(self):
        self.updateIV(self.receive)

    def updateIV(self, matrix):
        arr = [0xf2, 0x53, 0x50, 0xc6]
        for x in range(4):
            self.rotate(matrix[x], arr)
        matrix[:] = arr

    def rotate(self, input_byte, arr):
        elina = arr[1]
        anna = input_byte
        moritz = update_matrix[elina & 0xFF]
        moritz -= input_byte
        arr[0] += moritz
        moritz = arr[2]
        moritz ^= update_matrix[(int(anna) & 0xFF)]
        elina -= int(moritz) & 0xFF
        arr[1] = elina
        elina = arr[3]
        moritz = elina
        elina -= int(arr[0] & 0xFF)
        moritz = update_matrix[int(moritz & 0xFF)]
        moritz += input_byte
        moritz ^= arr[2]
        arr[2] = moritz
        elina += int(update_matrix[int(anna) & 0xFF]) & 0xFF
        arr[3] = elina
        merry = int(arr[0]) & 0xFF
        merry |= (arr[1] << 8) & 0xFF00
        merry |= (arr[2] << 16) & 0xFF0000
        merry |= (arr[3] << 24) & 0xFF000000
        ret_value = merry
        ret_value = bitutils.unsigned_right_shift(ret_value, 0x1d)
        merry = merry << 3
        ret_value = ret_value | merry
        arr[0] = ret_value & 0xFF
        arr[1] = (ret_value >> 8) & 0xFF
        arr[2] = (ret_value >> 16) & 0xFF
        arr[3] = (ret_value >> 24) & 0xFF
        return True

    # SHOULD BE [-44, -116, -42, -116]
    # [212, 140, 214, 140]
    def get_packet_header(self, length):
        iiv = self.send[3] & 0xFF
        iiv |= (self.send[2] << 8) & 0xFF00
        iiv ^= self.send_mapleversion
        mlength = ((length << 8) & 0xFF00) | (bitutils.unsigned_right_shift(length, 8))
        xoredIv = iiv ^ mlength
        return [
            bitutils.unsigned_right_shift(iiv, 8) & 0xFF,
            iiv & 0xFF,
            (bitutils.unsigned_right_shift(xoredIv, 8) & 0xFF),
            xoredIv & 0xFF
        ]

    def check_header(self, header):
        header = (
                  header >> 24 & 0xFF,
                  header >> 16 & 0xFF
                  )
        first = (header[0] ^ self.receive[2]) & 0xFF
        second = (self.receive_mapleversion >> 8) & 0xFF
        third = (header[1] ^ self.receive[3]) & 0xFF
        fourth = self.receive_mapleversion & 0xFF
        return first == second and third == fourth
