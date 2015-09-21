from src.common.decorators import packet
from src.common import sendopcodes


@packet(sendopcodes.SPAWN_MONSTER)
def spawn_mob(builder, monster):
    builder.write_int(monster.id)
    builder.write(5)
    builder.write_int(monster.lifeid)
    builder.skip(15)
    builder.write(0x88)
    builder.skip(6)
    builder.write_short(100)  # MONSTER X POS
    builder.write_short(300)  # MONSTER Y POS
    builder.write(0)  # MOB STANCE
    builder.write_short(0)
    builder.write(-2)  # NEWSPAWN -1, else -1
    builder.write(0)  # GET TEAM
    builder.write_int(0)
    return builder.get_packet()


@packet(sendopcodes.SPAWN_NPC)
def spawn_npc(builder, npc):
    (builder
     .write_int(npc.id)
     .write_int(npc.lifeid)
     .write_short(npc.x_pos)
     .write_short(npc.y_pos)
     .write(npc.flags != 'faces_left')
     .write_short(npc.foothold)
     .write_short(npc.min_click_pos)
     .write_short(npc.max_click_pos)
     .write(1)
     )
    return builder.get_packet()


@packet(sendopcodes.SPAWN_NPC_REQUEST_CONTROLLER)
def control_npc(builder, npc):
    (builder
     .write(1)
     .write_int(npc.id)
     .write_int(npc.lifeid)
     .write_short(npc.x_pos)
     .write_short(npc.y_pos)
     .write(npc.flags != 'faces_left')
     .write_short(npc.foothold)
     .write_short(npc.min_click_pos)
     .write_short(npc.max_click_pos)
     .write(1)
     )
    return builder.get_packet()
