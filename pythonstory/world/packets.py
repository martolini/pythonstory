from ..common import sendopcodes
from ..common.decorators import packet
from ..channel.models import Keymap

from . import packethelpers
from ..common.packethelpers import maple_time

import random
import time


@packet(sendopcodes.LOGIN_STATUS)
def auth_success(builder, client):
    (builder
     .write_int(0)
     .write_short(0)
     .write_int(client.account.id)
     .write(client.account.gender)
     .write(client.account.gm > 0)
     )
    temp = client.account.gm * 32
    (builder
     .write(0x80 if temp > 0x80 else temp)  # wtf admin towrite byte
     .write(client.account.gm > 0)
     .write_string(client.account.name)
     .write(0)
     .write(0)
     .write_long(0)
     .write_long(0)
     .write_int(0)
     .write_short(2)
     )
    return builder.get_packet()


@packet(sendopcodes.LOGIN_STATUS)
def auth_failed(builder, reason):
    (builder
     .write(reason)
     .write(0)
     .write_int(0)
     )
    return builder.get_packet()


@packet(sendopcodes.SERVERLIST)
def serverlist(builder, world):
    (builder
     .write(world.key)
     .write_string(world.name)
     .write(world.flag)
     .write_string(world.eventmsg)
     .write(100)  # Rate modifier? Ask moople
     .write(0)  # event xp * 2.6 ?
     .write(100)  # rate modifier? ask moople
     .write(0)  # drop rate * 2.6
     .write(0)
     .write(len(world.channels))
     )
    for channel in world.channels:
        (builder
         .write_string('{}-{}'.format(world.name, channel.key))
         .write_int(1)  # server load
         .write(1)
         .write_short(channel.key - 1)
         )
    builder.write_short(0)
    return builder.get_packet()


@packet(sendopcodes.SERVERLIST)
def end_of_serverlist(builder):
    builder.write(0xFF)
    return builder.get_packet()


@packet(sendopcodes.LAST_CONNECTED_WORLD)
def select_world(builder, worldid):
    builder.write_int(worldid)
    return builder.get_packet()


@packet(sendopcodes.RECOMMENDED_WORLD_MESSAGE)
def recommended_worlds(builder, worlds):
    builder.write(len(worlds))
    for w in worlds:
        (builder
         .write_int(w.key)
         .write_string(w.recommended)
         )
    return builder.get_packet()


@packet(sendopcodes.SERVERSTATUS)
def server_load(builder, load):
    builder.write_short(load)
    return builder.get_packet()


@packet(sendopcodes.CHARLIST)
def charlist(builder, account):
    builder.write(0)
    characters = account.characters
    builder.write(characters.count())
    for character in characters:
        packethelpers.add_character_entry(builder, character)
    (builder
     .write(2)  # No pic
     .write_int(account.character_slots)
     )
    return builder.get_packet()


@packet(sendopcodes.CHAR_NAME_RESPONSE)
def char_name_response(builder, name, available):
    (builder
     .write_string(name)
     .write(not available)
     )
    return builder.get_packet()


@packet(sendopcodes.ADD_NEW_CHAR_ENTRY)
def create_character(builder, character):
    builder.write(0)
    packethelpers.add_character_entry(builder, character)
    return builder.get_packet()


@packet(sendopcodes.SERVER_IP)
def serverip(builder, ip, port, char_id):
    (builder
     .write_short(0)
     .write_array((int(c) for c in ip.split('.')))
     .write_short(port)
     .write_int(char_id)
     .write_array([0] * 5)
     )
    return builder.get_packet()
