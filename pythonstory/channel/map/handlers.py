from . import models as mapmodels
from pythonstory.channel.mob import models as mobmodels


def move_life(packet, client):
    pass
    # objectid = packet.read_int()
    # moveid = packet.read_short()
    # mob = mapmodels.Map.get(id=client.character.map).mobs[objectid]
    # if mob is None:
    #     return
    # nibbles = packet.read_byte()
    # activity = packet.read_byte()
    # skillid = packet.read_byte()
    # skill_level = packet.read_byte()
    # option = packet.read_short()
    # packet.skip(9)
    # x, y, foothold, stance = parse_movement(packet)
    # if activity >= 0:
    #     activity = activity >> 1
    # is_attack = activity in range(12,21)
    # is_skill = activity in range(21,26)
    # attackid = activity - 12 if is_attack else -1
    # next_movement_could_be_skill = (nibbles & 0x0F) != 0
    # unk = (nibbles & 0xF0) != 0
    # next_skill = 0
    # next_skill_level = 0
    # if is_attack:
    #     mob.get_attack(attackid)
