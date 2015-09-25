from pythonstory.world import factory as worldfactory, models as worldmodels
from pythonstory.channel import factory as channelfactory
from pythonstory.common import settings
from twisted.internet import reactor


def runserver():
    worlds = [worldmodels.World(i, **w) for i, w in enumerate(settings.WORLDS)]
    worldfac = worldfactory.WorldFactory(worlds=worlds)
    for world in worlds:
        for c in xrange(len(world.channels)):
            channel = channelfactory.ChannelFactory(key=c+1,
                                                    world=world,
                                                    worldfac=worldfac)
            port = 7575 + channel.key - 1
            port += world.key * 100
            channel.port = port
            world.channels[c] = channel
            reactor.listenTCP(channel.port, channel)

    reactor.listenTCP(8484, worldfac)
    reactor.run()

if __name__ == '__main__':
    runserver()
