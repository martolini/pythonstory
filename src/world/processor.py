from ..common import processor, recvopcodes
from ..common import handlers as commonhandlers
from . import handlers as worldhandlers


class WorldPacketProcessor(processor.BasePacketProcessor):
    ignored_opcodes = (
                       recvopcodes.WTF_STARTUP_SHIT,
                       recvopcodes.CLIENT_START_ERROR,
                       recvopcodes.PLAYER_DC,
                       recvopcodes.PLAYER_UPDATE
                       )
    handlers = {
        recvopcodes.PONG: commonhandlers.pong,
        recvopcodes.LOGIN_PASSWORD: worldhandlers.login,
        recvopcodes.SERVERLIST_REQUEST: worldhandlers.serverlist,
        recvopcodes.SERVERLIST_REREQUEST: worldhandlers.serverlist,
        recvopcodes.SERVERSTATUS_REQUEST: worldhandlers.server_status_load,
        recvopcodes.CHARLIST_REQUEST: worldhandlers.charlist,
        recvopcodes.CHECK_CHAR_NAME: worldhandlers.check_charname,
        recvopcodes.CREATE_CHAR: worldhandlers.create_character,
        recvopcodes.CHAR_SELECTED: worldhandlers.character_selected,
    }
