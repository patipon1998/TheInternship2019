import json
import xml.etree.ElementTree as ET

def toDict(node) :
    Dictionary = dict()

    if (node.text != None) and (len(node.text.strip()) > 0) :
        Dictionary[node.tag] = node.text.strip()
        return Dictionary    

    if len(node.attrib) != 0 :
        Dictionary[node.tag] = (node.attrib)

    if len(list(node.iter(None))) > 1 :
        for child in node :
            try :
                Dictionary[node.tag].update(toDict(child))
            except :
                Dictionary[node.tag] = toDict(child)
    
    return Dictionary

tree = ET.parse('weather.xml')
root = tree.getroot()
out = toDict(root)
index = list(out.keys())[0]

with open('weather.json', 'w') as file:
    json.dump(out[index], file, ensure_ascii=False, indent=4)