'''
Created on Mar 16, 2013

@author: tosako
'''


class TerminalInformation():
    def __init__(self):
        self.AddressInformation = None
        self.attributes = self.Attributes()

    class Attributes():
        def __init__(self):
            self.EPAEntityID = None
            self.EPAFacilityID = None
            self.TerminalControlNumber = None
            self.TerminalName = None
            self.TerminalSPLC = None
            self.TerminalTimeZone = None
