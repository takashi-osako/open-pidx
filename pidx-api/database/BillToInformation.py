'''
Created on Mar 16, 2013

@author: tosako
'''


class BillToInformation():
    def __init__(self):
        self.attributes = self.Attributes()
    class Attributes():
        def __init__(self):
            self.AddressInformation = None
            self.ShipperInformation = None
            self.BillToFEIN = None
            self.BillToID = None
            self.BillToName = None
            self.ContractID = None
            self.ContractName = None
