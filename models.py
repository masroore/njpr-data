from __future__ import annotations

from typing import Any, Optional, List

from pydantic import BaseModel, Field


class MunicipalityData(BaseModel):
    municipality: str = Field(..., alias="Municipality")
    county: str = Field(..., alias="County")
    name: str = Field(..., alias="Name")
    codebook__homepage: str = Field(..., alias="Codebook_Homepage")
    codebook__zoning: str = Field(..., alias="Codebook_Zoning")
    website: str = Field(..., alias="Website")
    clerk__website: str = Field(..., alias="Clerk_Website")
    opra_url: str = Field(..., alias="OPRA_URL")
    clerk__name: str = Field(..., alias="Clerk_Name")
    clerk__email: str = Field(..., alias="Clerk_Email")
    d_clerk__name: str = Field(..., alias="DClerk_Name")
    d_clerk__email: str = Field(..., alias="DClerk_Email")
    clerk__phone: str = Field(..., alias="Clerk_Phone")
    d_clerk__phone: Any = Field(..., alias="DClerk_Phone")
    clerk__fax: str = Field(..., alias="Clerk_Fax")
    assessor__name: str = Field(..., alias="Assessor_Name")
    assessor__email: str = Field(..., alias="Assessor_Email")
    assessor__phone: str = Field(..., alias="Assessor_Phone")
    assessor__website: str = Field(..., alias="Assessor_Website")
    eng__name: str = Field(..., alias="ENG_Name")
    eng_phone: str = Field(..., alias="ENG_phone")
    eng__email: str = Field(..., alias="ENG_Email")
    eng__website: str = Field(..., alias="ENG_Website")


class VoterRegistrationItem(BaseModel):
    display_id: str = Field(..., alias="displayId")
    leg_id: str
    party: str
    status: str
    last: str
    first: str
    middle: str
    suffix: str
    dob: str
    reg_date: str
    location: str
    street_num: str
    street_pre: str
    street_post: str
    street_base: str
    street_suff: str
    street_name: str
    apt_unit: str
    city: str
    zip: str
    county: str
    municipality: str
    ward: str
    district: str
    congressional: str
    legislative: str
    freeholder: str
    school: str
    fire: str


class NearbyProperty(BaseModel):
    property__location: str = Field(..., alias="Property_Location")
    gis_pin: str = Field(..., alias="GIS_PIN")


class NearbyProperties(BaseModel):
    nearby_properties: Optional[List[NearbyProperty]] = Field(
        None, alias="nearbyProperties"
    )


class PropertyTaxMap(BaseModel):
    id: int
    mun: str
    page: str
    img_pnt1_x: float
    img_pnt1_y: float
    img_pnt2_x: float
    img_pnt2_y: float
    img_pnt3_x: float
    img_pnt3_y: float
    geo_pnt1_x: float
    geo_pnt1_y: float
    geo_pnt2_x: float
    geo_pnt2_y: float
    geo_pnt3_x: float
    geo_pnt3_y: float
    top_left_x: float
    top_left_y: float
    top_right_x: float
    top_right_y: float
    bottom_left_x: float
    bottom_left_y: float
    bottom_right_x: float
    bottom_right_y: float
    worker: str
    status: str
    year: str
    gis_pin: str


class PropertyTaxMaps(BaseModel):
    property_tax_maps: Optional[List[PropertyTaxMap]] = Field(
        None, alias="propertyTaxMaps"
    )


class PropertyForeclosure(BaseModel):
    transaction_id: int = Field(..., alias="TransactionID")
    attom_id: int = Field(..., alias="AttomID")
    record_type: str = Field(..., alias="RecordType")
    situs_state_code: str = Field(..., alias="SitusStateCode")
    situs_county: str = Field(..., alias="SitusCounty")
    property_jurisdiction_name: str = Field(..., alias="PropertyJurisdictionName")
    situs_state_county_fips: str = Field(..., alias="SitusStateCountyFIPS")
    parcel_number_formatted: str = Field(..., alias="ParcelNumberFormatted")
    property_address_full: str = Field(..., alias="PropertyAddressFull")
    property_address_house_number: str = Field(..., alias="PropertyAddressHouseNumber")
    property_address_street_direction: Any = Field(
        ..., alias="PropertyAddressStreetDirection"
    )
    property_address_street_name: str = Field(..., alias="PropertyAddressStreetName")
    property_address_street_suffix: str = Field(
        ..., alias="PropertyAddressStreetSuffix"
    )
    property_address_street_post_direction: Any = Field(
        ..., alias="PropertyAddressStreetPostDirection"
    )
    property_address_unit_prefix: Any = Field(..., alias="PropertyAddressUnitPrefix")
    property_address_unit_value: Any = Field(..., alias="PropertyAddressUnitValue")
    property_address_city: str = Field(..., alias="PropertyAddressCity")
    property_address_state: str = Field(..., alias="PropertyAddressState")
    property_address_zip: str = Field(..., alias="PropertyAddressZIP")
    property_address_zip4: str = Field(..., alias="PropertyAddressZIP4")
    property_address_crrt: str = Field(..., alias="PropertyAddressCRRT")
    property_address_info_privacy: Any = Field(..., alias="PropertyAddressInfoPrivacy")
    property_latitude: float = Field(..., alias="PropertyLatitude")
    property_longitude: float = Field(..., alias="PropertyLongitude")
    geo_quality: str = Field(..., alias="GeoQuality")
    zoned_code_local: Any = Field(..., alias="ZonedCodeLocal")
    property_use_muni: str = Field(..., alias="PropertyUseMuni")
    property_use_group: str = Field(..., alias="PropertyUseGroup")
    property_use_standardized: str = Field(..., alias="PropertyUseStandardized")
    bath_count: int = Field(..., alias="BathCount")
    bedrooms_count: int = Field(..., alias="BedroomsCount")
    area_building: int = Field(..., alias="AreaBuilding")
    area_building_definition_code: str = Field(..., alias="AreaBuildingDefinitionCode")
    area_lot_sf: int = Field(..., alias="AreaLotSF")
    area_lot_acres: float = Field(..., alias="AreaLotAcres")
    year_built: int = Field(..., alias="YearBuilt")
    year_built_effective: Any = Field(..., alias="YearBuiltEffective")
    original_loan_recording_date: Optional[str] = Field(
        ..., alias="OriginalLoanRecordingDate"
    )
    original_loan_instrument_number: Optional[str] = Field(
        ..., alias="OriginalLoanInstrumentNumber"
    )
    original_loan_book_page: Any = Field(..., alias="OriginalLoanBookPage")
    borrower_name_owner: str = Field(..., alias="BorrowerNameOwner")
    original_loan_loan_number: Any = Field(..., alias="OriginalLoanLoanNumber")
    original_loan_amount: int = Field(..., alias="OriginalLoanAmount")
    original_loan_interest_rate: Any = Field(..., alias="OriginalLoanInterestRate")
    loan_maturity_date: Any = Field(..., alias="LoanMaturityDate")
    lender_name_full_standardized: str = Field(..., alias="LenderNameFullStandardized")
    lender_address: Any = Field(..., alias="LenderAddress")
    lender_address_house_number: Any = Field(..., alias="LenderAddressHouseNumber")
    lender_address_street_direction: Any = Field(
        ..., alias="LenderAddressStreetDirection"
    )
    lender_address_street_name: Any = Field(..., alias="LenderAddressStreetName")
    lender_address_street_suffix: Any = Field(..., alias="LenderAddressStreetSuffix")
    lender_address_street_post_direction: Any = Field(
        ..., alias="LenderAddressStreetPostDirection"
    )
    lender_address_unit_value: Any = Field(..., alias="LenderAddressUnitValue")
    lender_address_city: Any = Field(..., alias="LenderAddressCity")
    lender_address_state: Any = Field(..., alias="LenderAddressState")
    lender_address_zip: Any = Field(..., alias="LenderAddressZIP")
    lender_phone: Any = Field(..., alias="LenderPhone")
    servicer_name: Any = Field(..., alias="ServicerName")
    servicer_address: Optional[str] = Field(..., alias="ServicerAddress")
    servicer_city: Any = Field(..., alias="ServicerCity")
    servicer_state: Any = Field(..., alias="ServicerState")
    servicer_zip: Any = Field(..., alias="ServicerZip")
    servicer_phone: Any = Field(..., alias="ServicerPhone")
    trustee_name: Optional[str] = Field(..., alias="TrusteeName")
    trustee_address: Optional[str] = Field(..., alias="TrusteeAddress")
    trustee_address_house_number: Any = Field(..., alias="TrusteeAddressHouseNumber")
    trustee_address_street_direction: Any = Field(
        ..., alias="TrusteeAddressStreetDirection"
    )
    trustee_address_street_name: Any = Field(..., alias="TrusteeAddressStreetName")
    trustee_address_street_suffix: Any = Field(..., alias="TrusteeAddressStreetSuffix")
    trustee_address_street_post_direction: Any = Field(
        ..., alias="TrusteeAddressStreetPostDirection"
    )
    trustee_address_unit_value: Any = Field(..., alias="TrusteeAddressUnitValue")
    trustee_address_city: Optional[str] = Field(..., alias="TrusteeAddressCity")
    trustee_address_state: Optional[str] = Field(..., alias="TrusteeAddressState")
    trustee_address_zip: Optional[str] = Field(..., alias="TrusteeAddressZIP")
    trustee_phone: Optional[str] = Field(..., alias="TrusteePhone")
    foreclosure_instrument_date: Any = Field(..., alias="ForeclosureInstrumentDate")
    foreclosure_recording_date: str = Field(..., alias="ForeclosureRecordingDate")
    foreclosure_instrument_number: Optional[str] = Field(
        ..., alias="ForeclosureInstrumentNumber"
    )
    foreclosure_book_page: Any = Field(..., alias="ForeclosureBookPage")
    case_number: Any = Field(..., alias="CaseNumber")
    trustee_reference_number: Any = Field(..., alias="TrusteeReferenceNumber")
    payment: Any = Field(..., alias="Payment")
    default_amount: int = Field(..., alias="DefaultAmount")
    penalty_interest: Any = Field(..., alias="PenaltyInterest")
    loan_balance: Any = Field(..., alias="LoanBalance")
    judgment_date: Any = Field(..., alias="JudgmentDate")
    judgment_amount: float = Field(..., alias="JudgmentAmount")
    courthouse: Any = Field(..., alias="Courthouse")
    auction_address: Optional[str] = Field(..., alias="AuctionAddress")
    auction_house_number: Any = Field(..., alias="AuctionHouseNumber")
    auction_direction: Any = Field(..., alias="AuctionDirection")
    auction_street_name: Any = Field(..., alias="AuctionStreetName")
    auction_suffix: Any = Field(..., alias="AuctionSuffix")
    auction_post_direction: Any = Field(..., alias="AuctionPostDirection")
    auction_unit: Any = Field(..., alias="AuctionUnit")
    auction_city: Optional[str] = Field(..., alias="AuctionCity")
    auction_date: Optional[str] = Field(..., alias="AuctionDate")
    auction_time: Optional[str] = Field(..., alias="AuctionTime")
    recorded_auction_opening_bid: Optional[int] = Field(
        ..., alias="RecordedAuctionOpeningBid"
    )
    estimated_value: Any = Field(..., alias="EstimatedValue")
    create_date: str = Field(..., alias="CreateDate")
    record_last_updated: str = Field(..., alias="RecordLastUpdated")
    publication_date: str = Field(..., alias="PublicationDate")


class PropertyForeclosures(BaseModel):
    property_foreclosures: Optional[List[PropertyForeclosure]] = Field(
        None, alias="propertyForeclosures"
    )


class PropertyMortgage(BaseModel):
    id: int
    gis_pin: str = Field(..., alias="GIS_PIN")
    transaction_id: str
    property_id: str
    fips_code: str
    assessors_parcel_number: str
    property_full_street_address: str
    property_city_name: str
    property_state: str
    property_zip_code: str
    property_zipplus4: str
    property_unit_type: str
    property_unit_number: str
    property_house_number: str
    property_street_direction_left: str
    property_street_name: str
    property_street_suffix: str
    property_street_direction_right: str
    property_address_carrier_route: str
    record_type: str
    recording_date: str
    recorders_book_number: str
    recorders_page_number: str
    recorders_document_number: str
    borrower_fname_mname_1: str
    borrower_lname_or_corpname_1: str
    borrower_id_code_1: str
    borrower_fname_mname_2: str
    borrower_lname_or_corpname_2: str
    borrower_id_code_2: str
    borrower_vesting_code: str
    legal_lot_number: str
    legal_block: str
    legal_section: str
    legal_district: str
    legal_land_lot: str
    legal_unit: str
    legal_city_township_municipality: str
    legal_subdivision_name: str
    legal_phase_number: str
    legal_tract_number: str
    legal_brief_description: str
    legal_sectiontownship_rangemeridian: str
    lender_name_beneficiary: str
    lender_type: str
    loan_amount: str
    loan_type: str
    type_financing: str
    interest_rate: str
    due_date: str
    adjustable_rate_rider: str
    adjustable_rate_index: str
    change_index: str
    rate_change_frequency: str
    interest_rate_not_greater_than: str
    interest_rate_not_less_than: str
    maximum_interest_rate: str
    interest_only_period: str
    fixedstep_conversion_rate_rider: str
    first_change_date_year_conversion_rider: str
    first_change_date_month_day_conversion_rider: str
    prepayment_rider: str
    prepayment_term_penalty_rider: str
    buyer_mail_full_street_address: str
    borrower_mail_unit_number: str
    borrower_mail_city: str
    borrower_mail_state: str
    borrower_mail_zip_code: str
    borrower_mail_zipplus4: str
    original_date_of_contract: str
    title_company_name: str
    lender_dba_name: str
    lender_mail_full_street_address: str
    lender_mail_unit: str
    lender_mail_city: str
    lender_mail_state: str
    lender_mail_zip_code: str
    lender_mail_zipplus4: str
    loan_term_months: str
    loan_term_years: str
    assessors_land_use: str
    residential_indicator: str
    construction_loan: str
    cash_purchase: str
    standalone_refi: str
    equity_credit_line: str
    purchase_money_mortgage: str
    unique_link_id: str
    type_financing_description: str
    loan_type_description: str
    borrower_id_code_1_description: str
    borrower_id_code_2_description: str
    record_type_description: str
    borrower_vesting_code_description: str
    lender_type_description: str


class PropertyMortgages(BaseModel):
    property_mortgages: Optional[List[PropertyMortgage]] = Field(
        None, alias="propertyMortgages"
    )


class PropertyTax(BaseModel):
    amount: Optional[float]
    year: int
    land: int
    improved: int
    total: int
    match_method: str = Field(..., alias="matchMethod")
    difference_currency: int = Field(..., alias="differenceCurrency")
    difference_percent: Optional[float] = Field(..., alias="differencePercent")
    amount_diff: Optional[float] = Field(..., alias="amountDiff")
    amount_diff_currency: float = Field(..., alias="amountDiffCurrency")


class PropertyTaxes(BaseModel):
    property_taxes: Optional[List[PropertyTax]] = Field(None, alias="propertyTaxes")


class PropertyHistoryItem(BaseModel):
    gis_pin: str = Field(..., alias="GIS_PIN")
    prior_gis_pin: Any = Field(..., alias="PRIOR_GIS_PIN")
    old__property_id: Any = Field(..., alias="Old_Property_ID")
    data__year: int = Field(..., alias="Data_Year")
    municipality: str = Field(..., alias="Municipality")
    block: str = Field(..., alias="Block")
    lot: str = Field(..., alias="Lot")
    qual: Any = Field(..., alias="Qual")
    property__location: str = Field(..., alias="Property_Location")
    property__class: str = Field(..., alias="Property_Class")
    owners__name: str = Field(..., alias="Owners_Name")
    owners__mailing__address: str = Field(..., alias="Owners_Mailing_Address")
    city__state__zip: str = Field(..., alias="City_State_Zip")
    yr__built: Optional[int] = Field(..., alias="Yr_Built")
    building__class: Optional[int] = Field(..., alias="Building_Class")
    updated: str = Field(..., alias="Updated")
    zone: Any = Field(..., alias="Zone")
    bank__code: str = Field(..., alias="Bank_Code")
    sp__tax__cd_1: Any = Field(..., alias="Sp_Tax_Cd_1")
    sp__tax__cd_2: Any = Field(..., alias="Sp_Tax_Cd_2")
    sp__tax__cd_3: Any = Field(..., alias="Sp_Tax_Cd_3")
    sp__tax__cd_4: Any = Field(..., alias="Sp_Tax_Cd_4")
    map__page: Optional[str] = Field(..., alias="Map_Page")
    additional__lots: Any = Field(..., alias="Additional_Lots")
    land__desc: str = Field(..., alias="Land_Desc")
    acreage: float = Field(..., alias="Acreage")
    building__desc: Optional[str] = Field(..., alias="Building_Desc")
    epl__own: str = Field(..., alias="EPL_Own")
    epl__use: str = Field(..., alias="EPL_Use")
    epl__desc: str = Field(..., alias="EPL_Desc")
    epl__init: Optional[str] = Field(..., alias="EPL_Init")
    epl__further: Optional[str] = Field(..., alias="EPL_Further")
    epl__statute: Any = Field(..., alias="EPL_Statute")
    epl__facility__name: Any = Field(..., alias="EPL_Facility_Name")
    sale__date: str = Field(..., alias="Sale_Date")
    deed__book: str = Field(..., alias="Deed_Book")
    deed__page: str = Field(..., alias="Deed_Page")
    sale__price: int = Field(..., alias="Sale_Price")
    nu__code: Optional[str] = Field(..., alias="NU_Code")
    land__assmnt_1: str = Field(..., alias="Land_Assmnt_1")
    building__assmnt_1: str = Field(..., alias="Building_Assmnt_1")
    total__assmnt_1: int = Field(..., alias="Total_Assmnt_1")
    total__assmnt_2: Optional[int] = Field(..., alias="Total_Assmnt_2")
    record__id: str = Field(..., alias="Record_Id")
    transaction__update__no: str = Field(..., alias="Transaction_Update_No")
    addition__lots_2: Any = Field(..., alias="Addition_Lots_2")
    zip__code: str = Field(..., alias="Zip_Code")
    street__address: str = Field(..., alias="Street_Address")
    city__state: str = Field(..., alias="City_State")
    number__of__owners: Any = Field(..., alias="Number_Of_Owners")
    deduction__amount: Any = Field(..., alias="Deduction_Amount")
    sales__price__code: Optional[str] = Field(..., alias="Sales_Price_Code")
    sale__assessment: Optional[str] = Field(..., alias="Sale_Assessment")
    sale_sr1_a__un__code: Optional[str] = Field(..., alias="Sale_SR1A_Un_Code")
    no__of__dwellings: Optional[str] = Field(..., alias="No_Of_Dwellings")
    no__of__commercial__dw: Any = Field(..., alias="No_Of_Commercial_Dw")
    multiple__occupancy: Any = Field(..., alias="Multiple_Occupancy")
    percent__owned__code: Any = Field(..., alias="Percent_Owned_Code")
    rebate__code: Any = Field(..., alias="Rebate_Code")
    delinquent__code: Any = Field(..., alias="Delinquent_Code")
    exemption__code_1: Any = Field(..., alias="Exemption_Code_1")
    exemption_amt_1: Any = Field(..., alias="Exemption_AMT_1")
    exemption__code_2: Any = Field(..., alias="Exemption_Code_2")
    exemption_amt_2: Any = Field(..., alias="Exemption_AMT_2")
    exemption__code_3: Any = Field(..., alias="Exemption_Code_3")
    exemption_amt_3: Any = Field(..., alias="Exemption_AMT_3")
    exemption__code_4: Any = Field(..., alias="Exemption_Code_4")
    exemption_amt_4: Any = Field(..., alias="Exemption_AMT_4")
    senior__citizens_cnt: Any = Field(..., alias="Senior_Citizens_CNT")
    veterans_cnt: Any = Field(..., alias="Veterans_CNT")
    widows_cnt: Any = Field(..., alias="Widows_CNT")
    surv__spouse_cnt: Any = Field(..., alias="Surv_Spouse_CNT")
    disabled_cnt: Any = Field(..., alias="Disabled_CNT")
    user__field_1: Any = Field(..., alias="User_Field_1")
    user__field_2: Any = Field(..., alias="User_Field_2")
    property__use__code: Any = Field(..., alias="Property_Use_Code")
    property__flags: Any = Field(..., alias="Property_Flags")
    rebate__response_flg: Any = Field(..., alias="Rebate_Response_FLG")
    rebate__base__year: Optional[str] = Field(..., alias="Rebate_Base_Year")
    rebate__base__year__tax: Optional[str] = Field(..., alias="Rebate_Base_Year_Tax")
    rebate__base__year__net__val: Optional[str] = Field(
        ..., alias="Rebate_Base_Year_Net_Val"
    )
    last__year__tax: str = Field(..., alias="Last_Year_Tax")
    match_method: str = Field(..., alias="matchMethod")


class PropertyHistory(BaseModel):
    property_history: Optional[List[PropertyHistoryItem]] = Field(
        None, alias="propertyHistory"
    )


class LatLng(BaseModel):
    lat: float
    lng: float


class Target(BaseModel):
    property_code: str = Field(..., alias="propertyCode")
    lat_lng: LatLng = Field(..., alias="latLng")
    municipality: Any
    zip: Any
