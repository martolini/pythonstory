from time import time as timenow


def pong(packet, client):
    client.latency = (timenow() - client.lastping) / 2
