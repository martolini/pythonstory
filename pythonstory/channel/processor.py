from ..common import processor, recvopcodes
from ..common import handlers as commonhandlers
from . import handlers as channelhandlers
from .player import handlers as playerhandlers
from .quest import handlers as questhandlers
from .npc import handlers as npchandlers
from .mob import handlers as mobhandlers


class ChannelPacketProcessor(processor.BasePacketProcessor):
    ignored_opcodes = (
        recvopcodes.PLAYER_UPDATE,
        recvopcodes.TEMP_SKILL
    )

    handlers = {
        recvopcodes.PONG: commonhandlers.pong,
        recvopcodes.PLAYER_LOAD: channelhandlers.load_player,
        recvopcodes.MOVE_PLAYER: playerhandlers.move_player,
        recvopcodes.CHANGE_MAP: playerhandlers.change_map,
        recvopcodes.CHANGE_KEYMAP: playerhandlers.change_keymap,
        recvopcodes.GENERAL_CHAT: playerhandlers.handle_chat,
        recvopcodes.QUEST_ACTION: questhandlers.quest_action,
        recvopcodes.NPC_ACTION: npchandlers.npc_action,
        recvopcodes.CLOSE_RANGE_ATTACK: playerhandlers.meele_attack,
        recvopcodes.MOVE_LIFE: mobhandlers.move_mob,
        recvopcodes.CHANGE_MAP_SPECIAL: playerhandlers.change_map_special,
    }
