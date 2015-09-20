from twisted.internet import reactor, protocol, task
import random
import struct
from mapleclient import MapleClient
from ..utils.packetprocessor import PacketProcessor
from ..utils.packetreader import PacketReader

class MapleServerHandler(protocol.Protocol):

  def unpack_header(self, header):
    return struct.unpack('!i', header)

  def dataReceived(self, data):
    if not data:
      print data
      return
    header = data[:4]
    # Do nothing with header so far
    body = data[4:]
    decoded_data = self.client.decoder.decode(body)
    packet = PacketReader(decoded_data)
    PacketProcessor.handle_packet(packet, self.client)


  def connectionMade(self):
    print 'Made a connection'
    self.client = MapleClient(self, channel=self.factory.channel, world=self.factory.world)
    data = struct.pack(
      '<hhhBBBBBBBBBB', 0x0E, 83, 1, 49, *(self.client.decoder.receive + self.client.decoder.send + [8])
    )
    self.transport.write(data)
    lc = task.LoopingCall(self.client.send_ping)
    lc.start(60, now=False)

  def connectionLost(self, reason):
    print 'Lost conn {}'.format(reason)

class MapleServerFactory(protocol.Factory):
  protocol = MapleServerHandler
  def __init__(self, world=-1, channel=-1, server=None):
    self.world = world
    self.channel = channel
    self.server = server
