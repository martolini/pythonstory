from src.common.staticmodels import MapData, MapSeats, MapPortals
from src.common.helperclasses import Point, Rect


class PortalDoesNotExist(Exception):
    pass


class SpawnInfo(object):
    def __init__(self):
        self.id = 0
        self.time = None
        self.spawned = False
        self.faces_left = False
        self.pos = Point(-1, -1)


class FootholdInfo(object):
    def __init__(self):
        self.forbid_jump_down = True
        self.left_edge = False
        self.right_edge = False
        self.id = 0
        self.drag_force = 0


class Map(object):

    def __init__(self, mapid):
        self.id = mapid
        self.seats = {}
        self.characters = set()
        self.portals = {}

    @classmethod
    def get(self, mapid):
        mmap = Map(mapid)
        mmap.load_data(MapData.get(MapData.mapid == mmap.id))
        mmap.load_seats(MapSeats.select().where(MapSeats.mapid == mmap.id))
        for portal in MapPortals.select().where(MapPortals.mapid == mmap.id):
            mmap.portals[portal.id] = portal
        return mmap

    def get_portal_from_string(self, string):
        for k, v in self.portals.iteritems():
            if v.label == string:
                return self.portals[k]
        raise PortalDoesNotExist("{} does not exist in map {}".format(
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
