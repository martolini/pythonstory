from peewee import ForeignKeyField, IntegerField

# from pythonstory.common.staticmodels import QuestData
from pythonstory.common.models import BaseModel
from pythonstory.channel.models import Character
import time


class Quest(BaseModel):
    character = ForeignKeyField(Character)
    questid = IntegerField()
    status = IntegerField(default=0)

    @classmethod
    def for_character(cls, character, questid):
        quest, _ = cls.get_or_create(
                                  character=character.id,
                                  questid=questid
                                  )
        return quest

    @classmethod
    def connect_data(cls, builder, character):
        qset = Quest.select().where(cls.character == character)
        active = [q for q in qset if q.status == 0]
        completed = [q for q in qset if q.status == 1]
        builder.write_short(len(active))
        for quest in active:
            (builder
             .write_short(quest.questid)
             .write_string("")
             )
        builder.write_short(len(completed))
        for quest in completed:
            (builder
             .write_short(quest.questid)
             .write_long(int(time.time()))
             )

    @classmethod
    def complete(cls, questid):
        cls.update(status=1).where(cls.questid == questid).execute()
