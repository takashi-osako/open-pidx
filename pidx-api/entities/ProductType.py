'''
Created on Mar 16, 2013

@author: tosako
'''


class ProductType():
    def __init__(self):
        self.ProductDescription = None
        self.GrossQuantity = None
        self.Temperature = None
        self.Gravity = None
        self.NetQuantity = None
        self.ProductCharacteristics = None
        self.attributes = self.Attributes()

    class Attributes():
        def __init__(self):
            self.ProductCode = None
            self.ProductName = None