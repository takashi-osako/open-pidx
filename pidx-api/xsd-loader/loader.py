'''
Created on Mar 16, 2013

@author: tosako
'''
import os
from xml.dom.minidom import parse, Element


class loader():
    def __init__(self, filename):
        doml = parse(filename)
        schema_node = doml.childNodes[0]
        for node in schema_node.childNodes:
            if isinstance(node, Element):
                if node.tagName == 'annotation':
                    pass
                elif node.tagName == 'element':
                    self.process_element(node)
        pass

    def process_element(self, element):
        pass

class Element():
    def __init__(self, name):
        self.name = name
        self.sequence = []
        

here = os.path.abspath(os.path.dirname(__file__)) + '/../resources/Invoice.xsd'
l = loader(here)
