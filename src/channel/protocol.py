from ..common.protocol import MapleProtocol
from .processor import ChannelPacketProcessor
from .map import models as mapmodels


class ChannelProtocol(MapleProtocol):
    processor = ChannelPacketProcessor

    def __init__(self, *args, **kwargs):
        self.character = None
        super(ChannelProtocol, self).__init__(*args, **kwargs)

    def send_map(self, *args, **kwargs):
        print 'Should send to map'

    def connectionLost(self, reason):
        self.character.save()
        mapmodels.Map.get(
                          mapid=self.character.map,
                          channel=self.factory.key
                          ).remove_client(self)
        return super(ChannelProtocol, self).connectionLost(reason)
