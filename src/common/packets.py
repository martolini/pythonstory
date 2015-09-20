from . import decorators, sendopcodes
from time import time as timenow


@decorators.packet(sendopcodes.PING)
def ping(builder, client):
    client.lastping = timenow()
    return builder.get_packet()
