'''
Created on Mar 16, 2013

@author: tosako
'''


class BillOfLadingSummary():
    def __init__(self):
        self.attributes=self.Attributes()

    class Attributes():
        def __init__(self):
            self.FinishedProductCount = None
            self.GrossQuantityTotal = None
            self.NetQuantityTotal = None
