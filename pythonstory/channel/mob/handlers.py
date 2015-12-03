from pythonstory.channel.map import models as mapmodels
from pythonstory.channel.mob import packets as mobpackets


def move_mob(packet, client):
    objectid = packet.read_int()
    moveid = packet.read_short()
    try:
        mob = mapmodels.Map.get(
            client.character.map, client.channel).mobs[objectid]
    except KeyError:
        return
    skill_byte = packet.read_byte()
    skill = packet.read_byte()
    skill_1 = packet.read_byte()
    skill_2 = packet.read_byte()
    skill_3 = packet.read_byte()
    skill_4 = packet.read_byte()
    packet.skip(8)
    to_use = None
    packet.read_byte()
    packet.read_int()
    start_x = packet.read_short()
    start_y = packet.read_short()
    mob.handle_movement(packet)

    aggro = False
    if to_use is None:
        client.send(
            mobpackets.move_mob_response(objectid, moveid, 5, aggro))
