# Class of Cards
class TarotCard:
    def __init__(self, archetype, subtype, name, meaning):
        self.archetype = archetype
        self.type = subtype
        self.name = name
        self.meaning = meaning

    def __getArch__(self):
        return self.archetype

    def __getType__(self):
        return self.type

    def __getPath__(self):
        return str(self.archetype) + str(self.type) + ".jpg"

    def __getName__(self):
        return self.name

    def __getMeaning__(self):
        return self.meaning
