'''
Created on Mar 16, 2013

@author: tosako
'''


class SecondaryDriverID():
    def __init__(self):
        self.attributes = self.Attributes()

    class Attributes():
        def __init__(self):
            self.IdentType = None
            self.Issuer = None
