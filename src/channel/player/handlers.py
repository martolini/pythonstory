from ..map import handlers as maphandlers
from ..map import models as mapmodels
from . import packets as playerpackets


def move_player(packet, client):
    packet.skip(9)
    x, y, foothold, stance = maphandlers.parse_movement(packet)
    client.character.move(x, y, foothold, stance)
    # client.send_map() # SOME PACKET, who cares as i'm the only one lol


def change_map(packet, client):
    if len(packet.data) == 0:
        # CASH SHOP
        return
    packet.read_byte()
    target = packet.read_int()
    startwp = packet.read_maplestring()
    currentmap = mapmodels.Map.get(mapid=client.character.map)
    portal = currentmap.get_portal_from_string(startwp)
    packet.read_byte()
    wheel = packet.read_short() > 0
    nextmap = mapmodels.Map.get(mapid=portal.destination)
    nextportal = nextmap.get_portal_from_string(portal.destination_label)
    client.send(
            playerpackets.change_map(nextmap, nextportal.id, client.character)
            )
    client.character.map = nextmap.id
