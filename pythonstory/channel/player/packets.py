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
