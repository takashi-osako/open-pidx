'''
Created on Mar 16, 2013

@author: tosako
'''
from entities.BillOfLadingCreate import BillOfLadingCreate
from entities.BillOfLadingDetails import BillOfLadingDetails
from entities.BillOfLadingHeader import BillOfLadingHeader
from entities.BillOfLadingSummary import BillOfLadingSummary
from entities.BillToInformation import BillToInformation
from entities.CarrierInformation import CarrierInformation
from entities.ComponentProduct import ComponentProduct


class BillOfLadingCreateManager():
    def __init__(self):
        self.BillOfLadingCreate = BillOfLadingCreate()
        self.BillOfLadingDetails = BillOfLadingDetails()
        self.BillOfLadingHeader = BillOfLadingHeader()
        self.BillOfLadingSummary = BillOfLadingSummary()
        self.BillToInformation = BillToInformation()
        self.CarrierInformation = CarrierInformation()
        self.ComponentProduct = ComponentProduct()
        self.SecondaryDriverID = SecondaryDriverID()
        self.ShipperInformation = None
