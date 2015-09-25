from ..common import processor, recvopcodes
from ..common import handlers as commonhandlers
from . import handlers as channelhandlers
from .player import handlers as playerhandlers
from .quest import handlers as questhandlers
from .npc import handlers as npchandlers


class ChannelPacketProcessor(processor.BasePacketProcessor):
    ignored_opcodes = (
        recvopcodes.CHANGE_MAP_SPECIAL,
    )

    handlers = {
        recvopcodes.PONG: commonhandlers.pong,
        recvopcodes.PLAYER_LOAD: channelhandlers.load_player,
        recvopcodes.MOVE_PLAYER: playerhandlers.move_player,
        recvopcodes.CHANGE_MAP: playerhandlers.change_map,
        recvopcodes.CHANGE_KEYMAP: playerhandlers.change_keymap,
        recvopcodes.GENERAL_CHAT: playerhandlers.handle_chat,
        recvopcodes.QUEST_ACTION: questhandlers.quest_action,
        recvopcodes.NPC_ACTION: npchandlers.npc_action
    }
