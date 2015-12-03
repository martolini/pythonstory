from ..map import models as mapmodels
from ..models import Keymap
from .. import commands
from pythonstory.channel.skill.utils import parse_attack
import packets


def move_player(packet, client):
    packet.skip(9)
    client.handle_movement(packet)


def change_map(packet, client):
    if len(packet.data) == 0:
        # CASH SHOP
        return
    packet.read_byte()
    targetmap = packet.read_int()  # Target map, use for something?
    startwp = packet.read_maplestring()
    currentmap = mapmodels.Map.get(
        mapid=client.character.map,
        channel=client.factory.key)
    portal = currentmap.get_portal_from_string(startwp)
    packet.read_byte()
    packet.read_short() > 0  # moople wheel
    nextmap = mapmodels.Map.get(
        mapid=portal.destination,
        channel=client.factory.key
    )
    nextportalid = nextmap.get_portal_from_string(portal.destination_label).id
    client.change_map(nextmap.id, nextportalid)


def change_keymap(packet, client):
    packet.read_int()
    numchanges = packet.read_int()
    changes = []
    for _ in xrange(numchanges):
        key = packet.read_int()
        ktype = packet.read_byte()
        action = packet.read_int()
        changes.append((key, ktype, action))
    Keymap.handle_changes(changes, client.character)


def handle_chat(packet, client):
    message = packet.read_maplestring()
    if message[0] == '@':
        splitted = message[1:].split(' ')
        command = splitted[0]
        args = splitted[1:]
        try:
            func = getattr(commands, command)
            func(client, *args)
        except AttributeError:
            print "No command {}".format(command)


def meele_attack(packet, client):
    attack = parse_attack(packet, client.character)
    curmap = mapmodels.Map.get(client.character.map, client.channel)
    for mobid, damages in attack.damages.iteritems():
        mob = curmap.mobs[mobid]
        total_damage = sum(damages)
        connected_hits = len(damages)
        mob.apply_damage(client, total_damage)


def change_map_special(packet, client):
    client.send(packets.enable_actions())
