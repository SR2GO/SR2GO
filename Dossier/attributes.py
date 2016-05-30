from xml.dom import minidom
import re


#init class

def __init__(self):
    self.data = []
    self.edge = 5



#opening xml file
xml_fname = open('test.xml')
_xml = minidom.parse(xml_fname) # or xml.dom.minidom.parseString(xml_string)

#loading attributes
_attribute = _xml.getElementsByTagName('Attribute')
##loading body attribute
_attribute_body = _attribute.item(0).toprettyxml()
_attribute_body = _attribute_body.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_body[2])
_attribute_body_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_body[3])
_attribute_body_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_body[4])
_attribute_body_naturalMaximum = m.group(1)

##loading agility attribute
_attribute_agility = _attribute.item(1).toprettyxml()
_attribute_agility = _attribute_agility.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_agility[2])
_attribute_agility_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_agility[3])
_attribute_agility_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_agility[4])
_attribute_agility_naturalMaximum = m.group(1)

##loading reaction attribute
_attribute_reaction = _attribute.item(2).toprettyxml()
_attribute_reaction = _attribute_reaction.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_reaction[2])
_attribute_reaction_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_reaction[3])
_attribute_reaction_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_reaction[4])
_attribute_reaction_naturalMaximum = m.group(1)

##loading strength attribute
_attribute_strength= _attribute.item(3).toprettyxml()
_attribute_strength = _attribute_strength.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_strength[2])
_attribute_strength_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_strength[3])
_attribute_strength_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_strength[4])
_attribute_strength_naturalMaximum = m.group(1)

## charisma
_attribute_charisma= _attribute.item(4).toprettyxml()
_attribute_charisma = _attribute_charisma.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_charisma[2])
_attribute_charisma_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_charisma[3])
_attribute_charisma_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_charisma[4])
_attribute_charisma_naturalMaximum = m.group(1)

## intuition
_attribute_intuition= _attribute.item(5).toprettyxml()
_attribute_intuition = _attribute_intuition.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_intuition[2])
_attribute_intuition_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_intuition[3])
_attribute_intuition_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_intuition[4])
_attribute_intuition_naturalMaximum = m.group(1)

## logic
_attribute_ilogic= _attribute.item(6).toprettyxml()
_attribute_ilogic = _attribute_ilogic.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_ilogic[2])
_attribute_ilogic_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_ilogic[3])
_attribute_ilogic_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_ilogic[4])
_attribute_ilogic_naturalMaximum = m.group(1)

##willpower
_attribute_willpower= _attribute.item(7).toprettyxml()
_attribute_willpower = _attribute_willpower.split()
m = re.search('<.+?>(.+?)<.+?>', _attribute_willpower[2])
_attribute_willpower_naturalValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_willpower[3])
_attribute_willpower_augmentedValue = m.group(1)
m = re.search('<.+?>(.+?)<.+?>', _attribute_willpower[4])
_attribute_willpower_naturalMaximum = m.group(1)

#loading edge
_edge = _xml.getElementsByTagName('Edge')
##edge
_attribute_edge = _edge.item(0).toprettyxml()
m = re.search('<.+?>(.+?)<.+?>', _attribute_edge)
_attribute_edge = m.group(1)

def getEdge(self):
    return _attribute_edge
def setEdge(self, x):
    self.edge = x
_edge = property(getEdge, setEdge)