from peewee import SqliteDatabase


WORLDS = [
    {
        'name': 'Scania',
        'flag': 1,
        'eventmsg': 'Event message',
        'exprate': 1,
        'droprate': 1,
        'mesorate': 1,
        'bossdroprate': 1,
        'recommended': 'Why not.',
        'channels': 3
    }
]

HOST_IP = '192.168.1.95'

DATABASES = {
    'default': SqliteDatabase('maple.db'),
    'static': SqliteDatabase('staticdb.sqlite'),
    'test': SqliteDatabase(':memory')
}

DEFAULT_KEYMAP = {
    2: (4, 10),
    3: (4, 12),
    4: (4, 13),
    5: (4, 18),
    6: (4, 24),
    7: (4, 21),
    16: (4, 8),
    17: (4, 5),
    18: (4, 0),
    19: (4, 4),
    23: (4, 1),
    24: (4, 25),
    25: (4, 19),
    26: (4, 14),
    27: (4, 15),
    29: (5, 52),
    31: (4, 2),
    33: (4, 26),
    34: (4, 17),
    35: (4, 11),
    37: (4, 3),
    38: (4, 20),
    40: (4, 16),
    41: (4, 23),
    43: (4, 9),
    44: (5, 50),
    45: (5, 51),
    46: (4, 6),
    48: (4, 22),
    50: (4, 7),
    56: (5, 53),
    57: (5, 54),
    59: (6, 100),
    60: (6, 101),
    61: (6, 102),
    62: (6, 103),
    63: (6, 104),
    64: (6, 105),
    65: (6, 1)
}
