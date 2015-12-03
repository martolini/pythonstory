from peewee import *

database = SqliteDatabase('staticdb.sqlite', **{})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class BlockChatReasonData(BaseModel):
    message = CharField()
    reason = CharField()

    class Meta:
        db_table = 'block_chat_reason_data'

class BlockReasonData(BaseModel):
    block_type = CharField()
    message = CharField()

    class Meta:
        db_table = 'block_reason_data'

class CashCommodityData(BaseModel):
    expiration_days = IntegerField()
    flags = TextField()
    gender = TextField()
    itemid = IntegerField()
    price = IntegerField()
    priority = UnknownField()  # tinyint(3)
    quantity = IntegerField()
    serial_number = PrimaryKeyField()

    class Meta:
        db_table = 'cash_commodity_data'

class CashPackageData(BaseModel):
    id = BigIntegerField(primary_key=True)
    packageid = IntegerField()
    serial_number = IntegerField()

    class Meta:
        db_table = 'cash_package_data'

class CharacterCreationData(BaseModel):
    character_type = TextField()
    gender = TextField()
    id = BigIntegerField(primary_key=True)
    object_type = TextField()
    objectid = IntegerField()

    class Meta:
        db_table = 'character_creation_data'

class CharacterFaceData(BaseModel):
    faceid = PrimaryKeyField()
    gender = TextField()

    class Meta:
        db_table = 'character_face_data'

class CharacterForbiddenNames(BaseModel):
    forbidden_name = CharField(primary_key=True)

    class Meta:
        db_table = 'character_forbidden_names'

class CharacterHairData(BaseModel):
    gender = TextField()
    hairid = PrimaryKeyField()

    class Meta:
        db_table = 'character_hair_data'

class CharacterSkinData(BaseModel):
    skinid = UnknownField(primary_key=True)  # tinyint(3)

    class Meta:
        db_table = 'character_skin_data'

class CrcInfo(BaseModel):
    crc_integer = IntegerField()
    crc_string = CharField()
    filename = CharField(primary_key=True)

    class Meta:
        db_table = 'crc_info'

class CurseData(BaseModel):
    word = CharField(primary_key=True)

    class Meta:
        db_table = 'curse_data'

class DropData(BaseModel):
    chance = IntegerField()
    dropperid = IntegerField(index=True)
    flags = TextField()
    id = BigIntegerField(primary_key=True)
    itemid = IntegerField()
    maximum_quantity = IntegerField()
    minimum_quantity = IntegerField()
    questid = IntegerField()

    class Meta:
        db_table = 'drop_data'

class DropGlobalData(BaseModel):
    chance = IntegerField()
    continent = UnknownField()  # tinyint(3)
    flags = TextField()
    id = BigIntegerField(primary_key=True)
    itemid = IntegerField()
    maximum_level = UnknownField()  # tinyint(3)
    maximum_quantity = IntegerField()
    minimum_level = UnknownField()  # tinyint(3)
    minimum_quantity = IntegerField()
    questid = IntegerField()

    class Meta:
        db_table = 'drop_global_data'

class ItemConsumeData(BaseModel):
    accuracy = IntegerField()
    avoid = IntegerField()
    buff_time = IntegerField()
    carnival_points = IntegerField()
    create_item = IntegerField()
    cure_ailments = TextField()
    decrease_fatigue = IntegerField()
    decrease_hunger = IntegerField()
    defense_vs_curse = UnknownField()  # tinyint(3)
    defense_vs_darkness = UnknownField()  # tinyint(3)
    defense_vs_fire = UnknownField()  # tinyint(3)
    defense_vs_ice = UnknownField()  # tinyint(3)
    defense_vs_lightning = UnknownField()  # tinyint(3)
    defense_vs_poison = UnknownField()  # tinyint(3)
    defense_vs_seal = UnknownField()  # tinyint(3)
    defense_vs_stun = UnknownField()  # tinyint(3)
    defense_vs_weakness = UnknownField()  # tinyint(3)
    drop_up = TextField(null=True)
    drop_up_item = IntegerField()
    drop_up_item_range = IntegerField()
    drop_up_map_ranges = UnknownField()  # tinyint(3)
    effect = UnknownField()  # tinyint(3)
    flags = TextField()
    hp = IntegerField()
    hp_percentage = IntegerField()
    itemid = PrimaryKeyField()
    jump = IntegerField()
    magic_attack = IntegerField()
    magic_defense = IntegerField()
    morph = IntegerField()
    move_to = IntegerField()
    mp = IntegerField()
    mp_percentage = IntegerField()
    prob = UnknownField()  # tinyint(3)
    speed = IntegerField()
    weapon_attack = IntegerField()
    weapon_defense = IntegerField()

    class Meta:
        db_table = 'item_consume_data'

class ItemData(BaseModel):
    experience = IntegerField()
    flags = TextField()
    inventory = TextField()
    itemid = PrimaryKeyField()
    level_for_maker = IntegerField()
    max_level = UnknownField()  # tinyint(3)
    max_possession_count = UnknownField()  # tinyint(3)
    max_slot_quantity = IntegerField()
    min_level = UnknownField()  # tinyint(3)
    money = IntegerField()
    npc = IntegerField()
    price = IntegerField()
    state_change_item = IntegerField()

    class Meta:
        db_table = 'item_data'

class ItemEquipBonusExp(BaseModel):
    bonus_exp = IntegerField()
    itemid = IntegerField()
    req_seconds_held = IntegerField()

    class Meta:
        db_table = 'item_equip_bonus_exp'
        primary_key = CompositeKey('bonus_exp', 'itemid')

class ItemEquipData(BaseModel):
    accuracy = IntegerField()
    attack_speed = UnknownField()  # tinyint(3)
    avoid = IntegerField()
    dexterity = IntegerField()
    elemental_default = UnknownField()  # tinyint(3)
    equip_slots = TextField()
    flags = TextField()
    hands = IntegerField()
    heal_hp = UnknownField()  # tinyint(3)
    hp = IntegerField()
    inc_fire_damage = UnknownField()  # tinyint(3)
    inc_ice_damage = UnknownField()  # tinyint(3)
    inc_lightning_damage = UnknownField()  # tinyint(3)
    inc_poison_damage = UnknownField()  # tinyint(3)
    intelligence = IntegerField()
    itemid = PrimaryKeyField()
    jump = IntegerField()
    knockback = IntegerField()
    luck = IntegerField()
    magic_attack = IntegerField()
    magic_defense = IntegerField()
    mp = IntegerField()
    recovery = IntegerField()
    req_dex = IntegerField()
    req_fame = IntegerField()
    req_int = IntegerField()
    req_job = TextField()
    req_luk = IntegerField()
    req_str = IntegerField()
    scroll_slots = IntegerField()
    specialid = IntegerField()
    speed = IntegerField()
    strength = IntegerField()
    taming_mob = UnknownField()  # tinyint(3)
    traction = UnknownField()  # double
    weapon_attack = IntegerField()
    weapon_defense = IntegerField()

    class Meta:
        db_table = 'item_equip_data'

class ItemHalloweenData(BaseModel):
    itemid = PrimaryKeyField()

    class Meta:
        db_table = 'item_halloween_data'

class ItemMakerData(BaseModel):
    inc_max_hp = IntegerField()
    inc_max_mp = IntegerField()
    inc_req_level = UnknownField()  # tinyint(3)
    itemid = PrimaryKeyField()
    rand_option = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'item_maker_data'

class ItemMonsterCardMapRanges(BaseModel):
    end_map = IntegerField()
    itemid = IntegerField()
    start_map = IntegerField()

    class Meta:
        db_table = 'item_monster_card_map_ranges'
        primary_key = CompositeKey('itemid', 'start_map')

class ItemPetData(BaseModel):
    default_name = CharField()
    evolution_item = IntegerField()
    flags = TextField()
    hunger = UnknownField()  # tinyint(3)
    itemid = IntegerField(index=True)
    life = IntegerField()
    limited_life = IntegerField()
    req_level_for_evolution = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'item_pet_data'

class ItemPetEvolutions(BaseModel):
    chance = IntegerField()
    evolution_itemid = IntegerField()
    itemid = IntegerField()

    class Meta:
        db_table = 'item_pet_evolutions'
        primary_key = CompositeKey('evolution_itemid', 'itemid')

class ItemPetInteractions(BaseModel):
    closeness = UnknownField()  # tinyint(3)
    command = IntegerField()
    itemid = IntegerField()
    success = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'item_pet_interactions'
        primary_key = CompositeKey('command', 'itemid')

class ItemRandomMorphs(BaseModel):
    id = BigIntegerField(primary_key=True)
    itemid = IntegerField()
    morphid = UnknownField()  # tinyint(3)
    success = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'item_random_morphs'

class ItemRechargeableData(BaseModel):
    itemid = PrimaryKeyField()
    unit_price = UnknownField()  # double(2,1)
    weapon_attack = IntegerField()

    class Meta:
        db_table = 'item_rechargeable_data'

class ItemRewardData(BaseModel):
    effect = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    itemid = IntegerField()
    prob = IntegerField()
    quantity = IntegerField()
    rewardid = IntegerField()

    class Meta:
        db_table = 'item_reward_data'

class ItemScrollData(BaseModel):
    break_item = IntegerField()
    flags = TextField()
    iacc = IntegerField()
    iavo = IntegerField()
    idex = IntegerField()
    ihp = IntegerField()
    iint = IntegerField()
    ijump = IntegerField()
    iluk = IntegerField()
    imatk = IntegerField()
    imdef = IntegerField()
    imp = IntegerField()
    ispeed = IntegerField()
    istr = IntegerField()
    itemid = PrimaryKeyField()
    iwatk = IntegerField()
    iwdef = IntegerField()
    success = IntegerField()

    class Meta:
        db_table = 'item_scroll_data'

class ItemScrollTargets(BaseModel):
    id = BigIntegerField(primary_key=True)
    req_itemid = IntegerField()
    scrollid = IntegerField()

    class Meta:
        db_table = 'item_scroll_targets'

class ItemSkills(BaseModel):
    chance = UnknownField()  # tinyint(3)
    itemid = IntegerField()
    master_level = UnknownField()  # tinyint(3)
    req_skill_level = UnknownField()  # tinyint(3)
    skillid = IntegerField()

    class Meta:
        db_table = 'item_skills'
        primary_key = CompositeKey('itemid', 'master_level', 'skillid')

class ItemSummons(BaseModel):
    chance = IntegerField()
    id = BigIntegerField(primary_key=True)
    itemid = IntegerField(index=True)
    mobid = IntegerField()

    class Meta:
        db_table = 'item_summons'

class ItemTimelessLevels(BaseModel):
    accuracy_max = IntegerField()
    accuracy_min = IntegerField()
    avoidability_max = IntegerField()
    avoidability_min = IntegerField()
    dex_max = IntegerField()
    dex_min = IntegerField()
    experience = IntegerField()
    hp_max = IntegerField()
    hp_min = IntegerField()
    int_max = IntegerField()
    int_min = IntegerField()
    item_level = UnknownField()  # tinyint(3)
    itemid = IntegerField()
    jump_max = IntegerField()
    jump_min = IntegerField()
    luk_max = IntegerField()
    luk_min = IntegerField()
    magic_attack_max = IntegerField()
    magic_attack_min = IntegerField()
    magic_defense_max = IntegerField()
    magic_defense_min = IntegerField()
    mp_max = IntegerField()
    mp_min = IntegerField()
    speed_max = IntegerField()
    speed_min = IntegerField()
    str_max = IntegerField()
    str_min = IntegerField()
    weapon_attack_max = IntegerField()
    weapon_attack_min = IntegerField()
    weapon_defense_max = IntegerField()
    weapon_defense_min = IntegerField()

    class Meta:
        db_table = 'item_timeless_levels'
        primary_key = CompositeKey('item_level', 'itemid')

class ItemTimelessSkills(BaseModel):
    item_level = UnknownField()  # tinyint(3)
    itemid = IntegerField()
    probability = UnknownField()  # tinyint(3)
    skill_level = UnknownField()  # tinyint(3)
    skillid = IntegerField()

    class Meta:
        db_table = 'item_timeless_skills'
        primary_key = CompositeKey('itemid', 'skillid')

class MakerCreationData(BaseModel):
    catalyst = IntegerField()
    classid = TextField()
    itemid = IntegerField()
    quantity = IntegerField()
    req_equip = IntegerField()
    req_item = IntegerField()
    req_level = UnknownField()  # tinyint(3)
    req_maker_level = UnknownField()  # tinyint(3)
    req_money = IntegerField()
    upgrade_crystals = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'maker_creation_data'
        primary_key = CompositeKey('classid', 'itemid')

class MakerRecipes(BaseModel):
    itemid = IntegerField()
    quantity = IntegerField()
    req_item = IntegerField()

    class Meta:
        db_table = 'maker_recipes'
        primary_key = CompositeKey('itemid', 'req_item')

class MakerRewards(BaseModel):
    chance = UnknownField()  # tinyint(3)
    itemid = IntegerField()
    quantity = IntegerField()
    rewardid = IntegerField()

    class Meta:
        db_table = 'maker_rewards'
        primary_key = CompositeKey('itemid', 'rewardid')

class MapContinentData(BaseModel):
    continent = UnknownField()  # tinyint(3)
    map_cluster = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'map_continent_data'
        primary_key = CompositeKey('continent', 'map_cluster')

class MapData(BaseModel):
    damage_per_second = IntegerField()
    decrease_hp = UnknownField()  # tinyint(3)
    default_bgm = CharField()
    default_traction = UnknownField()  # double(20,15)
    field_limitations = TextField()
    field_type = TextField()
    flags = TextField()
    forced_return_map = IntegerField()
    link = IntegerField()
    map_ltx = IntegerField()
    map_lty = IntegerField()
    map_rbx = IntegerField()
    map_rby = IntegerField()
    mapid = PrimaryKeyField()
    min_level_limit = UnknownField()  # tinyint(3)
    mob_rate = UnknownField()  # double(13,11)
    protect_item = IntegerField()
    regen_rate = UnknownField()  # tinyint(3)
    return_map = IntegerField()
    ship_kind = UnknownField()  # tinyint(3)
    shuffle_name = CharField()
    time_limit = IntegerField()

    class Meta:
        db_table = 'map_data'

class MapFootholds(BaseModel):
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

class MapLife(BaseModel):
    flags = TextField()
    foothold = IntegerField()
    id = BigIntegerField(primary_key=True)
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

class MapPortals(BaseModel):
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

class MapSeats(BaseModel):
    mapid = IntegerField()
    seatid = IntegerField()
    x_pos = IntegerField()
    y_pos = IntegerField()

    class Meta:
        db_table = 'map_seats'
        primary_key = CompositeKey('mapid', 'seatid')

class MapTimeMob(BaseModel):
    end_hour = UnknownField()  # tinyint(3)
    mapid = PrimaryKeyField()
    message = CharField()
    mobid = IntegerField()
    start_hour = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'map_time_mob'

class McdbInfo(BaseModel):
    maple_locale = TextField()
    maple_version = IntegerField()
    subversion = IntegerField()
    test_server = UnknownField()  # tinyint(1)
    version = IntegerField()

    class Meta:
        db_table = 'mcdb_info'

class MobAttacks(BaseModel):
    attack_type = TextField(null=True)
    attackid = IntegerField()
    element = TextField(null=True)
    flags = TextField()
    mob_skill_level = IntegerField()
    mob_skillid = IntegerField()
    mobid = IntegerField()
    mp_burn = IntegerField()
    mp_cost = IntegerField()

    class Meta:
        db_table = 'mob_attacks'
        primary_key = CompositeKey('attackid', 'mobid')

class MobData(BaseModel):
    mobid = PrimaryKeyField()
    acc = IntegerField(db_column='accuracy')
    avoid = IntegerField(db_column='avoidability')
    carnival_points = IntegerField()
    chase_speed = IntegerField()
    damaged_by_mob_only = IntegerField()
    damaged_by_skill_only = IntegerField()
    remove_after = IntegerField(db_column='death_after')
    buff = IntegerField(db_column='death_buff')
    exp = IntegerField(db_column='experience')
    explode_hp = IntegerField()
    fire_modifier = TextField()
    fixed_damage = IntegerField()
    flags = TextField()
    holy_modifier = TextField()
    hp = IntegerField()
    hp_bar_bg_color = IntegerField()
    hp_bar_color = IntegerField()
    hp_recovery = IntegerField()
    ice_modifier = TextField()
    knockback = IntegerField()
    lightning_modifier = TextField()
    link = IntegerField()
    matk = IntegerField(db_column='magical_attack')
    mdef = IntegerField(db_column='magical_defense')
    level = IntegerField(db_column='mob_level')
    mp = IntegerField()
    mp_recovery = IntegerField()
    nonelemental_modifier = TextField()
    physical_attack = IntegerField()
    physical_defense = IntegerField()
    poison_modifier = TextField()
    speed = IntegerField()
    summon_type = IntegerField()
    traction = FloatField()

    class Meta:
        db_table = 'mob_data'

class MobSkills(BaseModel):
    effect_delay = IntegerField()
    id = BigIntegerField(primary_key=True)
    mobid = IntegerField()
    skill_level = IntegerField()
    skillid = IntegerField()

    class Meta:
        db_table = 'mob_skills'

class MobSummons(BaseModel):
    id = BigIntegerField(primary_key=True)
    mobid = IntegerField(index=True)
    summonid = IntegerField()

    class Meta:
        db_table = 'mob_summons'

class MonsterCardData(BaseModel):
    cardid = PrimaryKeyField()
    mobid = IntegerField()

    class Meta:
        db_table = 'monster_card_data'

class MorphData(BaseModel):
    flags = TextField()
    jump = IntegerField()
    morphid = PrimaryKeyField()
    speed = IntegerField()
    swim = UnknownField()  # double(4,1)
    traction = UnknownField()  # double(4,1)

    class Meta:
        db_table = 'morph_data'

class NpcData(BaseModel):
    flags = TextField()
    npcid = PrimaryKeyField()
    storage_cost = IntegerField()

    class Meta:
        db_table = 'npc_data'

class OxQuizData(BaseModel):
    answer = TextField()
    display = CharField()
    question = CharField()
    question_set = IntegerField()
    questionid = IntegerField()

    class Meta:
        db_table = 'ox_quiz_data'
        primary_key = CompositeKey('question_set', 'questionid')

class PhysicalDefenseData(BaseModel):
    class_ = UnknownField(db_column='class')  # tinyint(3)
    defense = IntegerField()
    player_level = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'physical_defense_data'
        primary_key = CompositeKey('class_', 'player_level')

class QuestAreaData(BaseModel):
    area_name = CharField()
    areaid = UnknownField(primary_key=True)  # tinyint(3)

    class Meta:
        db_table = 'quest_area_data'

class QuestData(BaseModel):
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

class QuestExclusiveMedals(BaseModel):
    questid = PrimaryKeyField()

    class Meta:
        db_table = 'quest_exclusive_medals'

class QuestRequests(BaseModel):
    objectid = IntegerField()
    quantity = IntegerField()
    quest_state = TextField()
    questid = IntegerField(index=True)
    request_type = TextField()

    class Meta:
        db_table = 'quest_requests'
        primary_key = CompositeKey('objectid', 'quest_state', 'questid')

class QuestRequiredJobs(BaseModel):
    questid = IntegerField()
    valid_jobid = IntegerField()

    class Meta:
        db_table = 'quest_required_jobs'
        primary_key = CompositeKey('questid', 'valid_jobid')

class QuestRewards(BaseModel):
    flags = TextField()
    gender = TextField()
    id = BigIntegerField(primary_key=True)
    job = IntegerField()
    job_tracks = TextField()
    master_level = IntegerField()
    prop = IntegerField()
    quantity = IntegerField()
    quest_state = TextField()
    questid = IntegerField(index=True)
    reward_type = TextField()
    rewardid = IntegerField()

    class Meta:
        db_table = 'quest_rewards'

class ReactorData(BaseModel):
    flags = TextField()
    link = IntegerField()
    max_states = UnknownField()  # tinyint(3)
    reactorid = PrimaryKeyField()

    class Meta:
        db_table = 'reactor_data'

class ReactorEventTriggerSkills(BaseModel):
    reactorid = IntegerField()
    skillid = IntegerField()
    state = UnknownField()  # tinyint(3)

    class Meta:
        db_table = 'reactor_event_trigger_skills'

class ReactorEvents(BaseModel):
    event_type = TextField()
    itemid = IntegerField()
    ltx = IntegerField()
    lty = IntegerField()
    next_state = UnknownField()  # tinyint(3)
    quantity = IntegerField()
    rbx = IntegerField()
    rby = IntegerField()
    reactorid = IntegerField(index=True)
    state = UnknownField()  # tinyint(3)
    timeout = IntegerField()

    class Meta:
        db_table = 'reactor_events'
        primary_key = CompositeKey('next_state', 'reactorid', 'state')

class Scripts(BaseModel):
    helper = UnknownField()  # tinyint(3)
    objectid = IntegerField()
    script = CharField()
    script_type = TextField()

    class Meta:
        db_table = 'scripts'
        primary_key = CompositeKey('helper', 'objectid', 'script_type')

class ShopData(BaseModel):
    npcid = IntegerField()
    recharge_tier = IntegerField()
    shopid = PrimaryKeyField()

    class Meta:
        db_table = 'shop_data'

class ShopItems(BaseModel):
    itemid = IntegerField()
    price = IntegerField()
    quantity = IntegerField()
    shopid = IntegerField()
    sort = IntegerField()

    class Meta:
        db_table = 'shop_items'
        primary_key = CompositeKey('shopid', 'sort')

class ShopRechargeData(BaseModel):
    itemid = IntegerField()
    price = UnknownField()  # double(2,1)
    tierid = IntegerField()

    class Meta:
        db_table = 'shop_recharge_data'
        primary_key = CompositeKey('itemid', 'tierid')

class SkillFamilyData(BaseModel):
    amount = IntegerField()
    buff_time = IntegerField()
    description = CharField()
    rep_cost = IntegerField()
    skill_type = TextField()
    skillid = PrimaryKeyField()
    target = TextField()
    title = CharField()

    class Meta:
        db_table = 'skill_family_data'

class SkillMobBanishData(BaseModel):
    destination = IntegerField()
    message = CharField()
    mobid = PrimaryKeyField()
    portal = CharField()

    class Meta:
        db_table = 'skill_mob_banish_data'

class SkillMobData(BaseModel):
    buff_time = IntegerField()
    chance = IntegerField()
    cooldown = IntegerField()
    hp_limit_percentage = IntegerField()
    ltx = IntegerField()
    lty = IntegerField()
    mp_cost = IntegerField()
    rbx = IntegerField()
    rby = IntegerField()
    skill_level = IntegerField()
    skillid = IntegerField()
    summon_effect = IntegerField()
    summon_limit = IntegerField()
    target_count = IntegerField()
    x_property = IntegerField()
    y_property = IntegerField()

    class Meta:
        db_table = 'skill_mob_data'

class SkillMobSummons(BaseModel):
    level = IntegerField(index=True)
    mobid = IntegerField()

    class Meta:
        db_table = 'skill_mob_summons'

class SkillMonsterCarnival(BaseModel):
    buff_time = IntegerField()
    buff_type = TextField()
    carnival_point_cost = IntegerField()
    mob_skill_level = UnknownField()  # tinyint(3)
    mob_skillid = UnknownField()  # tinyint(3)
    mobid = IntegerField()
    prop = UnknownField()  # tinyint(3)
    skill_type = TextField()
    skillid = UnknownField()  # tinyint(3)
    target_type = TextField()

    class Meta:
        db_table = 'skill_monster_carnival'
        primary_key = CompositeKey('skill_type', 'skillid')

class SkillPlayerData(BaseModel):
    flags = TextField()
    skill_type = TextField()
    skillid = PrimaryKeyField()
    weapon = IntegerField()

    class Meta:
        db_table = 'skill_player_data'

class SkillPlayerLevelData(BaseModel):
    accuracy = IntegerField()
    avoid = IntegerField()
    buff_time = IntegerField()
    bullet_cost = IntegerField()
    cooldown_time = IntegerField()
    critical_damage = UnknownField()  # tinyint(3)
    damage = IntegerField()
    fixed_damage = IntegerField()
    hit_count = UnknownField()  # tinyint(3)
    hp = IntegerField()
    hp_cost = IntegerField()
    item_cost = IntegerField()
    item_count = IntegerField()
    jump = IntegerField()
    ltx = IntegerField()
    lty = IntegerField()
    magic_atk = IntegerField()
    magic_def = IntegerField()
    mastery = UnknownField()  # tinyint(3)
    mob_count = UnknownField()  # tinyint(3)
    money_cost = IntegerField()
    morph = IntegerField()
    mp = IntegerField()
    mp_cost = IntegerField()
    optional_item_cost = IntegerField()
    prop = IntegerField()
    range = IntegerField()
    rbx = IntegerField()
    rby = IntegerField()
    skill_level = IntegerField()
    skillid = IntegerField()
    speed = IntegerField()
    str = IntegerField()
    weapon_atk = IntegerField()
    weapon_def = IntegerField()
    x_property = IntegerField()
    y_property = IntegerField()

    class Meta:
        db_table = 'skill_player_level_data'
        primary_key = CompositeKey('skill_level', 'skillid')

class SkillPlayerRequirementData(BaseModel):
    req_level = UnknownField()  # tinyint(3)
    req_skillid = IntegerField()
    skillid = IntegerField()

    class Meta:
        db_table = 'skill_player_requirement_data'
        primary_key = CompositeKey('req_skillid', 'skillid')

class Strings(BaseModel):
    label = CharField(index=True)
    object_type = TextField()
    objectid = IntegerField()

    class Meta:
        db_table = 'strings'
        primary_key = CompositeKey('object_type', 'objectid')

class TamingMobData(BaseModel):
    fatigue = UnknownField()  # tinyint(3)
    jump = IntegerField()
    speed = IntegerField()
    swim = UnknownField()  # double(4,1)
    tamingmobid = UnknownField(primary_key=True)  # tinyint(3)
    traction = UnknownField()  # double(4,1)

    class Meta:
        db_table = 'taming_mob_data'

class UserDropData(BaseModel):
    chance = IntegerField()
    dropperid = IntegerField(index=True)
    flags = TextField()
    id = BigIntegerField(primary_key=True)
    itemid = IntegerField()
    maximum_quantity = IntegerField()
    minimum_quantity = IntegerField()
    questid = IntegerField()

    class Meta:
        db_table = 'user_drop_data'

class UserShopData(BaseModel):
    npcid = IntegerField()
    recharge_tier = IntegerField()
    shopid = PrimaryKeyField()

    class Meta:
        db_table = 'user_shop_data'

class UserShopItems(BaseModel):
    itemid = IntegerField()
    price = IntegerField()
    quantity = IntegerField()
    shopid = IntegerField()
    sort = IntegerField()

    class Meta:
        db_table = 'user_shop_items'
        primary_key = CompositeKey('shopid', 'sort')

