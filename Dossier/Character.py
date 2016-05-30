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
    def __init__(self, name=None):
        self.Name = name or ""
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


if __name__ == "__main__":
    print("Run Main.py !")

"""
This can be added to the character as either some static load_XML method or a ctor argument.

from xml.dom import minidom
#from xml.dom.minidom import parse
#from xml.dom.minidom import
import re
import os
xml_fname = open('C:\\Users\\Lukas\\Desktop\\test.xml')
xml = minidom.parse(xml_fname) # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()

#print(pretty_xml_as_string)


attributes = xml.getElementsByTagName("Attributes")
attributes = attributes.item(0)
pretty_xml_as_string = attributes.toprettyxml()
#print(pretty_xml_as_string)
#for Attributes in attributes:
naturalValue = attributes.getElementsByTagName("naturalValue")
for idx, item in enumerate(naturalValue):
    text=item.toprettyxml()
    m = re.search('<.+?>(.+?)<.+?>', text)
    if m:
        out = m.group(1)
  #  print(out)
    #print(item.toprettyxml())


attribute_body = xml.getElementsByTagName('Attribute')
attribute_body_out = attribute_body.item(0).toprettyxml()
attribute_body_out = attribute_body_out.split()
m = re.search('<.+?>(.+?)<.+?>', attribute_body_out[2])
attribute_body_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', attribute_body_out[3])
attribute_body_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', attribute_body_out[4])
attribute_body_naturalMaximum = m.group(1)

print(attribute_body_naturalValue,attribute_body_augmentedValue,attribute_body_naturalMaximum)
"""

