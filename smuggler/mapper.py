from . import models

_LIST_MAP = {
    "primary_data.nearby_properties": models.NearbyProperty,
    "primary_data.property_deeds": models.PropertyDeed,
    "primary_data.property_foreclosures": models.PropertyForeclosure,
    "primary_data.property_history": models.PropertyHistory,
    "primary_data.property_listings": models.PropertyListing,
    "primary_data.property_mortgages": models.PropertyMortgage,
    "primary_data.voter_registration": models.VoterRegistrationItem,
    "primary_data.property_taxes": models.PropertyTax,
}

_OBJECT_MAP = {
    "primary_data.property_information": models.PropertyInformation,
    "primary_data.municipality_data": models.MunicipalityData,
}
