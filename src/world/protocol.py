from ..common.protocol import MapleProtocol
from .processor import WorldPacketProcessor


class WorldProtocol(MapleProtocol):
    processor = WorldPacketProcessor

    def __init__(self, *args, **kwargs):
        self.channel = -1
        self.account = None
        super(WorldProtocol, self).__init__(*args, **kwargs)
