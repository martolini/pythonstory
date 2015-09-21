from . import packets as channelpackets
from .map import models as mapmodels


def load_player(packet, client):
    char_id = packet.read_int()
    character = client.factory.world_factory.get_character(char_id)

    character.channel = client.factory.key
    client.character = character

    # TODO BUFFS
    # TODO DUEY
    client.send(channelpackets.char_info(character, client.factory.key))
    client.send(channelpackets.keymap(character))
    # client.send(channelpackets.skillmacros(character)) NOT IMPLEMENTED
    # client.send(channelpackets.buddy_list(character)) NOT IMPLEMENTED
    # client.send(channelpackets.load_family(character)) NOT IMPLEMENTED
    # TODO NOTES
    # TODO PARTY
    mapmodels.Map.get(character.map, client.factory.key).add_client(client)
