from peewee import PrimaryKeyField, IntegerField, Model,\
                    Field, ForeignKeyField, BigIntegerField, FloatField,\
                    CharField, TextField, CompositeKey
from . import settings
from . import enums


class StaticModel(Model):
    class Meta:
        database = settings.DATABASES['static']


class ItemData(StaticModel):
    itemid = PrimaryKeyField()
    price = IntegerField(default=1)
    max_slot_quantity = IntegerField(default=1)
    max_possession_count = IntegerField(default=0)
    min_level = IntegerField(default=0)
    max_level = IntegerField(default=200)
    experience = IntegerField(default=0)
    money = IntegerField(default=0)
    state_change_item = IntegerField(default=0)
    level_for_maker = IntegerField(default=0)
    npc = IntegerField(default=0)
    flags = CharField(max_length=50)

    class Meta:
        db_table = 'item_data'


class EnumSetField(Field):

    def __init__(self, enumtype, *args, **kwargs):
        self.enumtype = enumtype
        return super(EnumSetField, self).__init__(*args, **kwargs)

    def python_value(self, value):
        if value:
            return set(
                       getattr(self.enumtype, val.upper())
                       for val in value.split(',')
                       )
        return set()

    def db_value(self, value):
        return '{}'.format(x.name.lower() for x in value)


class ItemEquipData(StaticModel):
    item = ForeignKeyField(ItemData, primary_key=True,
                           related_name='equip', db_column='itemid')
    acc = IntegerField(db_column='accuracy')
    attack_speed = IntegerField()
    avoid = IntegerField()
    dex = IntegerField(db_column='dexterity')
    elemental_default = IntegerField()
    equip_slots = EnumSetField(enumtype=enums.EquipSlot)
    flags = CharField(max_length=50)  # IGNORE FLAGS FOR NOW
    hands = IntegerField()
    heal_hp = IntegerField()
    hp = IntegerField()
    inc_fire_damage = IntegerField()
    inc_ice_damage = IntegerField()
    inc_lightning_damage = IntegerField()
    inc_poison_damage = IntegerField()
    int = IntegerField(db_column='intelligence')
    jump = IntegerField()
    knockback = IntegerField()
    luk = IntegerField(db_column='luck')
    matk = IntegerField(db_column='magic_attack')
    mdef = IntegerField(db_column='magic_defense')
    mp = IntegerField()
    recovery = IntegerField()
    req_dex = IntegerField()
    req_fame = IntegerField()
    req_int = IntegerField()
    req_job = EnumSetField(enumtype=enums.MapleJob)
    req_luk = IntegerField()
    req_str = IntegerField()
    scroll_slots = IntegerField()
    specialid = BigIntegerField()
    speed = IntegerField()
    str = IntegerField(db_column='strength')
    taming_mob = IntegerField()
    traction = FloatField()
    watk = IntegerField(db_column='weapon_attack')
    wdef = IntegerField(db_column='weapon_defense')

    class Meta:
        db_table = 'item_equip_data'

    @classmethod
    def from_id(cls, itemid):
        instance = (cls
                    .select()
                    .join(ItemData)
                    .where(ItemEquipData.item == itemid)
                    .get()
                    )
        return instance


class MapData(StaticModel):
    mapid = PrimaryKeyField()
    damage_per_second = IntegerField()
    decrease_hp = IntegerField()
    default_bgm = CharField()
    default_traction = FloatField()
    field_limitations = TextField()
    field_type = TextField()
    flags = TextField()
    forced_return_map = IntegerField()
    link = IntegerField()
    map_ltx = IntegerField()
    map_lty = IntegerField()
    map_rbx = IntegerField()
    map_rby = IntegerField()
    min_level_limit = IntegerField()
    mob_rate = FloatField()
    protect_item = IntegerField()
    regen_rate = IntegerField()
    return_map = IntegerField()
    ship_kind = IntegerField()
    shuffle_name = CharField()
    time_limit = IntegerField()

    class Meta:
        db_table = 'map_data'


class MapLife(StaticModel):
    id = BigIntegerField(primary_key=True)
    flags = TextField()
    foothold = IntegerField()
    life_name = CharField(null=True)
    life_type = TextField()
    lifeid = IntegerField()
    mapid = IntegerField()
    max_click_pos = IntegerField()
    min_click_pos = IntegerField()
    respawn_time = IntegerField()
    x_pos = IntegerField()
    y_pos = IntegerField()

    class Meta:
        db_table = 'map_life'


class MapFootholds(StaticModel):
    drag_force = IntegerField()
    flags = TextField()
    id = IntegerField()
    mapid = IntegerField()
    nextid = IntegerField()
    previousid = IntegerField()
    x1 = IntegerField()
    x2 = IntegerField()
    y1 = IntegerField()
    y2 = IntegerField()

    class Meta:
        db_table = 'map_footholds'
        primary_key = CompositeKey('id', 'mapid')


class MapPortals(StaticModel):
    destination = IntegerField()
    destination_label = CharField(null=True)
    flags = TextField()
    id = IntegerField()
    label = CharField(null=True)
    mapid = IntegerField()
    script = CharField(null=True)
    x_pos = IntegerField()
    y_pos = IntegerField()

    class Meta:
        db_table = 'map_portals'
        primary_key = CompositeKey('id', 'mapid')


class MapSeats(StaticModel):
    mapid = IntegerField()
    seatid = IntegerField()
    x_pos = IntegerField()
    y_pos = IntegerField()

    class Meta:
        db_table = 'map_seats'
        primary_key = CompositeKey('mapid', 'seatid')


class MapContinentData(StaticModel):
    continent = IntegerField()
    map_cluster = IntegerField()

    class Meta:
        db_table = 'map_continent_data'
        primary_key = CompositeKey('continent', 'map_cluster')


class QuestData(StaticModel):
    fame = IntegerField()
    flags = TextField()
    max_level = IntegerField()
    min_level = IntegerField()
    next_quest = IntegerField()
    pet_closeness = IntegerField()
    quest_area = IntegerField()
    questid = PrimaryKeyField()
    repeat_wait = IntegerField()
    taming_mob_level = IntegerField()
    time_limit = IntegerField()

    class Meta:
        db_table = 'quest_data'
