from pythonstory.common.decorators import packet
from pythonstory.common import sendopcodes


@packet(sendopcodes.SPAWN_NPC)
def spawn_npc(builder, npc, show=True):
    (builder
     .write_int(npc.lifeid)
     .write_int(npc.lifeid)
     .write_short(npc.x_pos)
     .write_short(npc.y_pos)
     .write(npc.flags != 'faces_left')
     .write_short(npc.foothold)
     .write_short(npc.min_click_pos)
     .write_short(npc.max_click_pos)
     .write(show)
     )
    return builder.get_packet()


@packet(sendopcodes.SPAWN_NPC_REQUEST_CONTROLLER)
def control_npc(builder, npc, minimap=True):
    (builder
     .write(1)
     .write_int(npc.lifeid)
     .write_int(npc.lifeid)
     .write_short(npc.x_pos)
     .write_short(npc.y_pos)
     .write(npc.flags != 'faces_left')
     .write_short(npc.foothold)
     .write_short(npc.min_click_pos)
     .write_short(npc.max_click_pos)
     .write(minimap)
     )
    return builder.get_packet()


@packet(sendopcodes.NPC_ACTION)
def npc_talk(builder, i, s):
    (builder
     .write_int(i)
     .write_short(s)
     )
    return builder.get_packet()


@packet(sendopcodes.NPC_ACTION)
def npc_move(builder, arr):
    builder.write_array(arr)
    return builder.get_packet()
