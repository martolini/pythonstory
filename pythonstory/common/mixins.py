from pythonstory.channel.models import Character


class CharacterCacheMixin(object):
    def __init__(self, *args, **kwargs):
        self.character_cache = {}
        super(CharacterCacheMixin, self).__init__(*args, **kwargs)

    def get_character(self, key):
        if key not in self.character_cache:
            c = Character.get(id=key)
            self.character_cache[key] = c
        return self.character_cache[key]

    def set_character(self, character):
        self.character_cache[character.id] = character
