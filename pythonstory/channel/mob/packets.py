from pythonstory.common.decorators import packet
from pythonstory.common import sendopcodes


@packet(sendopcodes.SPAWN_MONSTER)
def spawn_mob(builder, mob):
    (builder
     .write_int(mob.objid)
     .write(5 if mob.controller is None else 1)
     .write_int(mob.id)
     .skip(15)
     .write(0x88)
     .skip(6)
     .write_short(mob.pos.x)
     .write_short(mob.pos.y)
     .write(mob.stance)
     .write_short(0)
     .write_short(mob.foothold)
     )
    if mob.respawned:
        (builder
         .write(1)
         .write(0)
         .write_short(0)
         )
    (builder
     .write(-1 if mob.respawned else -2)
     .write(0)  # TEAM
     .write_int(0)
     )
    return builder.get_packet()


@packet(sendopcodes.SPAWN_MONSTER_CONTROL)
def control_mob(builder, mob):
    (builder
     .write(1)
     .write_int(mob.objid)
     .write(5 if mob.controller is None else 1)
     .write_int(mob.id)
     .skip(15)
     .write(0x88)
     .skip(6)
     .write_short(mob.pos.x)
     .write_short(mob.pos.y)
     .write(mob.stance)
     .write_short(0)
     .write_short(mob.foothold)
     .write(-1 if mob.respawned else -2)
     .write(0)  # TEAM
     .write_int(0)
     )
    return builder.get_packet()


@packet(sendopcodes.MOVE_MONSTER_RESPONSE)
def move_mob_response(builder, objid, moveid,
                      mp, aggro, skillid=False, skill_level=False):
    (builder
     .write_int(objid)
     .write_short(moveid)
     .write(aggro)
     .write_short(mp)
     .write(skillid)
     .write(skill_level)
     )
    return builder.get_packet()


@packet(sendopcodes.SHOW_MONSTER_HP)
def show_hp(builder, objid, percenthp):
    (builder
     .write_int(objid)
     .write(percenthp)
     )
    return builder.get_packet()


@packet(sendopcodes.KILL_MONSTER)
def kill_mob(builder, objid, animation=True):
    return (builder
            .write_int(objid)
            .write(animation)
            .write(animation)
            ).get_packet()
