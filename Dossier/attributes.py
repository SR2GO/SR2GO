from xml.dom import minidom
import re
import os
#opening xml file
xml_fname = open('test.xml')
xml = minidom.parse(xml_fname) # or xml.dom.minidom.parseString(xml_string)

#loading attributes
##loading body attribute
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
##loading agility attribute

##loading reaction attribute

##loading strength attribute

## charisma

## intuition

## logic

##willpower


