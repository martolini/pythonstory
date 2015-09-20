class World:
  def __init__(self, key, name, flag, eventmsg, exprate, droprate, mesorate, bossdroprate, recommended):
    self.key = key
    self.name = name
    self.flag = flag
    self.eventmsg = eventmsg
    self.exprate = exprate
    self.droprate = droprate
    self.mesorate = mesorate
    self.bossdroprate = bossdroprate
    self.recommended = recommended
    self.channels = []