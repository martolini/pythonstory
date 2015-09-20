import unittest
from src.common.staticmodels import *
from src.common import enums


class StaticModelTest(unittest.TestCase):
    def test_itemequipdata(self):
        item = ItemEquipData.get(ItemEquipData.item == 1000000).get()
        self.assertEqual(item.item_id, 1000000)
        self.assertEqual(len(item.req_job), 6)
        self.assertTrue(enums.MapleJob.WARRIOR in item.req_job)
