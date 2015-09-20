from ..common.protocol import MapleProtocol
from .processor import ChannelPacketProcessor
from .map import models as mapmodels


class ChannelProtocol(MapleProtocol):
    processor = ChannelPacketProcessor

    def __init__(self, *args, **kwargs):
        self.character = None
        super(ChannelProtocol, self).__init__(*args, **kwargs)

    def send_map(self, *args, **kwargs):
        for client in mapmodels.Map.get(id=self.character.map):
            pass  # Send
