'''
Created on Mar 16, 2013

@author: tosako
'''


class BillOfLadingCreate():
    def __init__(self):
        self.BillOfLadingHeader = None
        self.BillOfLadingDetails = None
        self.BillOfLadingSummary = None
        self.attributes = self.Attributes()

    class Attributes():
        def __init__(self):
            self.documentIdentifier = None
            self.transactionPurposeIndicator = None
            self.version = None
