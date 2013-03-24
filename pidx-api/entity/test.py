'''
Created on Mar 18, 2013

@author: tosako
'''
from utils.json_exporter import xml_to_json
import json

myjson = xml_to_json('../resources/xml/Receipt.xml')
print(json.dumps(myjson))