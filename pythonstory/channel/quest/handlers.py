from .models import Quest
from . import packets as questpackets


def quest_action(packet, client):
    action = packet.read_byte()
    questid = packet.read_short()
    Quest.for_character(client.character, questid)
    print "Action {}".format(action)
    if action == 1:  # Starting quest
        npcid = packet.read_int()
        if packet.bytes_available >= 4:
            packet.read_int()
        client.send(questpackets.accept_quest(questid, npcid))
        client.send(questpackets.accept_quest_notice(questid))
    elif action == 2:  # Quest completed
        npcid = packet.read_int()
        Quest.complete(questid)
        client.send(questpackets.complete_quest(questid))
