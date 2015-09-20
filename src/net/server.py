from ..constants import *
from .world import World
from .channel import Channel
from .serverhandler import MapleServerFactory
from twisted.internet import reactor

class Server:
  def __init__(self, ip):
    self.worlds = []
    self.ip = ip

  def run(self):
    for i, w in enumerate(ServerConstants.WORLDS):
      world = World(i, **w)
      for c in range(ServerConstants.CHANNELS):
        channel = Channel(world=world, key=c + 1)
        world.channels.append(channel)
        port = 7575 + c
        port += i * 100
        channel.port = port
        reactor.listenTCP(port, MapleServerFactory(world.key, channel.key, self), interface=self.ip)
      self.worlds.append(world)
    reactor.listenTCP(8484, MapleServerFactory(server=self), interface=self.ip)
    reactor.run()