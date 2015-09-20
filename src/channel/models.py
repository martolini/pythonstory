from peewee import ForeignKeyField, IntegerField,\
    DateTimeField, BooleanField, CharField,\
    BigIntegerField
from datetime import datetime
import re
from ..common.models import BaseModel
from ..world.models import Account
from ..common import enums, gamelogicutils, staticmodels, settings
from .map.mixins import MovableMixin


class Character(MovableMixin, BaseModel):
    account = ForeignKeyField(Account, related_name='characters')
    world = IntegerField(default=0)
    name = CharField(max_length=11)
    level = IntegerField(default=1)
    exp = IntegerField(default=0)
    gachaexp = IntegerField(default=0)
    str = IntegerField(default=12)
    dex = IntegerField(default=5)
    luk = IntegerField(default=4)
    int = IntegerField(default=4)
    hp = IntegerField(default=50)
    mp = IntegerField(default=5)
    maxhp = IntegerField(default=50)
    maxmp = IntegerField(default=5)
    meso = IntegerField(default=0)
    hp_mp_used = IntegerField(default=0)
    job = IntegerField(default=0)
    skin_color = IntegerField(default=0)
    gender = IntegerField(default=0)
    fame = IntegerField(default=0)
    hair = IntegerField(default=0)
    face = IntegerField(default=0)
    ap = IntegerField(default=0)
    sp = IntegerField(default=0)
    map = IntegerField(default=0)
    spawn_point = IntegerField(default=0)
    gm = IntegerField(default=0)
    party = IntegerField(default=0)
    buddy_capacity = IntegerField(default=25)
    created_at = DateTimeField(default=datetime.now())
    rank = IntegerField(default=1)
    rank_move = IntegerField(default=0)
    job_rank = IntegerField(default=1)
    job_rank_move = IntegerField(default=0)
    # Missing guild/rank
    # Missing messenger
    # missing mount
    # missing omok
    # missing matchcard
    merchant_mesos = IntegerField(default=0)
    has_merchant = BooleanField(default=0)
    equip_slots = IntegerField(default=24)
    use_slots = IntegerField(default=24)
    setup_slots = IntegerField(default=24)
    etc_slots = IntegerField(default=24)
    # no family
    # missing monsterbook
    # missing alliance
    # missing vanquisher
    dojo_points = IntegerField(default=0)
    last_dojo_stage = IntegerField(default=0)
    finished_dojo_tutorial = BooleanField(default=False)

    # Ingame stuff, non DB related

    @classmethod
    def name_is_available(cls, name):
        if not re.match(r'[a-zA-Z0-9_-]{3,12}', name):
            return False
        if 'gm' in name:
            return False
        return cls.select().where(cls.name == name).count() == 0


class Item(BaseModel):
    type = IntegerField(default=1)
    character = ForeignKeyField(Character, related_name='inventoryitems')
    itemid = IntegerField()
    inventory = IntegerField()
    slot = IntegerField()
    quantity = IntegerField(default=1)
    petid = IntegerField(default=-1)
    expiration = BigIntegerField(default=-1)
    gift_from = CharField(max_length=26, null=True)
    scroll_slots = IntegerField(default=0)
    level = IntegerField(default=0)
    str = IntegerField(default=0)
    dex = IntegerField(default=0)
    int = IntegerField(default=0)
    luk = IntegerField(default=0)
    hp = IntegerField(default=0)
    mp = IntegerField(default=0)
    watk = IntegerField(default=0)
    matk = IntegerField(default=0)
    wdef = IntegerField(default=0)
    mdef = IntegerField(default=0)
    acc = IntegerField(default=0)
    avoid = IntegerField(default=0)
    hands = IntegerField(default=0)
    speed = IntegerField(default=0)
    jump = IntegerField(default=0)
    locked = IntegerField(default=0)
    vicious = IntegerField(default=0)
    itemlevel = IntegerField(default=1)
    itemexp = IntegerField(default=0)
    ringid = IntegerField(default=-1)
    flag = IntegerField(default=0)

    class Meta:
        db_table = 'inventory_item'

    @classmethod
    def create(cls, itemid, character, slot, *args, **kwargs):
        inventory = gamelogicutils.get_inventory(itemid)
        item = Item()
        if inventory == enums.Inventory.EQUIP:
            sequip = staticmodels.ItemEquipData.from_id(itemid=itemid)
            item = Item(
                character=character,
                slot=slot,
                inventory=inventory,
                itemid=itemid,
                str=sequip.str,
                dex=sequip.dex,
                int=sequip.int,
                luk=sequip.luk,
                hp=sequip.hp,
                mp=sequip.mp,
                watk=sequip.watk,
                wdef=sequip.wdef,
                matk=sequip.matk,
                mdef=sequip.mdef,
                acc=sequip.acc,
                avoid=sequip.avoid,
                hands=sequip.hands,
                jump=sequip.jump,
                speed=sequip.jump,
                *args, **kwargs
            )
            item.save()
        elif inventory == enums.Inventory.ETC:
            return super(Item, item).create(
                itemid=itemid,
                character=character,
                slot=slot,
                inventory=inventory,
                *args, **kwargs
            )
        else:
            raise Exception("Item not implemented yet")
        return item

    @classmethod
    def get_inventory_for(cls, character, inventory):
        return (cls
                .select(cls.itemid, cls.slot)
                .where((cls.inventory == inventory) &
                       (cls.character == character))
                )

    @classmethod
    def get_equips_for(cls, character):
        return cls.get_inventory_for(character, enums.Inventory.EQUIP)

    @classmethod
    def get_etcs_for(cls, character):
        return cls.get_inventory_for(character, enums.Inventory.ETC)


class Keymap(BaseModel):
    character = ForeignKeyField(Character, related_name='keymaps')
    key = IntegerField(default=0)
    type = IntegerField(default=0)
    action = IntegerField(default=0)

    @classmethod
    def for_character(cls, character):
        keymap = {
            x.key: (x.type, x.action)
            for x in (
                cls.select(cls.key, cls.type, cls.action)
                .where(cls.character == character)
            )
        }
        for key in xrange(90):
            if key in keymap:
                yield keymap[key]
            else:
                yield (0, 0)

    @classmethod
    def handle_changes(cls, changes, character):
        inserts, deletes = [], []
        for k, t, a in changes:
            if t != 0:
                inserts.append(
                    {'key': k, 'type': t, 'action': a, 'character': character}
                )
            else:
                deletes.append(k)
        cls.insert_many(inserts).execute()
        cls.delete().where(
            (cls.character == character) & (cls.key << deletes)
        ).execute()

    @classmethod
    def create_default(cls, character):
        keymaps = (
            {
                'key': key,
                'type': ktype,
                'action': action,
                'character': character
            } for key, (ktype, action) in settings.DEFAULT_KEYMAP
        )
        cls.insert_many(keymaps)
