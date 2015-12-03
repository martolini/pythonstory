from ..channel.models import Item
from ..common import packethelpers as commonhelpers


def add_character_entry(builder, character, viewall=False, mega=False):
    commonhelpers.add_char_stats(builder, character)

    (builder
     .write(character.gender)
     .write(character.skin)
     .write_int(character.face)
     .write(not mega)
     .write_int(character.hair)
     )

    equips = {}
    masked_equips = {}
    for equip in Item.get_equips_for(character):
        slot = -equip.slot
        if slot < 100 and slot not in equips:
            equips[slot] = equip.itemid
        elif slot > 100 and slot != 111:
            slot -= 100
            if slot in equips:
                masked_equips[slot] = equips[slot]
            equips[slot] = equip.itemid
        elif slot in equips:
            masked_equips[slot] = equip.itemid

    for k, v in equips.iteritems():
        (builder
         .write(k)
         .write_int(v)
         )
    builder.write(0xFF)
    for k, v in masked_equips.iteritems():
        (builder
         .write(k)
         .write_int(v)
         )
    (builder
     .write(0xFF)
     .write_int(0)  # Cash weapon
     )
    for _ in xrange(3):  # Pets, deal with later
        builder.write_int(0)

    if not viewall:
        builder.write(0)

    (builder
     .write(1)
     .write_int(character.rank)
     .write_int(character.rank_move)
     .write_int(character.job_rank)
     .write_int(character.job_rank_move)
     )

    return
