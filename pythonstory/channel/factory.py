from ..common.factory import MapleFactory
from .protocol import ChannelProtocol


class ChannelFactory(MapleFactory):
    protocol = ChannelProtocol

    def __init__(self, key, world, worldfac, *args, **kwargs):
        self.key = key
        self.world = world
        self.world_factory = worldfac
        super(ChannelFactory, self).__init__(*args, **kwargs)
