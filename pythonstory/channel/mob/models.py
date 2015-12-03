from pythonstory.channel.mixins import MovableMixin
from pythonstory.common.staticmodels import MobAttacks, MobData
from collections import defaultdict
import packets


class Mob(MovableMixin, object):
    _data = {}

    def __init__(self, id, objid):
        self.id = id
        self.objid = objid
        self.spawned = True
        self.respawned = False
        self.controller = None
        self.damagetaken = defaultdict(int)
        self.hp = self.data.hp
        self.mp = self.data.mp
        super(Mob, self).__init__()

    def get_attack(self, attackid):
        return MobAttacks.get(
                             (MobAttacks.mobid == self.id) &
                             (MobAttacks.attackid == attackid)
                             )

    @property
    def channel(self):
        if self.mmap is not None:
            return self.mmap.channel
        return None

    @property
    def data(self):
        if self.id not in self._data:
            print 'Calling new mob'
            self.__class__._data[self.id] = MobData.get(mobid=self.id)
        return self._data[self.id]

    @classmethod
    def from_life(cls, objid, life, mmap):
        mob = cls(life.lifeid, objid)
        mob.map = mmap
        mob.mapid = life.mapid
        mob.move(life.x_pos, life.y_pos, life.foothold, stance=5)
        mob.faces_left = life.flags == 'faces_left'
        mob.respawn_time = life.respawn_time
        return mob

    def apply_damage(self, client, damage):
        if damage > self.hp:
            damage = self.hp
        self.damagetaken[client] += damage
        self.hp -= damage
        if self.hp < 0:
            print 'Mob should never get HP < 0'
        if self.hp == 0:
            return self.die(client)
        percent = int((float(self.hp) / self.data.hp * 100)+.5)
        client.send(packets.show_hp(self.objid, percent))

    def die(self, killer):
        # highest_damager = max(self.damagetaken, key=self.damagetaken.get)
        # This guy should get the drop eventually.
        self.distribute_exp(killer=killer)
        self.spawned = False
        self.controller = None
        self.map.mob_died(self.objid)

    def distribute_exp(self, killer):
        for client, damage in self.damagetaken.iteritems():
            exp = int(self.data.exp * (
                                   8 * damage / float(self.data.hp) +
                                   2 * (client == killer)
                                   ) / 10.0)
            client.gain_exp(exp * client.exprate)

    def respawn(self):
        self.respawned = self.spawned = True
        self.controller = None
        self.damagetaken.clear()
        self.hp = self.data.hp
        self.mp = self.data.mp

    def show_for(self, client):
        client.send(packets.spawn_mob(self))
        client.send(packets.control_mob(self))
