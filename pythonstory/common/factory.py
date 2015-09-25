from twisted.internet import protocol

class MapleFactory(protocol.Factory, object):
    protocol = None

    def __init__(self):
        self.connections = []
