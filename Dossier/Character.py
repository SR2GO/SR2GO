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
#m = re.search('<.+?>(.+?)<.+?>', attribute_body_out)
#if m:
#    attribute_body_out = m.group(1)
#print (attribute_body_out)