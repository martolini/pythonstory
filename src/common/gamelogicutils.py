from . import enums


def get_inventory(id):
    return id / 1000000


def is_cashslot(slot):
    return abs(slot) > 100


def is_pet(id):
    return id / 100 * 100 == 5000000


def is_equip(id):
    return get_inventory(id) == enums.Inventory.EQUIP
