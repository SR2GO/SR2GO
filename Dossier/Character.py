import json
from collections import namedtuple

class JSONCompatible:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Karma(JSONCompatible):
    def __init__(self, total = None, remaining = None):
        self.Total = 0
        self.Remaining = 0

class CurrentDamage(JSONCompatible):
    def __init__(self, physical = None, stun = None):
        self.Physical = physical or 0
        self.Stun = stun or 0

class Attribute(JSONCompatible):
    def __init__(self, name = None, natural = None, augmented = None, naturalMax = None):
        self.Name = name or ""
        self.Natural = natural or 0
        self.Augmented = augmented or 0
        self.NaturalMax = naturalMax or 0

class Skill(JSONCompatible):
    def __init__(self):
        self.Name = ""
        self.Rank = 0
        self.LinkedAttribute = ""

class Quality(JSONCompatible):
    def __init__(self):
        self.Name = ""
        self.Type = ""  # Positive or Negative
        self.Cost = 0

class Contact(JSONCompatible):
    def __init__(self):
        self.Name = ""
        self.Connection = 0
        self.Loyality = 0
        self.Description = ""

class Character(JSONCompatible):
    """Kapselt einen Character. Die Struktur basiert auf dem Datenformat von Chummer."""
    def __init__(self):
        self.Name = ""
        self.Metatype = ""
        self.Money = 0
        self.Karma = Karma(total = 0, remaining = 0)
        self.Awakened = ""
        self.Magic = 0
        self.Essence = 0
        self.Edge = 0
        self.Passes = 0
        self.CurrentDamage = CurrentDamage(physical=0, stun=0)
        self.Attributes = [
            Attribute("STR", 1, 1, 6),
            Attribute("KON", 1, 1, 6),
            Attribute("GES", 1, 1, 6),
            Attribute("LOG", 1, 1, 6),
            Attribute("WIL", 1, 1, 6),
            Attribute("INT", 1, 1, 6),
            Attribute("CHA", 1, 1, 6)
        ]
        self.Skills = []
        self.Qualities = []
        self.Contacts = []

c = Character()
print(c.to_JSON())