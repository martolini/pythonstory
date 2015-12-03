from peewee import ForeignKeyField, IntegerField

from pythonstory.common.staticmodels import QuestRewards
from pythonstory.common.models import BaseModel
from pythonstory.channel.models import Character
from . import packets
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

    def get_rewards(self, start=True):
        return QuestRewards.select().where(
                  (QuestRewards.questid == self.questid) &
                  (QuestRewards.quest_state == ('start' if start else 'end')))

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

    def start(self, npcid, client=None):
        client.send(packets.accept_quest(self.questid, npcid))
        client.send(packets.accept_quest_notice(self.questid))

    def complete(self, client):
        rewards = self.get_rewards(start=False)
        for reward in rewards:
            if reward.reward_type == 'exp':
                client.gain_exp(reward.rewardid)
            elif reward.reward_type == 'item':
                client.receive_item(reward.rewardid, reward.quantity)
        Quest.update(status=1).where(Quest.questid == self.questid).execute()
        client.send(packets.complete_quest(self.questid))
