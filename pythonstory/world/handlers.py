from .models import Account
from ..channel.models import Character, Item
from . import packets as worldpackets
from ..common import enums


def login(packet, client):
    name = packet.read_maplestring()
    pwd = packet.read_maplestring()
    account = Account.login(name, pwd)
    if account is not None:
        client.account = account
        packet = worldpackets.auth_success(client)
    else:
        reason = 4
        packet = worldpackets.auth_failed(reason)
    client.send(packet)


def serverlist(packet, client):
    for world in client.factory.worlds:
        client.send(worldpackets.serverlist(world))
    client.send(worldpackets.end_of_serverlist())
    client.send(worldpackets.select_world(0))
    client.send(worldpackets.recommended_worlds(client.factory.worlds))


def server_status_load(packet, client):
    world = packet.read_short()
    for channel in client.factory.worlds[world - 1].channels:
        pass  # Loop over all channels, sum connected clients
    load = 0  # Calculated load
    client.send(worldpackets.server_load(load))


def charlist(packet, client):
    packet.read_byte()
    world = packet.read_byte()
    client.world = client.factory.worlds[world]
    client.channel = packet.read_byte()
    client.send(worldpackets.charlist(client.account))


def check_charname(packet, client):
    name = packet.read_maplestring()
    available = Character.name_is_available(name)
    client.send(worldpackets.char_name_response(name, available))


def create_character(packet, client):
    character = Character()
    character.name = packet.read_maplestring()
    character.account = client.account
    character.world = client.world.key
    job = packet.read_int()
    character.face = packet.read_int()
    character.hair = packet.read_int() + packet.read_int()
    character.skin = packet.read_int()
    top = packet.read_int()
    bottom = packet.read_int()
    shoes = packet.read_int()
    weapon = packet.read_int()
    character.gender = packet.read_byte()

    beginnerbook = None
    if job == 0:  # Knights
        character.job = enums.MapleJob.NOBLESSE
        character.map = 13003000
        beginnerbook = 4161047
    elif job == 1:
        character.job = enums.MapleJob.BEGINNER
        character.map = 10000
        beginnerbook = 4161001
    elif job == 2:
        character.job = enums.MapleJob.LEGEND
        character.map = 914000000
        beginnerbook = 4161048
    else:
        raise Exception("Unknown job byte")

    character.save()
    client.factory.set_character(character)
    Item.create(itemid=top, character=character,
                slot=-enums.EquipSlot.TOP)
    Item.create(itemid=bottom, character=character,
                slot=-enums.EquipSlot.BOTTOM)
    Item.create(itemid=shoes, character=character,
                slot=-enums.EquipSlot.SHOE)
    Item.create(itemid=weapon, character=character,
                slot=-enums.EquipSlot.WEAPON)
    Item.create(itemid=beginnerbook, character=character,
                slot=0)
    client.send(worldpackets.create_character(character))


def character_selected(packet, client):
    char_id = packet.read_int()
    packet.read_maplestring()  # MAC addr, ignore
    host = client.transport.getHost()
    ip = host.host
    port = client.world.channels[client.channel].port
    client.send(worldpackets.serverip(ip, port, char_id))
