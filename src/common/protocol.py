from twisted.internet import protocol, task
import struct
from . import decoder, packetreader, packets
from threading import RLock


class MapleProtocol(protocol.Protocol, object):
    processor = None

    def __init__(self):
        self.reader = packetreader.PacketReader()
        self.lock = RLock()
        super(MapleProtocol, self).__init__()

    def send(self, packet):
        with self.lock:
            packet = self.decoder.encode(packet)
            self.transport.write(
                struct.pack('<%dB' % len(packet), *packet)
            )

    def dataReceived(self, data):
        header = struct.unpack('!i', data[:4])[0]
        if not self.decoder.check_header(header):
            print "Corrupted header or IVs"
            self.transport.loseConnection()
        body = data[4:]
        with self.lock:
            packet = self.reader.process(self.decoder.decode(body))
        self.processor.handle_packet(packet, self)

    def connectionMade(self):
        print "New connection {} on {} ".format(
                self.transport.getPeer().host,
                self.__class__.__name__
                )
        self.factory.connections.append(self)
        self.decoder = decoder.Decoder()
        self.send_connect()
        task.LoopingCall(self.send,
                         packets.ping(self)
                         ).start(60, now=False)

    def connectionLost(self, reason):
        print "Closed connection {} on {}".format(
                self.transport.getPeer().host,
                self.__class__.__name__
                )
        self.factory.connections.remove(self)

    def send_connect(self):
        data = struct.pack(
            '<hhhBBBBBBBBBB',
            0x0E,
            83,
            1,
            49,
            *(
              self.decoder.receive +
              self.decoder.send + [8]
            )
        )
        self.transport.write(data)
