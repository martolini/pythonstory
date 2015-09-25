from pythonstory.common.decorators import packet
from pythonstory.common import sendopcodes


@packet(sendopcodes.SPAWN_MONSTER)
def spawn_mob(builder, monster):
    (builder
     .write_int(monster.id)
     .write(5)  # CONTROL
     .write_int(monster.lifeid)
     .skip(15)
     .write(0x88)
     .skip(6)
     .write_short(monster.x_pos)  # MONSTER X POS
     .write_short(monster.y_pos)  # MONSTER Y POS
     .write(5)  # MOB STANCE
     .write_short(0)
     .write_short(monster.foothold)
     .write(-2)  # NEWSPAWN -2, else -1
     .write(0)  # GET TEAM
     .write_int(0)
     )
    return builder.get_packet()


@packet(sendopcodes.SPAWN_MONSTER_CONTROL)
def control_mob(builder, monster):
    (builder
     .write(1)
     .write_int(monster.id)
     .write(5)  # CONTROL
     .write_int(monster.lifeid)
     .skip(15)
     .write(0x88)
     .skip(6)
     .write_short(monster.x_pos)  # MONSTER X POS
     .write_short(monster.y_pos)  # MONSTER Y POS
     .write(5)  # MOB STANCE
     .write_short(0)
     .write_short(monster.foothold)
     .write(-2)  # NEWSPAWN -2, else -1
     .write(0)  # GET TEAM
     .write_int(0)
     )
    return builder.get_packet()
