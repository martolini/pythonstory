from pythonstory.common.staticmodels import (
                        MapData, MapSeats, MapPortals, MapLife
                        )
from pythonstory.common.helperclasses import Point, Rect
from . import packets as mappackets
import pythonstory.channel.npc.packets as npcpackets


class Map(object):
    cache = {c: {} for c in xrange(5)}

    def __init__(self, mapid):
        self.npcid = 200
        self.mobid = 500
        self.id = mapid
        self.seats = {}
        self.clients = set()
        self.portals = {}
        self.npc = {}
        self.mob = {}
        self.reactor = {}

    @classmethod
    def get(cls, mapid, channel):
        if mapid in cls.cache[channel]:
            return cls.cache[channel][mapid]

        mmap = Map(mapid)
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
        self.spawn_mobs(client)

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
                storage = self.mob
                life.id = self.mobid
                self.mobid += 1
            elif life.life_type == 'npc':
                self.npcid += 1
                storage = self.npc
                life.id = self.npcid
            if storage is not None:
                storage[life.id] = life

    def send(self, packet):
        for client in self.clients:
            client.send(packet)

    def spawn_mobs(self, client):
        for mob in self.mob.values():
            client.send(mappackets.spawn_mob(mob))
            client.send(mappackets.control_mob(mob))

    def show_objects(self, client):
        for npc in self.npc.values():
            client.send(npcpackets.spawn_npc(npc))
            client.send(npcpackets.control_npc(npc))
