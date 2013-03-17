'''
Created on Mar 16, 2013

@author: tosako
'''


class BillOfLadingHeader():
    def __init__(self):
        self.PurchaseOrderInformation = None
        self.SupplierInformation = None
        self.ExchangeOrThroughputPartnerInformation = None
        self.ThirdParty = None
        self.FinalShipper = None
        self.TerminalInformation = None
        self.CarrierInformation = None
        self.BillToInformation = None
        self.ShipToInformation = None
        self.attribute = self.Attributes()

    class Attributes():
        def __init__(self):
            self.AuthorizationCode = None
            self.ConsigneeNumber = None
            self.DispatchOrderNumber = None
            self.EndLoadDate = None
            self.EndLoadTime = None
            self.EntryDate = None
            self.EntryTime = None
            self.ExitDate = None
            self.ExitTime = None
            self.LoadSpot = None
            self.StartLoadDate = None
            self.StartLoadTime = None
            self.TransactionType = None
            self.BillOfLadingNumber = None
