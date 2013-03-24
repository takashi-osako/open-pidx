#!/usr/bin/env python

#
# Generated Mon Mar 18 22:52:30 2013 by generateDS.py version 2.9a.
#

import sys

import BillOfLadingCreate as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class BillOfLadingDetailsTypeSub(supermod.BillOfLadingDetailsType):
    def __init__(self, FinishedProduct=None):
        super(BillOfLadingDetailsTypeSub, self).__init__(FinishedProduct, )
supermod.BillOfLadingDetailsType.subclass = BillOfLadingDetailsTypeSub
# end class BillOfLadingDetailsTypeSub


class BillOfLadingHeaderTypeSub(supermod.BillOfLadingHeaderType):
    def __init__(self, LoadSpot=None, AuthorizationCode=None, ExitTime=None, ExitDate=None, ConsigneeNumber=None, StartLoadDate=None, EndLoadTime=None, DispatchOrderNumber=None, EntryTime=None, BillOfLadingNumber=None, EntryDate=None, TransactionType=None, EndLoadDate=None, StartLoadTime=None, PurchaseOrderInformation=None, SupplierInformation=None, ExchangeOrThroughputPartnerInformation=None, ThirdParty=None, FinalShipper=None, TerminalInformation=None, CarrierInformation=None, BillToInformation=None, ShipToInformation=None):
        super(BillOfLadingHeaderTypeSub, self).__init__(LoadSpot, AuthorizationCode, ExitTime, ExitDate, ConsigneeNumber, StartLoadDate, EndLoadTime, DispatchOrderNumber, EntryTime, BillOfLadingNumber, EntryDate, TransactionType, EndLoadDate, StartLoadTime, PurchaseOrderInformation, SupplierInformation, ExchangeOrThroughputPartnerInformation, ThirdParty, FinalShipper, TerminalInformation, CarrierInformation, BillToInformation, ShipToInformation, )
supermod.BillOfLadingHeaderType.subclass = BillOfLadingHeaderTypeSub
# end class BillOfLadingHeaderTypeSub


class BillOfLadingSummaryTypeSub(supermod.BillOfLadingSummaryType):
    def __init__(self, FinishedProductCount=None, GrossQuantityTotal=None, NetQuantityTotal=None):
        super(BillOfLadingSummaryTypeSub, self).__init__(FinishedProductCount, GrossQuantityTotal, NetQuantityTotal, )
supermod.BillOfLadingSummaryType.subclass = BillOfLadingSummaryTypeSub
# end class BillOfLadingSummaryTypeSub


class BillOfLadingTypeSub(supermod.BillOfLadingType):
    def __init__(self, transactionPurposeIndicator=None, version=None, documentIdentifier=None, BillOfLadingHeader=None, BillOfLadingDetails=None, BillOfLadingSummary=None):
        super(BillOfLadingTypeSub, self).__init__(transactionPurposeIndicator, version, documentIdentifier, BillOfLadingHeader, BillOfLadingDetails, BillOfLadingSummary, )
supermod.BillOfLadingType.subclass = BillOfLadingTypeSub
# end class BillOfLadingTypeSub


class BillToInformationTypeSub(supermod.BillToInformationType):
    def __init__(self, ContractID=None, BillToID=None, BillToFEIN=None, ContractName=None, BillToName=None, AddressInformation=None, ShipperInformation=None):
        super(BillToInformationTypeSub, self).__init__(ContractID, BillToID, BillToFEIN, ContractName, BillToName, AddressInformation, ShipperInformation, )
supermod.BillToInformationType.subclass = BillToInformationTypeSub
# end class BillToInformationTypeSub


class CarrierInformationTypeSub(supermod.CarrierInformationType):
    def __init__(self, SplitLoading=None, CarrierSCAC=None, CarrierID=None, CarrierFEIN=None, CarrierName=None, AddressInformation=None, DriverInformation=None, VehicleInformation=None):
        super(CarrierInformationTypeSub, self).__init__(SplitLoading, CarrierSCAC, CarrierID, CarrierFEIN, CarrierName, AddressInformation, DriverInformation, VehicleInformation, )
supermod.CarrierInformationType.subclass = CarrierInformationTypeSub
# end class CarrierInformationTypeSub


class DriverInformationTypeSub(supermod.DriverInformationType):
    def __init__(self, DriverID=None, DriverName=None, Signature=None, SecondaryDriverID=None):
        super(DriverInformationTypeSub, self).__init__(DriverID, DriverName, Signature, SecondaryDriverID, )
supermod.DriverInformationType.subclass = DriverInformationTypeSub
# end class DriverInformationTypeSub


class SecondaryDriverIDTypeSub(supermod.SecondaryDriverIDType):
    def __init__(self, Issuer=None, IdentType=None):
        super(SecondaryDriverIDTypeSub, self).__init__(Issuer, IdentType, )
supermod.SecondaryDriverIDType.subclass = SecondaryDriverIDTypeSub
# end class SecondaryDriverIDTypeSub


class ShipToInformationTypeSub(supermod.ShipToInformationType):
    def __init__(self, ShipToStateCode=None, ShipToCityCode=None, ShipToCountyCode=None, ShipToName=None, ShipToID=None, AddressInformation=None):
        super(ShipToInformationTypeSub, self).__init__(ShipToStateCode, ShipToCityCode, ShipToCountyCode, ShipToName, ShipToID, AddressInformation, )
supermod.ShipToInformationType.subclass = ShipToInformationTypeSub
# end class ShipToInformationTypeSub


class VehicleInformationTypeSub(supermod.VehicleInformationType):
    def __init__(self, VehicleType=None, VehicleNumber=None, extensiontype_=None):
        super(VehicleInformationTypeSub, self).__init__(VehicleType, VehicleNumber, extensiontype_, )
supermod.VehicleInformationType.subclass = VehicleInformationTypeSub
# end class VehicleInformationTypeSub


class AccountInformationSub(supermod.AccountInformation):
    def __init__(self, AccountHolderName=None, AccountNumber=None, FinancialInstitution=None, FinancialInstitutionDFINumber=None, CreditCardNumber=None, CreditCardType=None, ExpireDate=None):
        super(AccountInformationSub, self).__init__(AccountHolderName, AccountNumber, FinancialInstitution, FinancialInstitutionDFINumber, CreditCardNumber, CreditCardType, ExpireDate, )
supermod.AccountInformation.subclass = AccountInformationSub
# end class AccountInformationSub


class AddressInformationSub(supermod.AddressInformation):
    def __init__(self, POBoxNumber=None, BuildingHouseNumber=None, StreetName=None, AddressLine=None, CityName=None, StateProvince=None, PostalCode=None, PostalCountry=None, CountyName=None, LocationIdentifier=None, StreetDirection=None, RegionName=None, LocationCode=None, Comment=None):
        super(AddressInformationSub, self).__init__(POBoxNumber, BuildingHouseNumber, StreetName, AddressLine, CityName, StateProvince, PostalCode, PostalCountry, CountyName, LocationIdentifier, StreetDirection, RegionName, LocationCode, Comment, )
supermod.AddressInformation.subclass = AddressInformationSub
# end class AddressInformationSub


class AdditiveTypeIdentifierSub(supermod.AdditiveTypeIdentifier):
    def __init__(self, identifierIndicator=None, valueOf_=None):
        super(AdditiveTypeIdentifierSub, self).__init__(identifierIndicator, valueOf_, )
supermod.AdditiveTypeIdentifier.subclass = AdditiveTypeIdentifierSub
# end class AdditiveTypeIdentifierSub


class AllowanceOrChargeSub(supermod.AllowanceOrCharge):
    def __init__(self, allowanceOrChargeIndicator=None, AllowanceOrChargeTotalAmount=None, AllowanceOrChargeRate=None, AllowanceOrChargePercent=None, AllowanceOrChargeNumber=None, AllowanceOrChargeTypeCode=None, MethodOfHandlingCode=None, AllowanceOrChargeDescription=None, AllowanceOrChargeQuantity=None):
        super(AllowanceOrChargeSub, self).__init__(allowanceOrChargeIndicator, AllowanceOrChargeTotalAmount, AllowanceOrChargeRate, AllowanceOrChargePercent, AllowanceOrChargeNumber, AllowanceOrChargeTypeCode, MethodOfHandlingCode, AllowanceOrChargeDescription, AllowanceOrChargeQuantity, )
supermod.AllowanceOrCharge.subclass = AllowanceOrChargeSub
# end class AllowanceOrChargeSub


class AllowanceOrChargePercentSub(supermod.AllowanceOrChargePercent):
    def __init__(self, percentIndicator=None, valueOf_=None):
        super(AllowanceOrChargePercentSub, self).__init__(percentIndicator, valueOf_, )
supermod.AllowanceOrChargePercent.subclass = AllowanceOrChargePercentSub
# end class AllowanceOrChargePercentSub


class AllowanceOrChargeRateSub(supermod.AllowanceOrChargeRate):
    def __init__(self, MonetaryAmount=None, UnitOfMeasureCode=None, CurrencyCode=None):
        super(AllowanceOrChargeRateSub, self).__init__(MonetaryAmount, UnitOfMeasureCode, CurrencyCode, )
supermod.AllowanceOrChargeRate.subclass = AllowanceOrChargeRateSub
# end class AllowanceOrChargeRateSub


class AlternativeCommunicationMethodSub(supermod.AlternativeCommunicationMethod):
    def __init__(self, communicationMethodType=None, definitionOfOther=None, alternativeCommunicationMethodIndicator=None, valueOf_=None):
        super(AlternativeCommunicationMethodSub, self).__init__(communicationMethodType, definitionOfOther, alternativeCommunicationMethodIndicator, valueOf_, )
supermod.AlternativeCommunicationMethod.subclass = AlternativeCommunicationMethodSub
# end class AlternativeCommunicationMethodSub


class AmbientTemperatureSub(supermod.AmbientTemperature):
    def __init__(self, Temperature=None, UnitOfMeasureCode=None):
        super(AmbientTemperatureSub, self).__init__(Temperature, UnitOfMeasureCode, )
supermod.AmbientTemperature.subclass = AmbientTemperatureSub
# end class AmbientTemperatureSub


class AttachmentSub(supermod.Attachment):
    def __init__(self, AttachmentPurposeCode=None, FileName=None, AttachmentTitle=None, AttachmentDescription=None, FileType=None, AttachmentLocation=None):
        super(AttachmentSub, self).__init__(AttachmentPurposeCode, FileName, AttachmentTitle, AttachmentDescription, FileType, AttachmentLocation, )
supermod.Attachment.subclass = AttachmentSub
# end class AttachmentSub


class AveragePressureSub(supermod.AveragePressure):
    def __init__(self, Pressure=None, UnitOfMeasureCode=None):
        super(AveragePressureSub, self).__init__(Pressure, UnitOfMeasureCode, )
supermod.AveragePressure.subclass = AveragePressureSub
# end class AveragePressureSub


class AverageTemperatureSub(supermod.AverageTemperature):
    def __init__(self, Temperature=None, UnitOfMeasureCode=None):
        super(AverageTemperatureSub, self).__init__(Temperature, UnitOfMeasureCode, )
supermod.AverageTemperature.subclass = AverageTemperatureSub
# end class AverageTemperatureSub


class BatchNumberSub(supermod.BatchNumber):
    def __init__(self, batchNumberCreator=None, definitionOfOther=None, valueOf_=None):
        super(BatchNumberSub, self).__init__(batchNumberCreator, definitionOfOther, valueOf_, )
supermod.BatchNumber.subclass = BatchNumberSub
# end class BatchNumberSub


class BlockSub(supermod.Block):
    def __init__(self, BlockName=None, OCSGNumber=None, StateLease=None):
        super(BlockSub, self).__init__(BlockName, OCSGNumber, StateLease, )
supermod.Block.subclass = BlockSub
# end class BlockSub


class BuyersCurrencySub(supermod.BuyersCurrency):
    def __init__(self, CurrencyCode=None):
        super(BuyersCurrencySub, self).__init__(CurrencyCode, )
supermod.BuyersCurrency.subclass = BuyersCurrencySub
# end class BuyersCurrencySub


class ChangeOrderInformationSub(supermod.ChangeOrderInformation):
    def __init__(self, OrderChangeNumber=None, OrderChangeDate=None, PurchaseOrderTypeCode=None, SalesOrderNumber=None, SequenceNumber=None):
        super(ChangeOrderInformationSub, self).__init__(OrderChangeNumber, OrderChangeDate, PurchaseOrderTypeCode, SalesOrderNumber, SequenceNumber, )
supermod.ChangeOrderInformation.subclass = ChangeOrderInformationSub
# end class ChangeOrderInformationSub


class CommodityCodeSub(supermod.CommodityCode):
    def __init__(self, agencyIndicator=None, valueOf_=None):
        super(CommodityCodeSub, self).__init__(agencyIndicator, valueOf_, )
supermod.CommodityCode.subclass = CommodityCodeSub
# end class CommodityCodeSub


class ContactIdentifierSub(supermod.ContactIdentifier):
    def __init__(self, contactIdentifierIndicator=None, valueOf_=None):
        super(ContactIdentifierSub, self).__init__(contactIdentifierIndicator, valueOf_, )
supermod.ContactIdentifier.subclass = ContactIdentifierSub
# end class ContactIdentifierSub


class ContactInformationSub(supermod.ContactInformation):
    def __init__(self, contactInformationIndicator=None, ContactIdentifier=None, ContactName=None, ContactDescription=None, Telephone=None, EmailAddress=None, AlternativeCommunicationMethod=None, LanguageCode=None):
        super(ContactInformationSub, self).__init__(contactInformationIndicator, ContactIdentifier, ContactName, ContactDescription, Telephone, EmailAddress, AlternativeCommunicationMethod, LanguageCode, )
supermod.ContactInformation.subclass = ContactInformationSub
# end class ContactInformationSub


class ConveyanceInformationSub(supermod.ConveyanceInformation):
    def __init__(self, ConveyanceIdentifier=None, VoyageTripNumber=None, VoyageTripDateTimeRange=None, EstimatedDateTimeOfArrival=None):
        super(ConveyanceInformationSub, self).__init__(ConveyanceIdentifier, VoyageTripNumber, VoyageTripDateTimeRange, EstimatedDateTimeOfArrival, )
supermod.ConveyanceInformation.subclass = ConveyanceInformationSub
# end class ConveyanceInformationSub


class CountryOfFinalDestinationSub(supermod.CountryOfFinalDestination):
    def __init__(self, CountryCode=None):
        super(CountryOfFinalDestinationSub, self).__init__(CountryCode, )
supermod.CountryOfFinalDestination.subclass = CountryOfFinalDestinationSub
# end class CountryOfFinalDestinationSub


class CountryOfOriginSub(supermod.CountryOfOrigin):
    def __init__(self, CountryCode=None):
        super(CountryOfOriginSub, self).__init__(CountryCode, )
supermod.CountryOfOrigin.subclass = CountryOfOriginSub
# end class CountryOfOriginSub


class CreditCardInformationSub(supermod.CreditCardInformation):
    def __init__(self, CreditCardNumber=None, CardHolderName=None, CreditCardType=None, CreditCardExpirationDate=None, CardAuthorizationCode=None, CardReferenceNumber=None):
        super(CreditCardInformationSub, self).__init__(CreditCardNumber, CardHolderName, CreditCardType, CreditCardExpirationDate, CardAuthorizationCode, CardReferenceNumber, )
supermod.CreditCardInformation.subclass = CreditCardInformationSub
# end class CreditCardInformationSub


class CurrencyRatesSub(supermod.CurrencyRates):
    def __init__(self, SellersCurrency=None, BuyersCurrency=None, ExchangeRate=None):
        super(CurrencyRatesSub, self).__init__(SellersCurrency, BuyersCurrency, ExchangeRate, )
supermod.CurrencyRates.subclass = CurrencyRatesSub
# end class CurrencyRatesSub


class CustodyLocationIdentifierSub(supermod.CustodyLocationIdentifier):
    def __init__(self, identifierIndicator=None, valueOf_=None):
        super(CustodyLocationIdentifierSub, self).__init__(identifierIndicator, valueOf_, )
supermod.CustodyLocationIdentifier.subclass = CustodyLocationIdentifierSub
# end class CustodyLocationIdentifierSub


class CustodyLocationInformationSub(supermod.CustodyLocationInformation):
    def __init__(self, CustodyLocationIdentifier=None, CustodyLocationDescription=None, AddressInformation=None, GeographicalInformation=None):
        super(CustodyLocationInformationSub, self).__init__(CustodyLocationIdentifier, CustodyLocationDescription, AddressInformation, GeographicalInformation, )
supermod.CustodyLocationInformation.subclass = CustodyLocationInformationSub
# end class CustodyLocationInformationSub


class CustodyTicketInformationSub(supermod.CustodyTicketInformation):
    def __init__(self, custodyTicketType=None, thirdPartyTicketIndicator=None, CustodyTicketNumber=None, CustodyTicketDateTime=None, CustodyTransferStartDateTime=None, CustodyTransferStopDateTime=None, RevisionNumber=None, CustodySupercedeTicketNumber=None, ConnectingCarrierTicketNumber=None):
        super(CustodyTicketInformationSub, self).__init__(custodyTicketType, thirdPartyTicketIndicator, CustodyTicketNumber, CustodyTicketDateTime, CustodyTransferStartDateTime, CustodyTransferStopDateTime, RevisionNumber, CustodySupercedeTicketNumber, ConnectingCarrierTicketNumber, )
supermod.CustodyTicketInformation.subclass = CustodyTicketInformationSub
# end class CustodyTicketInformationSub


class CustodyTicketTimeLogSub(supermod.CustodyTicketTimeLog):
    def __init__(self, CustodyTicketTimeLogEntry=None):
        super(CustodyTicketTimeLogSub, self).__init__(CustodyTicketTimeLogEntry, )
supermod.CustodyTicketTimeLog.subclass = CustodyTicketTimeLogSub
# end class CustodyTicketTimeLogSub


class CustodyTicketTimeLogEntrySub(supermod.CustodyTicketTimeLogEntry):
    def __init__(self, TimeLogDateTime=None, TimeLogActivity=None):
        super(CustodyTicketTimeLogEntrySub, self).__init__(TimeLogDateTime, TimeLogActivity, )
supermod.CustodyTicketTimeLogEntry.subclass = CustodyTicketTimeLogEntrySub
# end class CustodyTicketTimeLogEntrySub


class CustodyTransferInformationSub(supermod.CustodyTransferInformation):
    def __init__(self, FromPartner=None, ToPartner=None):
        super(CustodyTransferInformationSub, self).__init__(FromPartner, ToPartner, )
supermod.CustodyTransferInformation.subclass = CustodyTransferInformationSub
# end class CustodyTransferInformationSub


class CustomerSpecificInformationSub(supermod.CustomerSpecificInformation):
    def __init__(self, informationType=None, valueOf_=None):
        super(CustomerSpecificInformationSub, self).__init__(informationType, valueOf_, )
supermod.CustomerSpecificInformation.subclass = CustomerSpecificInformationSub
# end class CustomerSpecificInformationSub


class DeferredSub(supermod.Deferred):
    def __init__(self, DeferredAmount=None, DeferredDueDate=None, PercentDeferredPayable=None, Description=None):
        super(DeferredSub, self).__init__(DeferredAmount, DeferredDueDate, PercentDeferredPayable, Description, )
supermod.Deferred.subclass = DeferredSub
# end class DeferredSub


class DeliveryTolerancesSub(supermod.DeliveryTolerances):
    def __init__(self, UpperLimit=None, LowerLimit=None):
        super(DeliveryTolerancesSub, self).__init__(UpperLimit, LowerLimit, )
supermod.DeliveryTolerances.subclass = DeliveryTolerancesSub
# end class DeliveryTolerancesSub


class DiscountsSub(supermod.Discounts):
    def __init__(self, DaysDue=None, DiscountsDueDate=None, PercentDiscount=None, DiscountAmount=None, Description=None):
        super(DiscountsSub, self).__init__(DaysDue, DiscountsDueDate, PercentDiscount, DiscountAmount, Description, )
supermod.Discounts.subclass = DiscountsSub
# end class DiscountsSub


class DocumentDeliveryInformationSub(supermod.DocumentDeliveryInformation):
    def __init__(self, PartnerInformation=None):
        super(DocumentDeliveryInformationSub, self).__init__(PartnerInformation, )
supermod.DocumentDeliveryInformation.subclass = DocumentDeliveryInformationSub
# end class DocumentDeliveryInformationSub


class DocumentReferenceSub(supermod.DocumentReference):
    def __init__(self, referenceType=None, definitionOfOther=None, DocumentIdentifier=None, ReferenceItem=None, ReferenceInformation=None, DocumentDate=None):
        super(DocumentReferenceSub, self).__init__(referenceType, definitionOfOther, DocumentIdentifier, ReferenceItem, ReferenceInformation, DocumentDate, )
supermod.DocumentReference.subclass = DocumentReferenceSub
# end class DocumentReferenceSub


class EffectiveDatesSub(supermod.EffectiveDates):
    def __init__(self, FromDate=None, ToDate=None):
        super(EffectiveDatesSub, self).__init__(FromDate, ToDate, )
supermod.EffectiveDates.subclass = EffectiveDatesSub
# end class EffectiveDatesSub


class ErrorClassificationSub(supermod.ErrorClassification):
    def __init__(self, GlobalMessageExceptionCode=None):
        super(ErrorClassificationSub, self).__init__(GlobalMessageExceptionCode, )
supermod.ErrorClassification.subclass = ErrorClassificationSub
# end class ErrorClassificationSub


class ErrorDescriptionSub(supermod.ErrorDescription):
    def __init__(self, FreeFormText=None):
        super(ErrorDescriptionSub, self).__init__(FreeFormText, )
supermod.ErrorDescription.subclass = ErrorDescriptionSub
# end class ErrorDescriptionSub


class ExceptionDescriptionSub(supermod.ExceptionDescription):
    def __init__(self, ErrorClassification=None, ErrorDescription=None, OffendingMessageComponent=None):
        super(ExceptionDescriptionSub, self).__init__(ErrorClassification, ErrorDescription, OffendingMessageComponent, )
supermod.ExceptionDescription.subclass = ExceptionDescriptionSub
# end class ExceptionDescriptionSub


class FieldTicketInformationSub(supermod.FieldTicketInformation):
    def __init__(self, FieldTicketNumber=None, FieldTicketDate=None, RevisionNumber=None):
        super(FieldTicketInformationSub, self).__init__(FieldTicketNumber, FieldTicketDate, RevisionNumber, )
supermod.FieldTicketInformation.subclass = FieldTicketInformationSub
# end class FieldTicketInformationSub


class FinalDestinationLocationIdentifierSub(supermod.FinalDestinationLocationIdentifier):
    def __init__(self, identifierIndicator=None, valueOf_=None):
        super(FinalDestinationLocationIdentifierSub, self).__init__(identifierIndicator, valueOf_, )
supermod.FinalDestinationLocationIdentifier.subclass = FinalDestinationLocationIdentifierSub
# end class FinalDestinationLocationIdentifierSub


class FinalDestinationLocationInformationSub(supermod.FinalDestinationLocationInformation):
    def __init__(self, FinalDestinationLocationIdentifier=None, FinalDestinationLocationDescription=None, AddressInformation=None, GeographicalInformation=None):
        super(FinalDestinationLocationInformationSub, self).__init__(FinalDestinationLocationIdentifier, FinalDestinationLocationDescription, AddressInformation, GeographicalInformation, )
supermod.FinalDestinationLocationInformation.subclass = FinalDestinationLocationInformationSub
# end class FinalDestinationLocationInformationSub


class FlashTemperatureSub(supermod.FlashTemperature):
    def __init__(self, Temperature=None, UnitOfMeasureCode=None):
        super(FlashTemperatureSub, self).__init__(Temperature, UnitOfMeasureCode, )
supermod.FlashTemperature.subclass = FlashTemperatureSub
# end class FlashTemperatureSub


class FreeFormTextSub(supermod.FreeFormText):
    def __init__(self, language=None, valueOf_=None):
        super(FreeFormTextSub, self).__init__(language, valueOf_, )
supermod.FreeFormText.subclass = FreeFormTextSub
# end class FreeFormTextSub


class GaugeReadingMeasureSub(supermod.GaugeReadingMeasure):
    def __init__(self, Measurement=None, UnitOfMeasureCode=None):
        super(GaugeReadingMeasureSub, self).__init__(Measurement, UnitOfMeasureCode, )
supermod.GaugeReadingMeasure.subclass = GaugeReadingMeasureSub
# end class GaugeReadingMeasureSub


class GeographicalInformationSub(supermod.GeographicalInformation):
    def __init__(self, FieldName=None, Section=None, Township=None, Range=None, Region=None, Block=None, GPSCoordinates=None):
        super(GeographicalInformationSub, self).__init__(FieldName, Section, Township, Range, Region, Block, GPSCoordinates, )
supermod.GeographicalInformation.subclass = GeographicalInformationSub
# end class GeographicalInformationSub


class GPSCoordinatesSub(supermod.GPSCoordinates):
    def __init__(self, Latitude=None, Longitude=None):
        super(GPSCoordinatesSub, self).__init__(Latitude, Longitude, )
supermod.GPSCoordinates.subclass = GPSCoordinatesSub
# end class GPSCoordinatesSub


class GravitySub(supermod.Gravity):
    def __init__(self, Type=None, valueOf_=None):
        super(GravitySub, self).__init__(Type, valueOf_, )
supermod.Gravity.subclass = GravitySub
# end class GravitySub


class GrossQuantitySub(supermod.GrossQuantity):
    def __init__(self, QuantityUnitOfMeasurement=None, valueOf_=None):
        super(GrossQuantitySub, self).__init__(QuantityUnitOfMeasurement, valueOf_, )
supermod.GrossQuantity.subclass = GrossQuantitySub
# end class GrossQuantitySub


class HazardousMaterialClassCodeSub(supermod.HazardousMaterialClassCode):
    def __init__(self, hazardousMaterialIndicator=None, valueOf_=None):
        super(HazardousMaterialClassCodeSub, self).__init__(hazardousMaterialIndicator, valueOf_, )
supermod.HazardousMaterialClassCode.subclass = HazardousMaterialClassCodeSub
# end class HazardousMaterialClassCodeSub


class HazardousMaterialsSub(supermod.HazardousMaterials):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialDescription=None, HazardousMaterialClassCode=None):
        super(HazardousMaterialsSub, self).__init__(SpecialHandlingCode, HazardousMaterialDescription, HazardousMaterialClassCode, )
supermod.HazardousMaterials.subclass = HazardousMaterialsSub
# end class HazardousMaterialsSub


class IntermodalServiceSub(supermod.IntermodalService):
    def __init__(self, codeListName=None, valueOf_=None):
        super(IntermodalServiceSub, self).__init__(codeListName, valueOf_, )
supermod.IntermodalService.subclass = IntermodalServiceSub
# end class IntermodalServiceSub


class IntrastatSub(supermod.Intrastat):
    def __init__(self, CommodityCode=None, CommodityDescription=None, TransactionNature=None, SupplementaryUnits=None, CountryOfFinalDestination=None, TransportMethodCode=None):
        super(IntrastatSub, self).__init__(CommodityCode, CommodityDescription, TransactionNature, SupplementaryUnits, CountryOfFinalDestination, TransportMethodCode, )
supermod.Intrastat.subclass = IntrastatSub
# end class IntrastatSub


class InvoiceInformationSub(supermod.InvoiceInformation):
    def __init__(self, InvoiceNumber=None, InvoiceDate=None, InvoiceTypeCode=None, RevisionNumber=None):
        super(InvoiceInformationSub, self).__init__(InvoiceNumber, InvoiceDate, InvoiceTypeCode, RevisionNumber, )
supermod.InvoiceInformation.subclass = InvoiceInformationSub
# end class InvoiceInformationSub


class JobLocationIdentifierSub(supermod.JobLocationIdentifier):
    def __init__(self, jobLocationIdentifierIndicator=None, valueOf_=None):
        super(JobLocationIdentifierSub, self).__init__(jobLocationIdentifierIndicator, valueOf_, )
supermod.JobLocationIdentifier.subclass = JobLocationIdentifierSub
# end class JobLocationIdentifierSub


class JobLocationInformationSub(supermod.JobLocationInformation):
    def __init__(self, JobLocationIdentifier=None, JobLocationClassCode=None, JobLocationDescription=None, JobLocationStatus=None, WellInformation=None, JobSiteCategory=None, AddressInformation=None, GeographicalInformation=None):
        super(JobLocationInformationSub, self).__init__(JobLocationIdentifier, JobLocationClassCode, JobLocationDescription, JobLocationStatus, WellInformation, JobSiteCategory, AddressInformation, GeographicalInformation, )
supermod.JobLocationInformation.subclass = JobLocationInformationSub
# end class JobLocationInformationSub


class LetterOfCreditInformationSub(supermod.LetterOfCreditInformation):
    def __init__(self, DocumentReference=None, AdvisingBank=None, LetterOfCreditAmount=None, PaymentTerms=None, LetterOfCreditQuantity=None, LetterOfCreditVoyageDateTimeRange=None, LetterOfCreditNegotiatedDateTimeRange=None):
        super(LetterOfCreditInformationSub, self).__init__(DocumentReference, AdvisingBank, LetterOfCreditAmount, PaymentTerms, LetterOfCreditQuantity, LetterOfCreditVoyageDateTimeRange, LetterOfCreditNegotiatedDateTimeRange, )
supermod.LetterOfCreditInformation.subclass = LetterOfCreditInformationSub
# end class LetterOfCreditInformationSub


class LineItemAdditiveSub(supermod.LineItemAdditive):
    def __init__(self, AdditiveTypeIdentifier=None, Quantity=None, UnitOfMeasureCode=None):
        super(LineItemAdditiveSub, self).__init__(AdditiveTypeIdentifier, Quantity, UnitOfMeasureCode, )
supermod.LineItemAdditive.subclass = LineItemAdditiveSub
# end class LineItemAdditiveSub


class LineItemIdentifierSub(supermod.LineItemIdentifier):
    def __init__(self, identifierIndicator=None, valueOf_=None):
        super(LineItemIdentifierSub, self).__init__(identifierIndicator, valueOf_, )
supermod.LineItemIdentifier.subclass = LineItemIdentifierSub
# end class LineItemIdentifierSub


class LineItemInformationSub(supermod.LineItemInformation):
    def __init__(self, LineItemIdentifier=None, LineItemName=None, LineItemDescription=None, ManufacturerIdentifier=None):
        super(LineItemInformationSub, self).__init__(LineItemIdentifier, LineItemName, LineItemDescription, ManufacturerIdentifier, )
supermod.LineItemInformation.subclass = LineItemInformationSub
# end class LineItemInformationSub


class LineItemMeasuresSub(supermod.LineItemMeasures):
    def __init__(self, SampleMeasures=None, VesselMeasures=None, TankMeasures=None, Meter=None, PartnerDefinedMeasure=None):
        super(LineItemMeasuresSub, self).__init__(SampleMeasures, VesselMeasures, TankMeasures, Meter, PartnerDefinedMeasure, )
supermod.LineItemMeasures.subclass = LineItemMeasuresSub
# end class LineItemMeasuresSub


class LineItemPurposeCodeSub(supermod.LineItemPurposeCode):
    def __init__(self, codeListName=None, valueOf_=None):
        super(LineItemPurposeCodeSub, self).__init__(codeListName, valueOf_, )
supermod.LineItemPurposeCode.subclass = LineItemPurposeCodeSub
# end class LineItemPurposeCodeSub


class LocationSub(supermod.Location):
    def __init__(self, locationIndicator=None, LocationIdentifier=None, LocationName=None, AddressInformation=None, GeographicalInformation=None, LocationDescription=None):
        super(LocationSub, self).__init__(locationIndicator, LocationIdentifier, LocationName, AddressInformation, GeographicalInformation, LocationDescription, )
supermod.Location.subclass = LocationSub
# end class LocationSub


class LocationCodeSub(supermod.LocationCode):
    def __init__(self, codeListName=None, valueOf_=None):
        super(LocationCodeSub, self).__init__(codeListName, valueOf_, )
supermod.LocationCode.subclass = LocationCodeSub
# end class LocationCodeSub


class LoadTenderInformationSub(supermod.LoadTenderInformation):
    def __init__(self, LoadTenderIdentifier=None, LoadTenderIssuedDateTime=None):
        super(LoadTenderInformationSub, self).__init__(LoadTenderIdentifier, LoadTenderIssuedDateTime, )
supermod.LoadTenderInformation.subclass = LoadTenderInformationSub
# end class LoadTenderInformationSub


class ManufacturingIdentificationDetailsSub(supermod.ManufacturingIdentificationDetails):
    def __init__(self, ManufacturingIdentificationTypeCode=None, ManufacturingIdentifier=None, ParentManufacturingIdentifier=None):
        super(ManufacturingIdentificationDetailsSub, self).__init__(ManufacturingIdentificationTypeCode, ManufacturingIdentifier, ParentManufacturingIdentifier, )
supermod.ManufacturingIdentificationDetails.subclass = ManufacturingIdentificationDetailsSub
# end class ManufacturingIdentificationDetailsSub


class ModeOfTransportationSub(supermod.ModeOfTransportation):
    def __init__(self, TransportMethodCode=None, TransportEvent=None, TransportContainer=None, HazardousMaterials=None):
        super(ModeOfTransportationSub, self).__init__(TransportMethodCode, TransportEvent, TransportContainer, HazardousMaterials, )
supermod.ModeOfTransportation.subclass = ModeOfTransportationSub
# end class ModeOfTransportationSub


class MeasurementRangeSub(supermod.MeasurementRange):
    def __init__(self, MinimumMeasurement=None, MaximumMeasurement=None):
        super(MeasurementRangeSub, self).__init__(MinimumMeasurement, MaximumMeasurement, )
supermod.MeasurementRange.subclass = MeasurementRangeSub
# end class MeasurementRangeSub


class MeterSub(supermod.Meter):
    def __init__(self, MeterNumber=None, OpenReading=None, CloseReading=None, MeterQuantity=None, MeterFactor=None, MeterDistributionPercent=None, ProverReport=None):
        super(MeterSub, self).__init__(MeterNumber, OpenReading, CloseReading, MeterQuantity, MeterFactor, MeterDistributionPercent, ProverReport, )
supermod.Meter.subclass = MeterSub
# end class MeterSub


class NetQuantitySub(supermod.NetQuantity):
    def __init__(self, QuantityUnitOfMeasurement=None, valueOf_=None):
        super(NetQuantitySub, self).__init__(QuantityUnitOfMeasurement, valueOf_, )
supermod.NetQuantity.subclass = NetQuantitySub
# end class NetQuantitySub


class ObservedTemperatureSub(supermod.ObservedTemperature):
    def __init__(self, Temperature=None, UnitOfMeasureCode=None):
        super(ObservedTemperatureSub, self).__init__(Temperature, UnitOfMeasureCode, )
supermod.ObservedTemperature.subclass = ObservedTemperatureSub
# end class ObservedTemperatureSub


class OffendingMessageComponentSub(supermod.OffendingMessageComponent):
    def __init__(self, GlobalMessageComponentCode=None):
        super(OffendingMessageComponentSub, self).__init__(GlobalMessageComponentCode, )
supermod.OffendingMessageComponent.subclass = OffendingMessageComponentSub
# end class OffendingMessageComponentSub


class OriginLocationIdentifierSub(supermod.OriginLocationIdentifier):
    def __init__(self, identifierIndicator=None, valueOf_=None):
        super(OriginLocationIdentifierSub, self).__init__(identifierIndicator, valueOf_, )
supermod.OriginLocationIdentifier.subclass = OriginLocationIdentifierSub
# end class OriginLocationIdentifierSub


class OriginLocationInformationSub(supermod.OriginLocationInformation):
    def __init__(self, OriginLocationIdentifier=None, OriginLocationDescription=None, AddressInformation=None, GeographicalInformation=None):
        super(OriginLocationInformationSub, self).__init__(OriginLocationIdentifier, OriginLocationDescription, AddressInformation, GeographicalInformation, )
supermod.OriginLocationInformation.subclass = OriginLocationInformationSub
# end class OriginLocationInformationSub


class PackageDetailSub(supermod.PackageDetail):
    def __init__(self, LineItemNumber=None, ProductInformation=None, PackageType=None, PackageLevel=None, PackagingQuantity=None, ShippingLabelNumber=None, PackageWeight=None, SubUnitCount=None):
        super(PackageDetailSub, self).__init__(LineItemNumber, ProductInformation, PackageType, PackageLevel, PackagingQuantity, ShippingLabelNumber, PackageWeight, SubUnitCount, )
supermod.PackageDetail.subclass = PackageDetailSub
# end class PackageDetailSub


class PackagingInformationSub(supermod.PackagingInformation):
    def __init__(self, ProductInformation=None, PackagingQuantity=None, PackageType=None, PackageWeight=None, PackagingLabel=None, SpecialInstructions=None):
        super(PackagingInformationSub, self).__init__(ProductInformation, PackagingQuantity, PackageType, PackageWeight, PackagingLabel, SpecialInstructions, )
supermod.PackagingInformation.subclass = PackagingInformationSub
# end class PackagingInformationSub


class PartnerDefinedMeasureSub(supermod.PartnerDefinedMeasure):
    def __init__(self, PartnerDefinedMeasureDescription=None, PartnerDefinedMeasureIdentifier=None, Measurement=None, UnitOfMeasureCode=None):
        super(PartnerDefinedMeasureSub, self).__init__(PartnerDefinedMeasureDescription, PartnerDefinedMeasureIdentifier, Measurement, UnitOfMeasureCode, )
supermod.PartnerDefinedMeasure.subclass = PartnerDefinedMeasureSub
# end class PartnerDefinedMeasureSub


class PartnerDefinedMeasureIdentifierSub(supermod.PartnerDefinedMeasureIdentifier):
    def __init__(self, partnerDefinedMeasureIdentifierIndicator=None, valueOf_=None):
        super(PartnerDefinedMeasureIdentifierSub, self).__init__(partnerDefinedMeasureIdentifierIndicator, valueOf_, )
supermod.PartnerDefinedMeasureIdentifier.subclass = PartnerDefinedMeasureIdentifierSub
# end class PartnerDefinedMeasureIdentifierSub


class PartnerIdentifierSub(supermod.PartnerIdentifier):
    def __init__(self, definitionOfOther=None, partnerIdentifierIndicator=None, valueOf_=None):
        super(PartnerIdentifierSub, self).__init__(definitionOfOther, partnerIdentifierIndicator, valueOf_, )
supermod.PartnerIdentifier.subclass = PartnerIdentifierSub
# end class PartnerIdentifierSub


class PartnerInformationSub(supermod.PartnerInformation):
    def __init__(self, partnerRoleIndicator=None, definitionOfOther=None, PartnerIdentifier=None, PartnerName=None, AddressInformation=None, ContactInformation=None, TaxInformation=None, URL=None, AccountInformation=None):
        super(PartnerInformationSub, self).__init__(partnerRoleIndicator, definitionOfOther, PartnerIdentifier, PartnerName, AddressInformation, ContactInformation, TaxInformation, URL, AccountInformation, )
supermod.PartnerInformation.subclass = PartnerInformationSub
# end class PartnerInformationSub


class PaymentTermsSub(supermod.PaymentTerms):
    def __init__(self, PaymentTermsOfSale=None, Description=None, PaymentTermsBasisDateCode=None, PaymentTermsBasisDate=None, TermsNetDays=None, PercentOfInvoicePayable=None, Discounts=None, Deferred=None, Penalty=None):
        super(PaymentTermsSub, self).__init__(PaymentTermsOfSale, Description, PaymentTermsBasisDateCode, PaymentTermsBasisDate, TermsNetDays, PercentOfInvoicePayable, Discounts, Deferred, Penalty, )
supermod.PaymentTerms.subclass = PaymentTermsSub
# end class PaymentTermsSub


class PersonnelInformationSub(supermod.PersonnelInformation):
    def __init__(self, PersonnelName=None, CompanyName=None, PersonnelIdentifier=None, TimeWorked=None, JobDescription=None, Comment=None):
        super(PersonnelInformationSub, self).__init__(PersonnelName, CompanyName, PersonnelIdentifier, TimeWorked, JobDescription, Comment, )
supermod.PersonnelInformation.subclass = PersonnelInformationSub
# end class PersonnelInformationSub


class PortOfDischargeSub(supermod.PortOfDischarge):
    def __init__(self, codeListName=None, valueOf_=None):
        super(PortOfDischargeSub, self).__init__(codeListName, valueOf_, )
supermod.PortOfDischarge.subclass = PortOfDischargeSub
# end class PortOfDischargeSub


class PostalCountrySub(supermod.PostalCountry):
    def __init__(self, CountryCode=None):
        super(PostalCountrySub, self).__init__(CountryCode, )
supermod.PostalCountry.subclass = PostalCountrySub
# end class PostalCountrySub


class PortOfLoadingSub(supermod.PortOfLoading):
    def __init__(self, codeListName=None, valueOf_=None):
        super(PortOfLoadingSub, self).__init__(codeListName, valueOf_, )
supermod.PortOfLoading.subclass = PortOfLoadingSub
# end class PortOfLoadingSub


class PriceBasisSub(supermod.PriceBasis):
    def __init__(self, Measurement=None, MeasurementRange=None, UnitOfMeasureCode=None, BasisDescription=None):
        super(PriceBasisSub, self).__init__(Measurement, MeasurementRange, UnitOfMeasureCode, BasisDescription, )
supermod.PriceBasis.subclass = PriceBasisSub
# end class PriceBasisSub


class PricingSub(supermod.Pricing):
    def __init__(self, UnitPrice=None, PriceBasis=None, PriceReason=None):
        super(PricingSub, self).__init__(UnitPrice, PriceBasis, PriceReason, )
supermod.Pricing.subclass = PricingSub
# end class PricingSub


class ProductSubLineItemsSub(supermod.ProductSubLineItems):
    def __init__(self, SubLineItemNumber=None, ManufacturingIdentificationDetails=None, GrossVolume=None, GrossWeight=None, NetWeight=None):
        super(ProductSubLineItemsSub, self).__init__(SubLineItemNumber, ManufacturingIdentificationDetails, GrossVolume, GrossWeight, NetWeight, )
supermod.ProductSubLineItems.subclass = ProductSubLineItemsSub
# end class ProductSubLineItemsSub


class PrimaryCurrencySub(supermod.PrimaryCurrency):
    def __init__(self, CurrencyCode=None):
        super(PrimaryCurrencySub, self).__init__(CurrencyCode, )
supermod.PrimaryCurrency.subclass = PrimaryCurrencySub
# end class PrimaryCurrencySub


class ProductIdentifierSub(supermod.ProductIdentifier):
    def __init__(self, definitionOfOther=None, assigningOrganization=None, valueOf_=None):
        super(ProductIdentifierSub, self).__init__(definitionOfOther, assigningOrganization, valueOf_, )
supermod.ProductIdentifier.subclass = ProductIdentifierSub
# end class ProductIdentifierSub


class ProductInformationSub(supermod.ProductInformation):
    def __init__(self, ProductIdentifier=None, ProductDescription=None, ProductGradeDescription=None):
        super(ProductInformationSub, self).__init__(ProductIdentifier, ProductDescription, ProductGradeDescription, )
supermod.ProductInformation.subclass = ProductInformationSub
# end class ProductInformationSub


class PurchaseOrderInformationSub(supermod.PurchaseOrderInformation):
    def __init__(self, PurchaseOrderNumber=None, PurchaseOrderIssuedDate=None, PurchaseOrderTypeCode=None, ReleaseNumber=None, SalesOrderNumber=None, RevisionNumber=None):
        super(PurchaseOrderInformationSub, self).__init__(PurchaseOrderNumber, PurchaseOrderIssuedDate, PurchaseOrderTypeCode, ReleaseNumber, SalesOrderNumber, RevisionNumber, )
supermod.PurchaseOrderInformation.subclass = PurchaseOrderInformationSub
# end class PurchaseOrderInformationSub


class PurchaseOrderReferenceInformationSub(supermod.PurchaseOrderReferenceInformation):
    def __init__(self, OrderNumber=None, OrderDate=None, LineItemNumber=None, ChangeSequenceNumber=None, ReleaseNumber=None):
        super(PurchaseOrderReferenceInformationSub, self).__init__(OrderNumber, OrderDate, LineItemNumber, ChangeSequenceNumber, ReleaseNumber, )
supermod.PurchaseOrderReferenceInformation.subclass = PurchaseOrderReferenceInformationSub
# end class PurchaseOrderReferenceInformationSub


class QuoteRequestInformationSub(supermod.QuoteRequestInformation):
    def __init__(self, QuoteRequestNumber=None, QuoteRequestDate=None, RevisionNumber=None):
        super(QuoteRequestInformationSub, self).__init__(QuoteRequestNumber, QuoteRequestDate, RevisionNumber, )
supermod.QuoteRequestInformation.subclass = QuoteRequestInformationSub
# end class QuoteRequestInformationSub


class RateOfExchangeDetailSub(supermod.RateOfExchangeDetail):
    def __init__(self, ReferenceCurrency=None, TargetCurrency=None, ExchangeRate=None, DateOfRateOfExchange=None):
        super(RateOfExchangeDetailSub, self).__init__(ReferenceCurrency, TargetCurrency, ExchangeRate, DateOfRateOfExchange, )
supermod.RateOfExchangeDetail.subclass = RateOfExchangeDetailSub
# end class RateOfExchangeDetailSub


class ReferenceCurrencySub(supermod.ReferenceCurrency):
    def __init__(self, CurrencyCode=None):
        super(ReferenceCurrencySub, self).__init__(CurrencyCode, )
supermod.ReferenceCurrency.subclass = ReferenceCurrencySub
# end class ReferenceCurrencySub


class ReferenceInformationSub(supermod.ReferenceInformation):
    def __init__(self, referenceInformationIndicator=None, ReferenceNumber=None, Description=None):
        super(ReferenceInformationSub, self).__init__(referenceInformationIndicator, ReferenceNumber, Description, )
supermod.ReferenceInformation.subclass = ReferenceInformationSub
# end class ReferenceInformationSub


class RequestedDocumentSub(supermod.RequestedDocument):
    def __init__(self, DocumentReference=None, DocumentDeliveryInformation=None, NumberOfOriginals=None, NumberOfCopies=None):
        super(RequestedDocumentSub, self).__init__(DocumentReference, DocumentDeliveryInformation, NumberOfOriginals, NumberOfCopies, )
supermod.RequestedDocument.subclass = RequestedDocumentSub
# end class RequestedDocumentSub


class RequestQuoteResponseSub(supermod.RequestQuoteResponse):
    def __init__(self, OpenDate=None, CloseDate=None, ContactInformation=None, ResponseInstructions=None):
        super(RequestQuoteResponseSub, self).__init__(OpenDate, CloseDate, ContactInformation, ResponseInstructions, )
supermod.RequestQuoteResponse.subclass = RequestQuoteResponseSub
# end class RequestQuoteResponseSub


class ResultingOrderTypeSub(supermod.ResultingOrderType):
    def __init__(self, PurchaseOrderTypeCode=None):
        super(ResultingOrderTypeSub, self).__init__(PurchaseOrderTypeCode, )
supermod.ResultingOrderType.subclass = ResultingOrderTypeSub
# end class ResultingOrderTypeSub


class RigIdentifierSub(supermod.RigIdentifier):
    def __init__(self, rigIdentifierType=None, valueOf_=None):
        super(RigIdentifierSub, self).__init__(rigIdentifierType, valueOf_, )
supermod.RigIdentifier.subclass = RigIdentifierSub
# end class RigIdentifierSub


class SampleMeasuresSub(supermod.SampleMeasures):
    def __init__(self, PartnerDefinedMeasure=None, ObservedDensity=None, ObservedTemperature=None, APIGravity=None, AverageTemperature=None, AveragePressure=None, AverageFlowRate=None, CorrectedGravity=None, CorrectedTemperatureLiquidFactor=None, CorrectedPressureLiquidFactor=None, CorrectedDensity=None, CompositeFactor=None, PercentLoaded=None, FlashTemperature=None, Haze=None, LineItemColor=None, Microseparometer=None, IncrustationFactor=None):
        super(SampleMeasuresSub, self).__init__(PartnerDefinedMeasure, ObservedDensity, ObservedTemperature, APIGravity, AverageTemperature, AveragePressure, AverageFlowRate, CorrectedGravity, CorrectedTemperatureLiquidFactor, CorrectedPressureLiquidFactor, CorrectedDensity, CompositeFactor, PercentLoaded, FlashTemperature, Haze, LineItemColor, Microseparometer, IncrustationFactor, )
supermod.SampleMeasures.subclass = SampleMeasuresSub
# end class SampleMeasuresSub


class SecondCurrencySub(supermod.SecondCurrency):
    def __init__(self, CurrencyCode=None):
        super(SecondCurrencySub, self).__init__(CurrencyCode, )
supermod.SecondCurrency.subclass = SecondCurrencySub
# end class SecondCurrencySub


class SellersCurrencySub(supermod.SellersCurrency):
    def __init__(self, CurrencyCode=None):
        super(SellersCurrencySub, self).__init__(CurrencyCode, )
supermod.SellersCurrency.subclass = SellersCurrencySub
# end class SellersCurrencySub


class ServiceDateTimeSub(supermod.ServiceDateTime):
    def __init__(self, dateTypeIndicator=None, valueOf_=None):
        super(ServiceDateTimeSub, self).__init__(dateTypeIndicator, valueOf_, )
supermod.ServiceDateTime.subclass = ServiceDateTimeSub
# end class ServiceDateTimeSub


class ShipmentTermsSub(supermod.ShipmentTerms):
    def __init__(self, ShipmentTermsCode=None, ShipmentTermsLocation=None):
        super(ShipmentTermsSub, self).__init__(ShipmentTermsCode, ShipmentTermsLocation, )
supermod.ShipmentTerms.subclass = ShipmentTermsSub
# end class ShipmentTermsSub


class ShipmentPackagingSub(supermod.ShipmentPackaging):
    def __init__(self, PackageDetail=None):
        super(ShipmentPackagingSub, self).__init__(PackageDetail, )
supermod.ShipmentPackaging.subclass = ShipmentPackagingSub
# end class ShipmentPackagingSub


class ShipmentTermsLocationSub(supermod.ShipmentTermsLocation):
    def __init__(self, codeListName=None, valueOf_=None):
        super(ShipmentTermsLocationSub, self).__init__(codeListName, valueOf_, )
supermod.ShipmentTermsLocation.subclass = ShipmentTermsLocationSub
# end class ShipmentTermsLocationSub


class ShipNoticeEquipmentDetailsSub(supermod.ShipNoticeEquipmentDetails):
    def __init__(self, LineItemNumber=None, EquipmentIdentifier=None, CarrierEquipmentCode=None, EquipmentOwnership=None, NumberOfUnits=None, SpecialInstructions=None, Height=None, Width=None, Length=None, NetWeight=None, TareWeight=None, GrossWeight=None, NetVolume=None, GrossVolume=None, SealNumber=None, EquipmentLoadEmptyStatus=None):
        super(ShipNoticeEquipmentDetailsSub, self).__init__(LineItemNumber, EquipmentIdentifier, CarrierEquipmentCode, EquipmentOwnership, NumberOfUnits, SpecialInstructions, Height, Width, Length, NetWeight, TareWeight, GrossWeight, NetVolume, GrossVolume, SealNumber, EquipmentLoadEmptyStatus, )
supermod.ShipNoticeEquipmentDetails.subclass = ShipNoticeEquipmentDetailsSub
# end class ShipNoticeEquipmentDetailsSub


class SpecialInstructionsSub(supermod.SpecialInstructions):
    def __init__(self, definitionOfOther=None, instructionIndicator=None, valueOf_=None):
        super(SpecialInstructionsSub, self).__init__(definitionOfOther, instructionIndicator, valueOf_, )
supermod.SpecialInstructions.subclass = SpecialInstructionsSub
# end class SpecialInstructionsSub


class TankCloseMeasuresSub(supermod.TankCloseMeasures):
    def __init__(self, AdjustmentQuantity=None, AmbientTemperature=None, APIGravity=None, CorrectedQuantity=None, CorrectedGravity=None, TankDateTime=None, GaugeReadingMeasure=None, GaugeQuantity=None, ReadingQuantity=None, TankWaterQuantity=None, TankWaterMeasure=None, TankTemperature=None, AdjustedRoofQuantity=None, CorrectedTemperatureLiquidFactor=None, PartnerDefinedMeasure=None):
        super(TankCloseMeasuresSub, self).__init__(AdjustmentQuantity, AmbientTemperature, APIGravity, CorrectedQuantity, CorrectedGravity, TankDateTime, GaugeReadingMeasure, GaugeQuantity, ReadingQuantity, TankWaterQuantity, TankWaterMeasure, TankTemperature, AdjustedRoofQuantity, CorrectedTemperatureLiquidFactor, PartnerDefinedMeasure, )
supermod.TankCloseMeasures.subclass = TankCloseMeasuresSub
# end class TankCloseMeasuresSub


class TankHeightSub(supermod.TankHeight):
    def __init__(self, Measurement=None, UnitOfMeasureCode=None):
        super(TankHeightSub, self).__init__(Measurement, UnitOfMeasureCode, )
supermod.TankHeight.subclass = TankHeightSub
# end class TankHeightSub


class TankMeasuresSub(supermod.TankMeasures):
    def __init__(self, TankHeight=None, TankCapacityQuantity=None, PartnerDefinedMeasure=None, TankOpenMeasures=None, TankCloseMeasures=None):
        super(TankMeasuresSub, self).__init__(TankHeight, TankCapacityQuantity, PartnerDefinedMeasure, TankOpenMeasures, TankCloseMeasures, )
supermod.TankMeasures.subclass = TankMeasuresSub
# end class TankMeasuresSub


class TankOpenMeasuresSub(supermod.TankOpenMeasures):
    def __init__(self, AdjustmentQuantity=None, AmbientTemperature=None, APIGravity=None, CorrectedQuantity=None, CorrectedGravity=None, TankDateTime=None, GaugeReadingMeasure=None, GaugeQuantity=None, ReadingQuantity=None, TankWaterQuantity=None, TankWaterMeasure=None, TankTemperature=None, AdjustedRoofQuantity=None, CorrectedTemperatureLiquidFactor=None, PartnerDefinedMeasure=None):
        super(TankOpenMeasuresSub, self).__init__(AdjustmentQuantity, AmbientTemperature, APIGravity, CorrectedQuantity, CorrectedGravity, TankDateTime, GaugeReadingMeasure, GaugeQuantity, ReadingQuantity, TankWaterQuantity, TankWaterMeasure, TankTemperature, AdjustedRoofQuantity, CorrectedTemperatureLiquidFactor, PartnerDefinedMeasure, )
supermod.TankOpenMeasures.subclass = TankOpenMeasuresSub
# end class TankOpenMeasuresSub


class TankTemperatureSub(supermod.TankTemperature):
    def __init__(self, Temperature=None, UnitOfMeasureCode=None):
        super(TankTemperatureSub, self).__init__(Temperature, UnitOfMeasureCode, )
supermod.TankTemperature.subclass = TankTemperatureSub
# end class TankTemperatureSub


class TankWaterMeasureSub(supermod.TankWaterMeasure):
    def __init__(self, Measurement=None, UnitOfMeasureCode=None):
        super(TankWaterMeasureSub, self).__init__(Measurement, UnitOfMeasureCode, )
supermod.TankWaterMeasure.subclass = TankWaterMeasureSub
# end class TankWaterMeasureSub


class TargetCurrencySub(supermod.TargetCurrency):
    def __init__(self, CurrencyCode=None):
        super(TargetCurrencySub, self).__init__(CurrencyCode, )
supermod.TargetCurrency.subclass = TargetCurrencySub
# end class TargetCurrencySub


class TaxCertificateNumberSub(supermod.TaxCertificateNumber):
    def __init__(self, taxCertificateType=None, valueOf_=None):
        super(TaxCertificateNumberSub, self).__init__(taxCertificateType, valueOf_, )
supermod.TaxCertificateNumber.subclass = TaxCertificateNumberSub
# end class TaxCertificateNumberSub


class TaxIdentifierNumberSub(supermod.TaxIdentifierNumber):
    def __init__(self, taxType=None, valueOf_=None):
        super(TaxIdentifierNumberSub, self).__init__(taxType, valueOf_, )
supermod.TaxIdentifierNumber.subclass = TaxIdentifierNumberSub
# end class TaxIdentifierNumberSub


class TaxInformationSub(supermod.TaxInformation):
    def __init__(self, TaxIdentifierNumber=None, Jurisdiction=None, TaxCertificateNumber=None, TaxBasisAmount=None, TaxRate=None, DateTimeRange=None, TaxCertificateType=None):
        super(TaxInformationSub, self).__init__(TaxIdentifierNumber, Jurisdiction, TaxCertificateNumber, TaxBasisAmount, TaxRate, DateTimeRange, TaxCertificateType, )
supermod.TaxInformation.subclass = TaxInformationSub
# end class TaxInformationSub


class TaxLocationSub(supermod.TaxLocation):
    def __init__(self, LocationIdentifier=None, LocationName=None, LocationDescription=None, AddressInformation=None):
        super(TaxLocationSub, self).__init__(LocationIdentifier, LocationName, LocationDescription, AddressInformation, )
supermod.TaxLocation.subclass = TaxLocationSub
# end class TaxLocationSub


class TelephoneSub(supermod.Telephone):
    def __init__(self, telephoneIndicator=None, PhoneNumber=None, PhoneNumberExtension=None, TelecomCountryCode=None, TelecomAreaCode=None):
        super(TelephoneSub, self).__init__(telephoneIndicator, PhoneNumber, PhoneNumberExtension, TelecomCountryCode, TelecomAreaCode, )
supermod.Telephone.subclass = TelephoneSub
# end class TelephoneSub


class TemperatureSub(supermod.Temperature):
    def __init__(self, TemperatureUnitOfMeasurement=None, valueOf_=None):
        super(TemperatureSub, self).__init__(TemperatureUnitOfMeasurement, valueOf_, )
supermod.Temperature.subclass = TemperatureSub
# end class TemperatureSub


class TransportInformationSub(supermod.TransportInformation):
    def __init__(self, stageIdentifier=None, ShipmentMethodOfPayment=None, RoutingSequenceCode=None, TransportMethodCode=None, PartnerInformation=None, Location=None, ShipmentTermsCode=None, Routing=None, ServiceLevelCode=None, HazardousMaterials=None, CarrierEquipmentCode=None, TransportName=None, TransportMethod=None, DocumentReference=None):
        super(TransportInformationSub, self).__init__(stageIdentifier, ShipmentMethodOfPayment, RoutingSequenceCode, TransportMethodCode, PartnerInformation, Location, ShipmentTermsCode, Routing, ServiceLevelCode, HazardousMaterials, CarrierEquipmentCode, TransportName, TransportMethod, DocumentReference, )
supermod.TransportInformation.subclass = TransportInformationSub
# end class TransportInformationSub


class TransportMethodSub(supermod.TransportMethod):
    def __init__(self, codeListName=None, valueOf_=None):
        super(TransportMethodSub, self).__init__(codeListName, valueOf_, )
supermod.TransportMethod.subclass = TransportMethodSub
# end class TransportMethodSub


class UnitPriceSub(supermod.UnitPrice):
    def __init__(self, MonetaryAmount=None, UnitOfMeasureCode=None, CurrencyCode=None):
        super(UnitPriceSub, self).__init__(MonetaryAmount, UnitOfMeasureCode, CurrencyCode, )
supermod.UnitPrice.subclass = UnitPriceSub
# end class UnitPriceSub


class ValidityDatesSub(supermod.ValidityDates):
    def __init__(self, FromDate=None, ToDate=None):
        super(ValidityDatesSub, self).__init__(FromDate, ToDate, )
supermod.ValidityDates.subclass = ValidityDatesSub
# end class ValidityDatesSub


class VesselMeasuresSub(supermod.VesselMeasures):
    def __init__(self, VesselType=None, VesselDescription=None, VesselPurged=None, VaporFactor=None, VesselCapacityQuantity=None, VolumeOutageQuantity=None, PurgedQuantity=None, PartnerDefinedMeasure=None):
        super(VesselMeasuresSub, self).__init__(VesselType, VesselDescription, VesselPurged, VaporFactor, VesselCapacityQuantity, VolumeOutageQuantity, PurgedQuantity, PartnerDefinedMeasure, )
supermod.VesselMeasures.subclass = VesselMeasuresSub
# end class VesselMeasuresSub


class WellInformationSub(supermod.WellInformation):
    def __init__(self, WellIdentifier=None, WellName=None, WellType=None, WellCategory=None):
        super(WellInformationSub, self).__init__(WellIdentifier, WellName, WellType, WellCategory, )
supermod.WellInformation.subclass = WellInformationSub
# end class WellInformationSub


class AdvancedShipNoticeLineItemsTypeSub(supermod.AdvancedShipNoticeLineItemsType):
    def __init__(self, LineItemNumber=None, EquipmentDetailsLineNumber=None, RevisionNumber=None, ProductInformation=None, ShippedQuantity=None, OrderQuantity=None, InvoiceQuantity=None, PackagingQuantity=None, CumulativeTotalQuantity=None, LineItemText=None, DocumentReference=None, ShipmentIndicator=None, PartnerInformation=None, DateTimeRange=None, ShipmentTerms=None, ScheduleDateTime=None, ScheduleDateTimeRange=None, SpecialInstructions=None, RequestedDocument=None, Routing=None, CustomerSpecificInformation=None, PercentActive=None, ProductSubLineItems=None, PackagingInformation=None, Comment=None):
        super(AdvancedShipNoticeLineItemsTypeSub, self).__init__(LineItemNumber, EquipmentDetailsLineNumber, RevisionNumber, ProductInformation, ShippedQuantity, OrderQuantity, InvoiceQuantity, PackagingQuantity, CumulativeTotalQuantity, LineItemText, DocumentReference, ShipmentIndicator, PartnerInformation, DateTimeRange, ShipmentTerms, ScheduleDateTime, ScheduleDateTimeRange, SpecialInstructions, RequestedDocument, Routing, CustomerSpecificInformation, PercentActive, ProductSubLineItems, PackagingInformation, Comment, )
supermod.AdvancedShipNoticeLineItemsType.subclass = AdvancedShipNoticeLineItemsTypeSub
# end class AdvancedShipNoticeLineItemsTypeSub


class CompanyInformationTypeSub(supermod.CompanyInformationType):
    def __init__(self, CompanyCode=None, CompanyFEIN=None, CompanyName=None):
        super(CompanyInformationTypeSub, self).__init__(CompanyCode, CompanyFEIN, CompanyName, )
supermod.CompanyInformationType.subclass = CompanyInformationTypeSub
# end class CompanyInformationTypeSub


class CustodyPartnerTypeSub(supermod.CustodyPartnerType):
    def __init__(self, PartnerInformation=None, PartnerEntityIdentifier=None, PartnerFacilityIdentifier=None):
        super(CustodyPartnerTypeSub, self).__init__(PartnerInformation, PartnerEntityIdentifier, PartnerFacilityIdentifier, )
supermod.CustodyPartnerType.subclass = CustodyPartnerTypeSub
# end class CustodyPartnerTypeSub


class DateTimeRangeTypeSub(supermod.DateTimeRangeType):
    def __init__(self, definitionOfOther=None, rangeType=None, FromDateTime=None, ToDateTime=None):
        super(DateTimeRangeTypeSub, self).__init__(definitionOfOther, rangeType, FromDateTime, ToDateTime, )
supermod.DateTimeRangeType.subclass = DateTimeRangeTypeSub
# end class DateTimeRangeTypeSub


class DescriptionTypeSub(supermod.DescriptionType):
    def __init__(self, Description=None, LanguageCode=None):
        super(DescriptionTypeSub, self).__init__(Description, LanguageCode, )
supermod.DescriptionType.subclass = DescriptionTypeSub
# end class DescriptionTypeSub


class ErrorsTypeSub(supermod.ErrorsType):
    def __init__(self, Error=None):
        super(ErrorsTypeSub, self).__init__(Error, )
supermod.ErrorsType.subclass = ErrorsTypeSub
# end class ErrorsTypeSub


class FreeTextTypeSub(supermod.FreeTextType):
    def __init__(self, Language=None, valueOf_=None, extensiontype_=None):
        super(FreeTextTypeSub, self).__init__(Language, valueOf_, extensiontype_, )
supermod.FreeTextType.subclass = FreeTextTypeSub
# end class FreeTextTypeSub


class InvoiceResponseReasonTypeSub(supermod.InvoiceResponseReasonType):
    def __init__(self, ResponseReasonCode=None, ResponseReasonCodeXPath=None, ResponseReasonComments=None):
        super(InvoiceResponseReasonTypeSub, self).__init__(ResponseReasonCode, ResponseReasonCodeXPath, ResponseReasonComments, )
supermod.InvoiceResponseReasonType.subclass = InvoiceResponseReasonTypeSub
# end class InvoiceResponseReasonTypeSub


class LineItemsTypeSub(supermod.LineItemsType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None, extensiontype_=None):
        super(LineItemsTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, extensiontype_, )
supermod.LineItemsType.subclass = LineItemsTypeSub
# end class LineItemsTypeSub


class MeasurementTypeSub(supermod.MeasurementType):
    def __init__(self, Measurement=None, UnitOfMeasureCode=None):
        super(MeasurementTypeSub, self).__init__(Measurement, UnitOfMeasureCode, )
supermod.MeasurementType.subclass = MeasurementTypeSub
# end class MeasurementTypeSub


class MonetaryTypeSub(supermod.MonetaryType):
    def __init__(self, MonetaryAmount=None, CurrencyCode=None, extensiontype_=None):
        super(MonetaryTypeSub, self).__init__(MonetaryAmount, CurrencyCode, extensiontype_, )
supermod.MonetaryType.subclass = MonetaryTypeSub
# end class MonetaryTypeSub


class OrderChangeCancelLineItemsTypeSub(supermod.OrderChangeCancelLineItemsType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None, PurchaseOrderReferenceInformation=None, LineItemRequestedAction=None, AccompanyingSampleCode=None):
        super(OrderChangeCancelLineItemsTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, PurchaseOrderReferenceInformation, LineItemRequestedAction, AccompanyingSampleCode, )
supermod.OrderChangeCancelLineItemsType.subclass = OrderChangeCancelLineItemsTypeSub
# end class OrderChangeCancelLineItemsTypeSub


class OrderStatusLineItemsRequestTypeSub(supermod.OrderStatusLineItemsRequestType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None):
        super(OrderStatusLineItemsRequestTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, )
supermod.OrderStatusLineItemsRequestType.subclass = OrderStatusLineItemsRequestTypeSub
# end class OrderStatusLineItemsRequestTypeSub


class OrderLineItemsTypeSub(supermod.OrderLineItemsType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None, RevisionNumber=None, ProductInformation=None, OrderQuantity=None, PackagingQuantity=None, LineItemPurposeCode=None, EngineeringChangeOrderIdentifier=None, BatchNumber=None, CountryOfOrigin=None, CountryOfFinalDestination=None, DeliveryTolerances=None, ShipmentTerms=None, ScheduleDateTime=None, ScheduleDateTimeRange=None, TransportInformation=None, RequestedDocument=None, Routing=None, SpecialServicesRequest=None, PackListRequirements=None, QuoteIdentifier=None, Label=None, ImportLicenseNeededFlag=None, ImportLicenseAvailableFlag=None, AccompanyingSampleCode=None, JobLocationClassCode=None, extensiontype_=None):
        super(OrderLineItemsTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, RevisionNumber, ProductInformation, OrderQuantity, PackagingQuantity, LineItemPurposeCode, EngineeringChangeOrderIdentifier, BatchNumber, CountryOfOrigin, CountryOfFinalDestination, DeliveryTolerances, ShipmentTerms, ScheduleDateTime, ScheduleDateTimeRange, TransportInformation, RequestedDocument, Routing, SpecialServicesRequest, PackListRequirements, QuoteIdentifier, Label, ImportLicenseNeededFlag, ImportLicenseAvailableFlag, AccompanyingSampleCode, JobLocationClassCode, extensiontype_, )
supermod.OrderLineItemsType.subclass = OrderLineItemsTypeSub
# end class OrderLineItemsTypeSub


class PartnerConfirmationStatusTypeSub(supermod.PartnerConfirmationStatusType):
    def __init__(self, PartnerInformation=None, ConfirmationDateTime=None, ConfirmationStatusCode=None):
        super(PartnerConfirmationStatusTypeSub, self).__init__(PartnerInformation, ConfirmationDateTime, ConfirmationStatusCode, )
supermod.PartnerConfirmationStatusType.subclass = PartnerConfirmationStatusTypeSub
# end class PartnerConfirmationStatusTypeSub


class PartnerEventActionSub(supermod.PartnerEventAction):
    def __init__(self, PartnerInformation=None, EventDateTime=None):
        super(PartnerEventActionSub, self).__init__(PartnerInformation, EventDateTime, )
supermod.PartnerEventAction.subclass = PartnerEventActionSub
# end class PartnerEventActionSub


class PipelineEventInformationTypeSub(supermod.PipelineEventInformationType):
    def __init__(self, PipelineEvent=None, PipelineEventVolumeAffect=None, PipelineEventStatus=None, PipelineEventDescription=None, PipelineCustodyEvent=None, AllowPartnerChange=None, AffectShipperInventory=None):
        super(PipelineEventInformationTypeSub, self).__init__(PipelineEvent, PipelineEventVolumeAffect, PipelineEventStatus, PipelineEventDescription, PipelineCustodyEvent, AllowPartnerChange, AffectShipperInventory, )
supermod.PipelineEventInformationType.subclass = PipelineEventInformationTypeSub
# end class PipelineEventInformationTypeSub


class ProductCharacteristicsTypeSub(supermod.ProductCharacteristicsType):
    def __init__(self, DyesFlag=None, OXY=None, CetaneOctane=None, FungibleSegregated=None, SulfurContent=None, RVP=None, Additized=None, OxygenatePercent=None, RFGFlag=None):
        super(ProductCharacteristicsTypeSub, self).__init__(DyesFlag, OXY, CetaneOctane, FungibleSegregated, SulfurContent, RVP, Additized, OxygenatePercent, RFGFlag, )
supermod.ProductCharacteristicsType.subclass = ProductCharacteristicsTypeSub
# end class ProductCharacteristicsTypeSub


class ProductTypeSub(supermod.ProductType):
    def __init__(self, ProductCode=None, ProductName=None, ProductDescription=None, GrossQuantity=None, Temperature=None, Gravity=None, NetQuantity=None, ProductCharacteristics=None, extensiontype_=None):
        super(ProductTypeSub, self).__init__(ProductCode, ProductName, ProductDescription, GrossQuantity, Temperature, Gravity, NetQuantity, ProductCharacteristics, extensiontype_, )
supermod.ProductType.subclass = ProductTypeSub
# end class ProductTypeSub


class QuantityTypeSub(supermod.QuantityType):
    def __init__(self, Quantity=None, UnitOfMeasureCode=None):
        super(QuantityTypeSub, self).__init__(Quantity, UnitOfMeasureCode, )
supermod.QuantityType.subclass = QuantityTypeSub
# end class QuantityTypeSub


class ReceiptLineItemsTypeSub(supermod.ReceiptLineItemsType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None, StorageTankIdentifier=None):
        super(ReceiptLineItemsTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, StorageTankIdentifier, )
supermod.ReceiptLineItemsType.subclass = ReceiptLineItemsTypeSub
# end class ReceiptLineItemsTypeSub


class SuccessTypeSub(supermod.SuccessType):
    def __init__(self):
        super(SuccessTypeSub, self).__init__()
supermod.SuccessType.subclass = SuccessTypeSub
# end class SuccessTypeSub


class TaxTypeSub(supermod.TaxType):
    def __init__(self, TaxTypeCode=None, MixedRateIndicator=None, TaxIdentifierNumber=None, TaxExemptCode=None, TaxLocation=None, TaxRate=None, TaxBasisAmount=None, TaxAmount=None, TaxReference=None, DeferredAmount=None, extensiontype_=None):
        super(TaxTypeSub, self).__init__(TaxTypeCode, MixedRateIndicator, TaxIdentifierNumber, TaxExemptCode, TaxLocation, TaxRate, TaxBasisAmount, TaxAmount, TaxReference, DeferredAmount, extensiontype_, )
supermod.TaxType.subclass = TaxTypeSub
# end class TaxTypeSub


class TerminalInformationTypeSub(supermod.TerminalInformationType):
    def __init__(self, TerminalSPLC=None, TerminalTimeZone=None, TerminalControlNumber=None, TerminalName=None, EPAFacilityID=None, EPAEntityID=None, AddressInformation=None):
        super(TerminalInformationTypeSub, self).__init__(TerminalSPLC, TerminalTimeZone, TerminalControlNumber, TerminalName, EPAFacilityID, EPAEntityID, AddressInformation, )
supermod.TerminalInformationType.subclass = TerminalInformationTypeSub
# end class TerminalInformationTypeSub


class WarningsTypeSub(supermod.WarningsType):
    def __init__(self, Warning=None):
        super(WarningsTypeSub, self).__init__(Warning, )
supermod.WarningsType.subclass = WarningsTypeSub
# end class WarningsTypeSub


class WellIdentifierTypeSub(supermod.WellIdentifierType):
    def __init__(self, wellIdentifierIndicator=None, valueOf_=None):
        super(WellIdentifierTypeSub, self).__init__(wellIdentifierIndicator, valueOf_, )
supermod.WellIdentifierType.subclass = WellIdentifierTypeSub
# end class WellIdentifierTypeSub


class CompartmentInfoTypeSub(supermod.CompartmentInfoType):
    def __init__(self, CompartmentId=None, VehicleNumber=None):
        super(CompartmentInfoTypeSub, self).__init__(CompartmentId, VehicleNumber, )
supermod.CompartmentInfoType.subclass = CompartmentInfoTypeSub
# end class CompartmentInfoTypeSub


class AdvisingBankTypeSub(supermod.AdvisingBankType):
    def __init__(self, PartnerInformation=None):
        super(AdvisingBankTypeSub, self).__init__(PartnerInformation, )
supermod.AdvisingBankType.subclass = AdvisingBankTypeSub
# end class AdvisingBankTypeSub


class LetterOfCreditQuantityTypeSub(supermod.LetterOfCreditQuantityType):
    def __init__(self, MinimumQuantity=None, ActualQuantity=None, MaximumQuantity=None):
        super(LetterOfCreditQuantityTypeSub, self).__init__(MinimumQuantity, ActualQuantity, MaximumQuantity, )
supermod.LetterOfCreditQuantityType.subclass = LetterOfCreditQuantityTypeSub
# end class LetterOfCreditQuantityTypeSub


class OrderResponseLineItemsTypeSub(supermod.OrderResponseLineItemsType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None, RevisionNumber=None, ProductInformation=None, OrderQuantity=None, PackagingQuantity=None, LineItemPurposeCode=None, EngineeringChangeOrderIdentifier=None, BatchNumber=None, CountryOfOrigin=None, CountryOfFinalDestination=None, DeliveryTolerances=None, ShipmentTerms=None, ScheduleDateTime=None, ScheduleDateTimeRange=None, TransportInformation=None, RequestedDocument=None, Routing=None, SpecialServicesRequest=None, PackListRequirements=None, QuoteIdentifier=None, Label=None, ImportLicenseNeededFlag=None, ImportLicenseAvailableFlag=None, AccompanyingSampleCode=None, JobLocationClassCode=None, StatusCode=None, ResponseReason=None, extensiontype_=None):
        super(OrderResponseLineItemsTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, RevisionNumber, ProductInformation, OrderQuantity, PackagingQuantity, LineItemPurposeCode, EngineeringChangeOrderIdentifier, BatchNumber, CountryOfOrigin, CountryOfFinalDestination, DeliveryTolerances, ShipmentTerms, ScheduleDateTime, ScheduleDateTimeRange, TransportInformation, RequestedDocument, Routing, SpecialServicesRequest, PackListRequirements, QuoteIdentifier, Label, ImportLicenseNeededFlag, ImportLicenseAvailableFlag, AccompanyingSampleCode, JobLocationClassCode, StatusCode, ResponseReason, extensiontype_, )
supermod.OrderResponseLineItemsType.subclass = OrderResponseLineItemsTypeSub
# end class OrderResponseLineItemsTypeSub


class ErrorWarningTypeSub(supermod.ErrorWarningType):
    def __init__(self, Language=None, Status=None, Code=None, RecordID=None, ShortText=None, Tag=None, Type=None, DocURL=None, valueOf_=None):
        super(ErrorWarningTypeSub, self).__init__(Language, Status, Code, RecordID, ShortText, Tag, Type, DocURL, valueOf_, )
supermod.ErrorWarningType.subclass = ErrorWarningTypeSub
# end class ErrorWarningTypeSub


class AdvancedShipmentNoticeLineItemsTypeSub(supermod.AdvancedShipmentNoticeLineItemsType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None, StorageTankIdentifier=None):
        super(AdvancedShipmentNoticeLineItemsTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, StorageTankIdentifier, )
supermod.AdvancedShipmentNoticeLineItemsType.subclass = AdvancedShipmentNoticeLineItemsTypeSub
# end class AdvancedShipmentNoticeLineItemsTypeSub


class TaxSummarySub(supermod.TaxSummary):
    def __init__(self, TaxTypeCode=None, MixedRateIndicator=None, TaxIdentifierNumber=None, TaxExemptCode=None, TaxLocation=None, TaxRate=None, TaxBasisAmount=None, TaxAmount=None, TaxReference=None, DeferredAmount=None):
        super(TaxSummarySub, self).__init__(TaxTypeCode, MixedRateIndicator, TaxIdentifierNumber, TaxExemptCode, TaxLocation, TaxRate, TaxBasisAmount, TaxAmount, TaxReference, DeferredAmount, )
supermod.TaxSummary.subclass = TaxSummarySub
# end class TaxSummarySub


class SubTotalAmountSub(supermod.SubTotalAmount):
    def __init__(self, MonetaryAmount=None, CurrencyCode=None, subTotalIndicator=None):
        super(SubTotalAmountSub, self).__init__(MonetaryAmount, CurrencyCode, subTotalIndicator, )
supermod.SubTotalAmount.subclass = SubTotalAmountSub
# end class SubTotalAmountSub


class PriceAmountSub(supermod.PriceAmount):
    def __init__(self, MonetaryAmount=None, CurrencyCode=None, definitionOfOther=None, priceType=None):
        super(PriceAmountSub, self).__init__(MonetaryAmount, CurrencyCode, definitionOfOther, priceType, )
supermod.PriceAmount.subclass = PriceAmountSub
# end class PriceAmountSub


class FinishedProductTypeSub(supermod.FinishedProductType):
    def __init__(self, ProductCode=None, ProductName=None, ProductDescription=None, GrossQuantity=None, Temperature=None, Gravity=None, NetQuantity=None, ProductCharacteristics=None, BlendOrAlterationIndicator=None, ComponentProduct=None, CompartmentInfo=None):
        super(FinishedProductTypeSub, self).__init__(ProductCode, ProductName, ProductDescription, GrossQuantity, Temperature, Gravity, NetQuantity, ProductCharacteristics, BlendOrAlterationIndicator, ComponentProduct, CompartmentInfo, )
supermod.FinishedProductType.subclass = FinishedProductTypeSub
# end class FinishedProductTypeSub


class VehicleInformationSub(supermod.VehicleInformation):
    def __init__(self, VehicleType=None, VehicleNumber=None):
        super(VehicleInformationSub, self).__init__(VehicleType, VehicleNumber, )
supermod.VehicleInformation.subclass = VehicleInformationSub
# end class VehicleInformationSub


class OrderStatusResponseLineItemsTypeSub(supermod.OrderStatusResponseLineItemsType):
    def __init__(self, LineItemNumber=None, DocumentReference=None, PartnerInformation=None, CustomerSpecificInformation=None, Comment=None, RevisionNumber=None, ProductInformation=None, OrderQuantity=None, PackagingQuantity=None, LineItemPurposeCode=None, EngineeringChangeOrderIdentifier=None, BatchNumber=None, CountryOfOrigin=None, CountryOfFinalDestination=None, DeliveryTolerances=None, ShipmentTerms=None, ScheduleDateTime=None, ScheduleDateTimeRange=None, TransportInformation=None, RequestedDocument=None, Routing=None, SpecialServicesRequest=None, PackListRequirements=None, QuoteIdentifier=None, Label=None, ImportLicenseNeededFlag=None, ImportLicenseAvailableFlag=None, AccompanyingSampleCode=None, JobLocationClassCode=None, StatusCode=None, ResponseReason=None, ProprietaryShipmentTrackingIdentifier=None):
        super(OrderStatusResponseLineItemsTypeSub, self).__init__(LineItemNumber, DocumentReference, PartnerInformation, CustomerSpecificInformation, Comment, RevisionNumber, ProductInformation, OrderQuantity, PackagingQuantity, LineItemPurposeCode, EngineeringChangeOrderIdentifier, BatchNumber, CountryOfOrigin, CountryOfFinalDestination, DeliveryTolerances, ShipmentTerms, ScheduleDateTime, ScheduleDateTimeRange, TransportInformation, RequestedDocument, Routing, SpecialServicesRequest, PackListRequirements, QuoteIdentifier, Label, ImportLicenseNeededFlag, ImportLicenseAvailableFlag, AccompanyingSampleCode, JobLocationClassCode, StatusCode, ResponseReason, ProprietaryShipmentTrackingIdentifier, )
supermod.OrderStatusResponseLineItemsType.subclass = OrderStatusResponseLineItemsTypeSub
# end class OrderStatusResponseLineItemsTypeSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BillOfLadingCreate'
        rootClass = supermod.BillOfLadingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj


def parseEtree(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BillOfLadingCreate'
        rootClass = supermod.BillOfLadingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BillOfLadingCreate'
        rootClass = supermod.BillOfLadingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'BillOfLadingCreate'
        rootClass = supermod.BillOfLadingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from BillOfLadingCreate import *\n\n')
    sys.stdout.write('import BillOfLadingCreate as model_\n\n')
    sys.stdout.write('rootObj = model_.BillOfLadingCreate(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="BillOfLadingCreate")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


