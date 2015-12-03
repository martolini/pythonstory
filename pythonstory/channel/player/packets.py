from pythonstory.common.decorators import packet
from pythonstory.common import sendopcodes
from pythonstory.common.packethelpers import maple_time

import time


@packet(sendopcodes.SET_FIELD)
def change_map(builder, destinationid, character, channel, spawnpoint=0):
    (builder
     .write_int(channel - 1)
     .write_int(0)
     .write(0)
     .write_int(destinationid)
     .write(spawnpoint)
     .write_short(character.hp)
     .write(0)
     .write_long(maple_time(time.time()))
     )
    return builder.get_packet()


@packet(sendopcodes.SHOW_STATUS_INFO)
def gain_exp(builder, exp, white=True, inchat=False):
    (builder
     .write(3)
     .write(white)
     .write_int(exp)
     .write(inchat)
     .write_int(0)
     .write_short(0)
     .write_int(0)
     .write(0)
     .write_int(0)
     .write_int(0)
     .write_int(0)
     .write_int(0)
     )
    if inchat:
        builder.write(0)
    return builder.get_packet()


@packet(sendopcodes.STAT_CHANGED)
def update_stat(builder, updatebit, value, itemresponse=False):
    (builder
     .write(itemresponse)
     .write_int(updatebit)
     )
    if updatebit == 0x1:
        builder.write_short(value)
    elif updatebit <= 0x4:
        builder.write_int(value)
    elif updatebit < 0x20:
        builder.write(value)
    elif updatebit < 0xFFFF:
        builder.write_short(value)
    else:
        builder.write_int(value)
    return builder.get_packet()


@packet(sendopcodes.STAT_CHANGED)
def enable_actions(builder):
    return (builder
            .write(True)
            .write_int(0)).get_packet()
