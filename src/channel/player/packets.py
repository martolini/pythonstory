from src.common.decorators import packet
from src.common import sendopcodes
from src.common.packethelpers import maple_time

import time


@packet(sendopcodes.SET_FIELD)
def change_map(builder, destination, spawnpoint, character, channel):
    (builder
     .write_int(channel - 1)
     .write_int(0)
     .write(0)
     .write_int(destination.id)
     .write(spawnpoint)
     .write_short(character.hp)
     .write(0)
     .write_long(maple_time(time.time()))
     )
    return builder.get_packet()
