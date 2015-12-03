from ..common.protocol import MapleProtocol
from .processor import ChannelPacketProcessor
from .map import models as mapmodels
from .player import packets as playerpackets
from .mixins import MovableMixin
from pythonstory.common import gameconstants
from pythonstory.common import enums
import random


class ChannelProtocol(MovableMixin, MapleProtocol):
    processor = ChannelPacketProcessor

    def __init__(self, *args, **kwargs):
        self.character = None
        super(ChannelProtocol, self).__init__(*args, **kwargs)

    @property
    def current_map(self):
        return mapmodels.Map.get(self.character.map, self.channel)

    @property
    def channel(self):
        return self.factory.key

    @property
    def exprate(self):
        return self.factory.world.exprate

    def level_up(self):
        update_stats = ['level', 'exp']
        if self.character.job in (
                        enums.MapleJob.BEGINNER,
                        enums.MapleJob.NOBLESSE,
                        enums.MapleJob.LEGEND
                        ):
            self.character.ap = 0
            self.character.maxhp += random.randint(12, 16)
            self.character.maxmp += random.randint(10, 12)
            self.character.hp = self.character.maxhp
            self.character.mp = self.character.maxmp
            if self.character.level < 6:
                self.character.str += 5
            else:
                self.character.str += 4
                self.character.dex += 1
                update_stats.append('dex')
            update_stats.extend(['maxhp', 'maxmp', 'hp', 'mp', 'str'])
        else:
            self.character.ap += 5
            update_stats.append('ap')
            raise NotImplementedError("levelup {}".format(self.character.job))
        self.character.level += 1
        self.character.exp = 1
        self.send_stat_updates(update_stats)

    def send_stat_updates(self, stats):
        for stat in stats:
            self.send(playerpackets.update_stat(
                      getattr(enums.Stats, stat.upper()),
                      getattr(
                              self.character,
                              stat.lower()
                              )
                      ))

    def gain_exp(self, exp):
        total_exp = exp + self.character.exp
        if total_exp >= gameconstants.exptable[self.character.level - 1]:
            total_exp -= gameconstants.exptable[self.character.level - 1]
            self.level_up()
            self.character.exp = total_exp
        else:
            self.character.exp = total_exp
            self.send_stat_updates(['exp'])

        self.send(playerpackets.gain_exp(exp))
        self.character.save()

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
