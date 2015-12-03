from .models import Quest


def quest_action(packet, client):
    action = packet.read_byte()
    questid = packet.read_short()
    quest = Quest.for_character(client.character, questid)
    if action == 1:  # Starting quest
        npcid = packet.read_int()
        quest.start(npcid, client)
    elif action == 2:  # Quest completed
        npcid = packet.read_int()
        quest.complete(client)
    else:
        print 'Questaction {} not handled yet.'.format(action)
