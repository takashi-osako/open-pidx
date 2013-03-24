'''
Created on Mar 24, 2013

@author: tosako
'''
from pymongo.mongo_client import MongoClient

client = MongoClient()
pidx = client.pidx
# TODO: read host information from ini
# client = MongoClient('localhost', 27017)

class MongoConnector():
    def __init__(self, collection_name):
        self.collection = getattr(pidx, collection_name)

    def insert(self,data):
        self.collection.insert(data)
