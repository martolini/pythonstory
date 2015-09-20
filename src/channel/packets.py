from ..common.decorators import packet
from ..common import sendopcodes
from . import packethelpers
from ..common.packethelpers import maple_time
from .models import Keymap

import random
import time


@packet(sendopcodes.SET_FIELD)
def char_info(builder, character, channel):
    (builder
     .write_int(channel - 1)
     .write(1)
     .write(1)
     .write_short(0)
     )
    for i in xrange(3):
        builder.write_int(random.randint(1, 10000000))
    packethelpers.add_char_info(builder, character)
    builder.write_long(maple_time(time.time()))
    return builder.get_packet()


@packet(sendopcodes.KEYMAP)
def keymap(builder, character):
    builder.write(0)
    for ktype, action in Keymap.for_character(character):
        (builder
         .write(ktype)
         .write_int(action)
         )
    return builder.get_packet()


@packet(sendopcodes.MACRO_SYS_DATA_INIT)
def skillmacros(builder, character):
    builder.write(0)
    return builder.get_packet()


@packet(sendopcodes.BUDDYLIST)
def buddy_list(builder, character):
    (builder
     .write(7)
     .write(0)  # 0 Buddies :x
     )
    return builder.get_packet()


@packet(sendopcodes.FAMILY_PRIVILEGE_LIST)
def load_family(builder, character):
    builder.write_int(11)
    rep_cost = (3, 5, 7, 8, 10, 12, 15, 20, 25, 40, 50)
    for i in xrange(11):
        (builder
         .write((i % 2) + 1 if i > 4 else i)
         .write_int(rep_cost[i] * 100)
         .write_int(1)
         .write_string("Title {}".format(i))
         .write_string("Description {}".format(i))
         )
    return builder.get_packet()
