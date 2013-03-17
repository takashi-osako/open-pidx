'''
Created on Mar 16, 2013

@author: tosako
'''

class CompanyInformationType():
    def __init__(self):
        self.attributes = self.Attributes()
    class Attributes():
        def __init__(self):
            self.CompanyCode = None
            self.CompanyName = None
            self.CompanyFEIN = None
