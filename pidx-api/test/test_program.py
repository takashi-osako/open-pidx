'''
Created on Mar 18, 2013

@author: tosako
'''
from utils.json_exporter import xml_to_json
import json
from database.mongo_connector import MongoConnector

myjson = xml_to_json('../resources/xml/Receipt.xml')
print(json.dumps(myjson))


recept = MongoConnector('Recept')
recept.insert(myjson)
