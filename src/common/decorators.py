from . import packetbuilder

def packet(opcode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            pb = packetbuilder.PacketBuilder()
            pb.write_short(opcode)
            return func(pb, *args, **kwargs)
        return wrapper
    return decorator
