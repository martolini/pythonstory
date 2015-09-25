from pythonstory.common.decorators import packet
from pythonstory.common import sendopcodes
import time


@packet(sendopcodes.UPDATE_QUEST_INFO)
def accept_quest(builder, questid, npcid):
    (builder
     .write(8)
     .write_short(questid)
     .write_int(npcid)
     .write_int(0)
     )
    return builder.get_packet()


@packet(sendopcodes.SHOW_STATUS_INFO)
def accept_quest_notice(builder, questid):
    (builder
     .write(1)
     .write_short(questid)
     .write(1)
     .write_int(0)
     .write_int(0)
     .write_short(0)
     )
    return builder.get_packet()


@packet(sendopcodes.SHOW_STATUS_INFO)
def complete_quest(builder, questid, completion_time=None):
    if completion_time is None:
        completion_time = int(time.time())
    (builder
     .write(1)
     .write_short(questid)
     .write(2)
     .write_long(completion_time)
     )
    return builder.get_packet()
