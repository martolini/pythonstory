from . import enums


def maple_time(ts):
    if ts == -1:
        return enums.TimeType.DEFAULT_TIME
    if ts == -2:
        return enums.TimeType.ZERO_TIME
    if ts == -3:
        return enums.TimeType.PERMANENT
    return int(ts) * 1000 * 10000 + enums.TimeType.FT_UT_OFFSET


def add_char_stats(builder, character):
    (builder
     .write_int(character.id)
     .write_string_rightpad(character.name, '\0', 13)
     .write(character.gender)
     .write(character.skin_color)
     .write_int(character.face)
     .write_int(character.hair)
     )
    for i in xrange(3):  # Pets - ignore
        builder.write_long(0)
    (builder
     .write(character.level)
     .write_short(character.job)
     .write_short(character.str)
     .write_short(character.dex)
     .write_short(character.int)
     .write_short(character.luk)
     .write_short(character.hp)
     .write_short(character.maxhp)
     .write_short(character.mp)
     .write_short(character.maxmp)
     .write_short(character.ap)
     .write_short(character.sp)
     .write_int(character.exp)
     .write_short(character.fame)
     .write_int(character.gachaexp)
     .write_int(character.map)
     .write(character.spawn_point)
     .write_int(0)
     )
    return
