from peewee import *
from ..common.models import BaseModel
from datetime import datetime


class Account(BaseModel):
    name = CharField(unique=True)
    password = CharField(max_length=128)
    pin = CharField(max_length=10, null=True)
    pic = CharField(max_length=26, null=True)
    loggedin = IntegerField(default=0)
    last_login = DateTimeField(null=True)
    created_at = DateTimeField(default=datetime.now())
    birthday = DateField(null=True)
    banned = IntegerField(default=0)
    banreason = TextField(null=True)
    gm = IntegerField(default=0)
    macs = TextField(null=True)
    nx_credit = IntegerField(default=0)
    maple_points = IntegerField(default=0)
    nx_prepaid = IntegerField(default=0)
    character_slots = IntegerField(default=5)
    gender = IntegerField(default=0)
    tempban = DateTimeField(null=True)
    greason = IntegerField(default=0)
    tos = IntegerField(default=0)

    @classmethod
    def login(cls, username, password):
        account = None
        try:
            account = cls.select().where(
                (cls.name == username) &
                (cls.password == password)
            ).get()
        except cls.DoesNotExist:
            return None
        return account


class World:
    def __init__(self, key, name, flag, eventmsg,
                 exprate, droprate, mesorate,
                 bossdroprate, recommended, channels):
        self.key = key  # 0 indexed
        self.name = name
        self.flag = flag
        self.eventmsg = eventmsg
        self.exprate = exprate
        self.droprate = droprate
        self.mesorate = mesorate
        self.bossdroprate = bossdroprate
        self.recommended = recommended
        self.channels = [None] * channels
