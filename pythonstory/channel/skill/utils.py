from . import models as skillmodels


def parse_attack(packet, character, ranged=False):
    packet.skip(1)
    tempbyte = packet.read_byte()
    targets = tempbyte / 0x10
    hits = tempbyte % 0x10
    skillid = packet.read_int()
    skill_level = None
    if skillid > 0:
        skill_level = skillmodels.Skill.get_level(skillid, character)
    # Handle big bang and heavens hammer
    packet.skip(8)
    display = packet.read_byte()
    direction = packet.read_byte()
    stance = packet.read_byte()
    # Handle meso explosion
    if ranged:
        pass
    else:
        packet.read_byte()
        weapon_speed = packet.read_byte()
        packet.skip(4)

    damages = {}
    for i in xrange(targets):
        mobid = packet.read_int()
        packet.skip(14)
        damagenumbers = []
        for j in xrange(hits):
            damagenumbers.append(packet.read_int())
        if skillid != 5221004:
            packet.skip(4)
        damages[mobid] = damagenumbers
    return skillmodels.Attack(damages=damages,
                              stance=stance,
                              direction=direction,
                              display=display,
                              skillid=skillid,
                              weapon_speed=weapon_speed,
                              skill_level=skill_level,
                              hits=hits,
                              targets=targets
                              )
