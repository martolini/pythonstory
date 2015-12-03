import unittest
from ..models import Character
from ..protocol import ChannelProtocol
from pythonstory.world.models import Account


class CharacterTest(unittest.TestCase):
    def setUp(self):
        a = Account.create(name='test', password='test')
        c = Character.create(account=a, name='test')
        self.client = ChannelProtocol()
        self.client.character = c
        self.client.send = lambda x: None

    def test_levelup(self):
        self.client.gain_exp(20)
        c = self.client.character
        self.assertEqual(c.level, 2)
        self.assertEqual(c.exp, 5)
        self.assertEqual(c.str, 17)

    def tearDown(self):
        self.client.character.account.delete_instance()
        self.client.character.delete_instance()
