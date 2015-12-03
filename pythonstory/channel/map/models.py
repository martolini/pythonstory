from pythonstory.common.staticmodels import (
                        MapData, MapSeats, MapPortals, MapLife
                        )
from pythonstory.common.helperclasses import Point, Rect
import pythonstory.channel.npc.packets as npcpackets
from pythonstory.channel.mob import (
                                     models as mobmodels,
                                     packets as mobpackets
                                     )
import threading


class Map(object):
    cache = {c: {} for c in xrange(5)}

    def __init__(self, mapid, channel):
        self.npcid = 200
        self.mobid = 500
        self.id = mapid
        self.channel = channel
        self.seats = {}
        self.clients = set()
        self.portals = {}
        self.npcs = {}
        self.mobs = {}
        self.reactor = {}

    @classmethod
    def get(cls, mapid, channel):
        if mapid in cls.cache[channel]:
            return cls.cache[channel][mapid]

        mmap = Map(mapid, channel)
        mmap.load_data(MapData.get(MapData.mapid == mmap.id))
        mmap.load_seats(MapSeats.select().where(MapSeats.mapid == mmap.id))
        for portal in MapPortals.select(
                        ).where(MapPortals.mapid == mmap.id):
            mmap.portals[portal.id] = portal
        mmap.load_life(MapLife.select().where(MapLife.mapid == mmap.id))
        cls.cache[channel][mmap.id] = mmap
        return mmap

    def add_client(self, client):
        self.clients.add(client)
        self.show_objects(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def get_portal_from_string(self, string):
        for k, v in self.portals.iteritems():
            if v.label == string:
                return self.portals[k]
        raise Exception("{} does not exist in map {}".format(
                                 string, self.id))

    def load_data(self, data):
        self.link = data.link
        self.return_map = data.return_map
        self.forced_return_map = data.forced_return_map
        self.spawn_rate = data.mob_rate
        self.music = data.default_bgm
        self.dimensions = Rect(
                               Point(data.map_ltx, data.map_lty),
                               Point(data.map_rbx, data.map_rby)
                               )
        self.shuffle_name = data.shuffle_name
        self.regular_hp_decrease = data.decrease_hp
        self.traction = data.default_traction
        self.regen_rate = data.regen_rate
        self.min_level_limit = data.min_level_limit
        self.time_limit = data.time_limit
        self.protect_item = data.protect_item
        self.damage_per_second = data.damage_per_second
        self.ship_kind = data.ship_kind

    def load_seats(self, seats):
        for seat in seats:
            self.seats[seat.seatid] = Point(seat.x_pos, seat.y_pos)

    def load_life(self, data):
        for life in data:
            storage = None
            if life.life_type == 'mob':
                mob = mobmodels.Mob.from_life(self.mobid, life, self)
                self.mobid += 1
                self.mobs[mob.objid] = mob
            elif life.life_type == 'npc':
                self.npcid += 1
                storage = self.npcs
                life.id = self.npcid
            if storage is not None:
                storage[life.id] = life

    def send(self, packet):
        for client in self.clients:
            client.send(packet)

    def show_objects(self, client):
        for npc in self.npcs.values():
            client.send(npcpackets.spawn_npc(npc))
            client.send(npcpackets.control_npc(npc))
        for mob in self.mobs.values():
            if mob.spawned:
                mob.show_for(client)

    def mob_died(self, objid):
        self.send(mobpackets.kill_mob(objid))
        mob = self.mobs[objid]
        threading.Timer(5.0, self.respawn_mob, [mob]).start()

    def respawn_mob(self, mob):
        mob.respawn()
        for client in self.clients:
            mob.show_for(client)
