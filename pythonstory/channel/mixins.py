from pythonstory.common.helperclasses import Point


class MovableMixin(object):
    def __init__(self, xpos=0, ypos=0, stance=0, foothold=0):
        self.pos = Point(xpos, ypos)
        self.stance = stance
        self.foothold = foothold
        return super(MovableMixin, self).__init__()

    def move(self, x, y, foothold, stance):
        self.pos.x = x
        self.pos.y = y
        self.foothold = foothold
        self.stance = stance

    def handle_movement(self, packet):
        foothold = 0
        stance = 0
        x = 0
        y = 0
        n_commands = packet.read_byte()
        for i in xrange(n_commands):
            mtype = packet.read_byte()
            if mtype in (0, 15, 17):
                x = packet.read_short()
                y = packet.read_short()
                packet.read_int()
                foothold = packet.read_short()
                stance = packet.read_byte()
                packet.read_short()
            elif mtype in (1, 2, 6, 12, 13, 16):
                x = packet.read_short()
                y = packet.read_short()
                stance = packet.read_byte()
                foothold = packet.read_short()
            elif mtype in (3, 4, 7, 8, 9, 14):
                packet.skip(9)
            elif mtype == 10:
                packet.read_byte()
                print 'Should change equip, wtf'
            elif mtype == 11:
                x = packet.read_short()
                y = packet.read_short()
                foothold = packet.read_short()
                stance = packet.read_byte()
                packet.read_short()
            elif mtype == 15:
                x = packet.read_short()
                y = packet.read_short()
                packet.read_int()
                packet.read_short()
                foothold = packet.read_short()
                stance = packet.read_byte()
                packet.read_short()
            elif mtype == 21:
                packet.skip(3)
            else:
                print 'Unknown movement type {}'.format(mtype)
                break

        self.move(x, y, foothold, stance)
