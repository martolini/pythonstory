from ..common.factory import MapleFactory
from .protocol import WorldProtocol
from ..common.mixins import CharacterCacheMixin


class WorldFactory(CharacterCacheMixin, MapleFactory):
    protocol = WorldProtocol

    def __init__(self, worlds, *args, **kwargs):
        self.worlds = worlds
        return super(WorldFactory, self).__init__(*args, **kwargs)
