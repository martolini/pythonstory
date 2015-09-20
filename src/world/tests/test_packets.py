import unittest
from ..packets import charlist
from ..models import Account


class PacketTest(unittest.TestCase):

    def setUp(self):
        self.account = Account.create(id=999, name='test', password='test')

    def test_charlist(self):
        self.assertEqual(type(self.account), Account)
        packet = charlist(self.account)
        self.assertEqual(len(packet), 9)

    def tearDown(self):
        self.account.delete_instance()
