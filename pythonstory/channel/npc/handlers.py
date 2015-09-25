from . import packets as npcpackets


def npc_action(packet, client):
    size = packet.bytes_available
    if size == 6:
        i = packet.read_int()
        s = packet.read_short()
        client.send(npcpackets.npc_talk(i, s))
    elif size > 6:
        arr = [packet.read_byte() for _ in xrange(size - 9)]
        client.send(npcpackets.npc_move(arr))
