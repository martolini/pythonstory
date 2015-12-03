

class BasePacketProcessor(object):
    """
    Abstract packet processor, handles the packet
    handlers = {OPCODE: func}
    """

    handlers = {}  # {OPCODE: function}
    ignored_opcodes = set()

    @classmethod
    def handle_packet(cls, packet, client):
        if packet.opcode in cls.handlers:
            try:
                return cls.handlers[packet.opcode](packet, client)
            except:
                import traceback
                print traceback.format_exc()
                return
        if packet.opcode not in cls.ignored_opcodes:
            print '{} Could not handle opcode {}'.format(
                                        cls.__name__,
                                        hex(packet.opcode)
            )
