from ..utils.decoder import Decoder
import struct
from ..enums.sendopcodes import SendOpCode
from ..utils.packetbuilder import PacketBuilder
from time import time as timenow

class MapleClient:
  def __init__(self, session, channel, world):
    self.decoder = Decoder()
    self.session = session
    self.latency = -1
    self.account = None
    self.character = None
    self.channel = channel
    self.world = world

  def send_ping(self):
    pb = PacketBuilder()
    pb.write_short(SendOpCode.PING)
    self.lastping = timenow()
    self.send(pb.get_packet())

  def received_pong(self, timestamp):
    self.latency = (timestamp - self.lastping) / 2

  def send(self, data):
    data = self.decoder.encode(data)

    self.session.transport.write(
      struct.pack('<%sB' % len(data), *data)
    )
