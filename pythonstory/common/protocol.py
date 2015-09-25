from twisted.internet import protocol, task
import struct
from . import decoder, packetreader, packets


class MapleProtocol(protocol.Protocol, object):
    PING_TIME = 30
    processor = None

    def __init__(self):
        self.reader = packetreader.PacketReader()
        self.pingcall = task.LoopingCall(self.send_ping)
        self.decoder = decoder.Decoder()
        super(MapleProtocol, self).__init__()

    def send(self, packet):
        packet = self.decoder.encode(packet)
        self.transport.write(
            struct.pack('<%dB' % len(packet), *packet)
        )

    def dataReceived(self, data):
        if len(data) < 4:
            print 'Packet too small'
            return self.transport.loseConnection()
        header = struct.unpack('!i', data[:4])[0]
        if not self.decoder.check_header(header):
            print 'Corrupted header'
            return self.transport.loseConnection()
        body = data[4:]
        packetlength = self.decoder.get_packet_length(header)
        if len(body) == packetlength:
            self.packet_received(body)
        elif len(body) > packetlength:
            self.dataReceived(data[:4+packetlength])
            self.dataReceived(data[packetlength+4:])

    def packet_received(self, packet):
        packet = self.reader.process(self.decoder.decode(packet))
        self.processor.handle_packet(packet, self)

    def connectionMade(self):
        print "New connection {} on {} ".format(
                self.transport.getPeer().host,
                self.__class__.__name__
                )
        self.factory.connections.append(self)
        self.send_connect()
        self.pingcall.start(self.PING_TIME, now=True)

    def connectionLost(self, reason):
        print "Closed connection {} on {}".format(
                self.transport.getPeer().host,
                self.__class__.__name__
                )
        self.pingcall.stop()
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

    def send_ping(self):
        self.send(packets.ping(self))
