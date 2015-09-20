from ..common import enums, packethelpers as commonhelpers, gamelogicutils
from .models import Item


def add_char_info(builder, character):
    (builder
     .write_long(-1)
     .write(0)
     )
    commonhelpers.add_char_stats(builder, character)
    (builder
     .write(0)  # No buddies :(
     .write(0)  # No linked name
     .write_int(character.meso)
     )
    add_inventor_info(builder, character)
    add_skill_info(builder, character)
    add_quest_info(builder, character)
    add_minigame_info(builder, character)
    add_ring_info(builder, character)
    add_teleport_info(builder, character)
    add_monsterbook_info(builder, character)
    add_new_year_info(builder, character)
    add_area_info(builder, character)
    builder.write_short(0)
    return


def add_inventor_info(builder, character):
    for i in xrange(5):  # Write inventory slots
        builder.write(24)
    builder.write_long(enums.TimeType.ZERO_TIME)
    equips = Item.get_equips_for(character)
    for equip in equips:
        if -100 < equip.slot < 0:
            add_item_info(builder, equip)
    builder.write_short(0)

    for equip in equips:
        if equip.slot < -100:
            add_item_info(builder, equip)
    builder.write_short(0)

    for equip in equips:
        if equip.slot > 0:
            add_item_info(builder, equip)

    builder.write_int(0)  # Use inventory
    builder.write(0)  # Setup inv
    builder.write(0)
    # ETC INV
    for item in Item.get_etcs_for(character):
        add_item_info(builder, item)
    builder.write(0)
    return


def add_item_info(builder, item, zeroslot=False):
    cash = gamelogicutils.is_cashslot(item.slot)
    pet = item.petid > -1
    equip = gamelogicutils.is_equip(item.itemid)
    slot = abs(item.slot)

    if not zeroslot:
        if equip:
            builder.write_short(slot - 100 if slot > 100 else slot)
        else:
            builder.write(slot + 1)
    (builder
     .write(1 if equip else 2)  # 3 if pet?
     .write_int(item.itemid)
     .write(0)
     )
    if cash:
        pass  # Ignore for now
    builder.write_long(enums.TimeType.DEFAULT_TIME)
    if pet:
        return  # Ignore
    if not equip:
        (builder
         .write_short(item.quantity)
         .write_string("")
         .write_short(item.flag)
         )
        # Add rechargables
        return

    (builder
     .write(item.scroll_slots)
     .write(item.level)
     .write_short(item.str)
     .write_short(item.dex)
     .write_short(item.int)
     .write_short(item.luk)
     .write_short(item.hp)
     .write_short(item.mp)
     .write_short(item.watk)
     .write_short(item.matk)
     .write_short(item.wdef)
     .write_short(item.mdef)
     .write_short(item.acc)
     .write_short(item.avoid)
     .write_short(item.hands)
     .write_short(item.speed)
     .write_short(item.jump)
     .write_string("")  # Owner
     .write_short(item.flag)
     )
    if cash:
        pass
    else:
        (builder
         .write(0)
         .write(item.level)
         .write_short(0)
         .write_short(item.itemexp)
         .write_int(item.vicious)
         .write_long(0)
         )
    (builder
     .write_long(enums.TimeType.ZERO_TIME)
     .write_int(-1)
     )
    return


def add_skill_info(builder, character):
    (builder
     .write(0)  # Start of skills
     .write_short(0)  # Size of skills
     .write_short(0)  # Cooldown size
     )


def add_quest_info(builder, character):
    (builder
     .write_short(0)  # N OF STARTED QUESTS
     .write_short(0)  # N OF COMPLETED QUESTS
     )
    return


def add_minigame_info(builder, character):
    builder.write_short(0)
    return


def add_ring_info(builder, character):
    (builder
     .write_short(0)  # CRUSH RINGS SIZE
     .write_short(0)  # FRIENDSSHIP RING SIZE
     .write_short(0)  # MARRIAGE ? No thanks.
     )
    return


def add_teleport_info(builder, character):
    for i in xrange(5):
        builder.write_int(999999999)  # TELE ROCK MAPS
    for i in xrange(10):
        builder.write_int(999999999)  # VIP TELE ROCK MAPS
    return


def add_monsterbook_info(builder, character):
    (builder
     .write_int(0)  # MONSTER BOOK COVER
     .write(0)
     .write_short(0)  # 0 monsterbook cards
     )
    return


def add_new_year_info(builder, character):
    builder.write_short(0)
    return


def add_area_info(builder, character):
    builder.write_short(0)  # null area info
    return
