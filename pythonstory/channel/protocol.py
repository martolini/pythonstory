from ..common.protocol import MapleProtocol
from .processor import ChannelPacketProcessor
from .map import models as mapmodels
from .player import packets as playerpackets


class ChannelProtocol(MapleProtocol):
    processor = ChannelPacketProcessor

    def __init__(self, *args, **kwargs):
        self.character = None
        super(ChannelProtocol, self).__init__(*args, **kwargs)

    @property
    def channel(self):
        return self.factory.key

    def send_map(self, *args, **kwargs):
        print 'Should send to map'

    def change_map(self, mapid, spawnpoint=0):
        currentmap = mapmodels.Map.get(
                                       self.character.map,
                                       self.channel)
        nextmap = mapmodels.Map.get(
                                    mapid,
                                    self.channel)
        currentmap.remove_client(self)
        self.character.map = nextmap.id
        self.send(playerpackets.change_map(
                  nextmap.id,
                  self.character,
                  self.channel,
                  spawnpoint
                  ))
        nextmap.add_client(self)

    def connectionLost(self, reason):
        if self.character is not None:
            self.character.save()
            mapmodels.Map.get(
                              mapid=self.character.map,
                              channel=self.factory.key
                              ).remove_client(self)
        return super(ChannelProtocol, self).connectionLost(reason)
