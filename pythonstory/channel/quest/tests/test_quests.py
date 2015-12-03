import unittest
from pythonstory.channel.protocol import ChannelProtocol
from pythonstory.world.models import Account
from pythonstory.channel.models import Character
from ..models import Quest


class QuestTests(unittest.TestCase):
    def setUp(self):
        client = ChannelProtocol()
        client.send = lambda x: None
        a = Account.create(name='test', password='test', id=918171)
        character = Character.create(id=91817161, account=a, name='test')
        client.character = character
        self.client = client

    def test_complete_quest(self):
        exp = self.client.character.exp
        q = Quest.for_character(self.client.character, 1031)
        q.complete(self.client)
        self.assertEqual(exp+5, self.client.character.exp)

    def tearDown(self):
        self.client.character.account.delete_instance()
        self.client.character.delete_instance()
