from peewee import ForeignKeyField, IntegerField
from pythonstory.common.models import BaseModel
from pythonstory.channel.models import Character


class Skill(BaseModel):
    character = ForeignKeyField(Character)
    skillid = IntegerField()
    level = IntegerField()
    max_level = IntegerField()

    @classmethod
    def get_level(cls, skillid, character):
        return cls.select(cls.level).where(
                                           (cls.skillid == skillid) &
                                           (cls.character == character)
                                           ).level


class Attack(object):
    def __init__(self, damages, stance, direction, display, weapon_speed,
                 skill_level, hits, targets, skillid):
        # self.is_meso_explosion = False
        self.stance = stance
        # self.is_shadow_meso = False
        # self.is_charge_skill = False
        # self.is_piercing_arrow = False
        # self.is_heal = False
        self.targets = targets
        self.hits = hits
        self.display = display
        self.weapon_speed = weapon_speed
        self.direction = direction
        # self.weapon_class = 0
        self.skill_level = skill_level
        self.star_slot = -1
        self.skillid = skillid
        self.summonid = 0
        self.charge = 0
        self.starid = 0
        self.ticks = 0
        self.total_damage = 0
        self.projectile_slot = 0
        self.damages = damages
