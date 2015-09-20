class MovableMixin(object):
    def __init__(self, *args, **kwargs):
        self._xpos = 0
        self._ypos = 0
        self._foothold = 0
        self._stance = 0
        super(MovableMixin, self).__init__(*args, **kwargs)

    def move(self, x, y, foothold, stance):
        self._xpos = x
        self._ypos = y
        self._foothold = foothold
        self._stance = stance
