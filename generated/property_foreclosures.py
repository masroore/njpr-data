# generated by datamodel-codegen:
#   filename:  propertyForeclosures.json
#   timestamp: 2023-03-21T08:04:19+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class PropertyForeclosure(BaseModel):
    transaction_id: Optional[int] = Field(None, alias="TransactionID")
    attom_id: Optional[int] = Field(None, alias="AttomID")
    record_type: Optional[str] = Field(None, alias="RecordType")
    situs_state_code: Optional[str] = Field(None, alias="SitusStateCode")
    situs_county: Optional[str] = Field(None, alias="SitusCounty")
    property_jurisdiction_name: Optional[str] = Field(
        None, alias="PropertyJurisdictionName"
    )
    situs_state_county_fips: Optional[str] = Field(None, alias="SitusStateCountyFIPS")
    parcel_number_formatted: Optional[str] = Field(None, alias="ParcelNumberFormatted")
    property_address_full: Optional[str] = Field(None, alias="PropertyAddressFull")
    property_address_house_number: Optional[str] = Field(
        None, alias="PropertyAddressHouseNumber"
    )
    property_address_street_direction: Optional[Any] = Field(
        None, alias="PropertyAddressStreetDirection"
    )
    property_address_street_name: Optional[str] = Field(
        None, alias="PropertyAddressStreetName"
    )
    property_address_street_suffix: Optional[str] = Field(
        None, alias="PropertyAddressStreetSuffix"
    )
    property_address_street_post_direction: Optional[Any] = Field(
        None, alias="PropertyAddressStreetPostDirection"
    )
    property_address_unit_prefix: Optional[Any] = Field(
        None, alias="PropertyAddressUnitPrefix"
    )
    property_address_unit_value: Optional[Any] = Field(
        None, alias="PropertyAddressUnitValue"
    )
    property_address_city: Optional[str] = Field(None, alias="PropertyAddressCity")
    property_address_state: Optional[str] = Field(None, alias="PropertyAddressState")
    property_address_zip: Optional[str] = Field(None, alias="PropertyAddressZIP")
    property_address_zip4: Optional[str] = Field(None, alias="PropertyAddressZIP4")
    property_address_crrt: Optional[str] = Field(None, alias="PropertyAddressCRRT")
    property_address_info_privacy: Optional[Any] = Field(
        None, alias="PropertyAddressInfoPrivacy"
    )
    property_latitude: Optional[float] = Field(None, alias="PropertyLatitude")
    property_longitude: Optional[float] = Field(None, alias="PropertyLongitude")
    geo_quality: Optional[str] = Field(None, alias="GeoQuality")
    zoned_code_local: Optional[Any] = Field(None, alias="ZonedCodeLocal")
    property_use_muni: Optional[str] = Field(None, alias="PropertyUseMuni")
    property_use_group: Optional[str] = Field(None, alias="PropertyUseGroup")
    property_use_standardized: Optional[str] = Field(
        None, alias="PropertyUseStandardized"
    )
    bath_count: Optional[int] = Field(None, alias="BathCount")
    bedrooms_count: Optional[int] = Field(None, alias="BedroomsCount")
    area_building: Optional[int] = Field(None, alias="AreaBuilding")
    area_building_definition_code: Optional[str] = Field(
        None, alias="AreaBuildingDefinitionCode"
    )
    area_lot_sf: Optional[int] = Field(None, alias="AreaLotSF")
    area_lot_acres: Optional[float] = Field(None, alias="AreaLotAcres")
    year_built: Optional[int] = Field(None, alias="YearBuilt")
    year_built_effective: Optional[Any] = Field(None, alias="YearBuiltEffective")
    original_loan_recording_date: Optional[str] = Field(
        None, alias="OriginalLoanRecordingDate"
    )
    original_loan_instrument_number: Optional[str] = Field(
        None, alias="OriginalLoanInstrumentNumber"
    )
    original_loan_book_page: Optional[Any] = Field(None, alias="OriginalLoanBookPage")
    borrower_name_owner: Optional[str] = Field(None, alias="BorrowerNameOwner")
    original_loan_loan_number: Optional[Any] = Field(
        None, alias="OriginalLoanLoanNumber"
    )
    original_loan_amount: Optional[int] = Field(None, alias="OriginalLoanAmount")
    original_loan_interest_rate: Optional[Any] = Field(
        None, alias="OriginalLoanInterestRate"
    )
    loan_maturity_date: Optional[Any] = Field(None, alias="LoanMaturityDate")
    lender_name_full_standardized: Optional[str] = Field(
        None, alias="LenderNameFullStandardized"
    )
    lender_address: Optional[Any] = Field(None, alias="LenderAddress")
    lender_address_house_number: Optional[Any] = Field(
        None, alias="LenderAddressHouseNumber"
    )
    lender_address_street_direction: Optional[Any] = Field(
        None, alias="LenderAddressStreetDirection"
    )
    lender_address_street_name: Optional[Any] = Field(
        None, alias="LenderAddressStreetName"
    )
    lender_address_street_suffix: Optional[Any] = Field(
        None, alias="LenderAddressStreetSuffix"
    )
    lender_address_street_post_direction: Optional[Any] = Field(
        None, alias="LenderAddressStreetPostDirection"
    )
    lender_address_unit_value: Optional[Any] = Field(
        None, alias="LenderAddressUnitValue"
    )
    lender_address_city: Optional[Any] = Field(None, alias="LenderAddressCity")
    lender_address_state: Optional[Any] = Field(None, alias="LenderAddressState")
    lender_address_zip: Optional[Any] = Field(None, alias="LenderAddressZIP")
    lender_phone: Optional[Any] = Field(None, alias="LenderPhone")
    servicer_name: Optional[Any] = Field(None, alias="ServicerName")
    servicer_address: Optional[str] = Field(None, alias="ServicerAddress")
    servicer_city: Optional[Any] = Field(None, alias="ServicerCity")
    servicer_state: Optional[Any] = Field(None, alias="ServicerState")
    servicer_zip: Optional[Any] = Field(None, alias="ServicerZip")
    servicer_phone: Optional[Any] = Field(None, alias="ServicerPhone")
    trustee_name: Optional[str] = Field(None, alias="TrusteeName")
    trustee_address: Optional[str] = Field(None, alias="TrusteeAddress")
    trustee_address_house_number: Optional[Any] = Field(
        None, alias="TrusteeAddressHouseNumber"
    )
    trustee_address_street_direction: Optional[Any] = Field(
        None, alias="TrusteeAddressStreetDirection"
    )
    trustee_address_street_name: Optional[Any] = Field(
        None, alias="TrusteeAddressStreetName"
    )
    trustee_address_street_suffix: Optional[Any] = Field(
        None, alias="TrusteeAddressStreetSuffix"
    )
    trustee_address_street_post_direction: Optional[Any] = Field(
        None, alias="TrusteeAddressStreetPostDirection"
    )
    trustee_address_unit_value: Optional[Any] = Field(
        None, alias="TrusteeAddressUnitValue"
    )
    trustee_address_city: Optional[str] = Field(None, alias="TrusteeAddressCity")
    trustee_address_state: Optional[str] = Field(None, alias="TrusteeAddressState")
    trustee_address_zip: Optional[str] = Field(None, alias="TrusteeAddressZIP")
    trustee_phone: Optional[str] = Field(None, alias="TrusteePhone")
    foreclosure_instrument_date: Optional[Any] = Field(
        None, alias="ForeclosureInstrumentDate"
    )
    foreclosure_recording_date: Optional[str] = Field(
        None, alias="ForeclosureRecordingDate"
    )
    foreclosure_instrument_number: Optional[str] = Field(
        None, alias="ForeclosureInstrumentNumber"
    )
    foreclosure_book_page: Optional[Any] = Field(None, alias="ForeclosureBookPage")
    case_number: Optional[Any] = Field(None, alias="CaseNumber")
    trustee_reference_number: Optional[Any] = Field(
        None, alias="TrusteeReferenceNumber"
    )
    payment: Optional[Any] = Field(None, alias="Payment")
    default_amount: Optional[int] = Field(None, alias="DefaultAmount")
    penalty_interest: Optional[Any] = Field(None, alias="PenaltyInterest")
    loan_balance: Optional[Any] = Field(None, alias="LoanBalance")
    judgment_date: Optional[Any] = Field(None, alias="JudgmentDate")
    judgment_amount: Optional[float] = Field(None, alias="JudgmentAmount")
    courthouse: Optional[Any] = Field(None, alias="Courthouse")
    auction_address: Optional[str] = Field(None, alias="AuctionAddress")
    auction_house_number: Optional[Any] = Field(None, alias="AuctionHouseNumber")
    auction_direction: Optional[Any] = Field(None, alias="AuctionDirection")
    auction_street_name: Optional[Any] = Field(None, alias="AuctionStreetName")
    auction_suffix: Optional[Any] = Field(None, alias="AuctionSuffix")
    auction_post_direction: Optional[Any] = Field(None, alias="AuctionPostDirection")
    auction_unit: Optional[Any] = Field(None, alias="AuctionUnit")
    auction_city: Optional[str] = Field(None, alias="AuctionCity")
    auction_date: Optional[str] = Field(None, alias="AuctionDate")
    auction_time: Optional[str] = Field(None, alias="AuctionTime")
    recorded_auction_opening_bid: Optional[int] = Field(
        None, alias="RecordedAuctionOpeningBid"
    )
    estimated_value: Optional[Any] = Field(None, alias="EstimatedValue")
    create_date: Optional[str] = Field(None, alias="CreateDate")
    record_last_updated: Optional[str] = Field(None, alias="RecordLastUpdated")
    publication_date: Optional[str] = Field(None, alias="PublicationDate")


class Model(BaseModel):
    property_foreclosures: Optional[list[PropertyForeclosure]] = Field(
        None, alias="propertyForeclosures"
    )
