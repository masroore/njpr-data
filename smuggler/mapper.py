from pydantic import BaseModel
import jmespath

from . import models

_JSON_MAP = {
    "main": {
        "list": {
            "primary_data.nearby_properties": models.NearbyProperty,
            "primary_data.property_deeds": models.PropertyDeed,
            "primary_data.property_foreclosures": models.PropertyForeclosure,
            "primary_data.property_history": models.PropertyHistory,
            # "primary_data.property_listings": models.PropertyListing,
            "primary_data.property_mortgages": models.PropertyMortgage,
            "primary_data.voter_registration": models.VoterRegistrationItem,
            "primary_data.property_taxes": models.PropertyTax,
        },
        "object": {
            "primary_data.property_information": models.PropertyInformation,
            "primary_data.municipality_data": models.MunicipalityData,
        },
    },
    "schools": {
        "list": {
            "*": models.School,
        }
    },
    "walkscore": {
        "object": {
            "*": models.Walkscore,
        }
    },
    "additional-data": {
        "object": {
            "property_census_data": models.PropertyCensusData,
            "property_utilities": models.PropertyUtilities,
        },
        "list": {
            "potentially_related_properties": models.PotentiallyRelatedProperty,
            "property_broadband_coverage": models.PropertyBroadbandCoverage,
        },
    },
    "demographics": {
        "object": {
            "*": models.Demographics,
        }
    },
    "contaminated-site": {
        "list": {
            "*": models.ContaminatedSite,
        }
    },
}


def map(data: dict, section: str) -> list[BaseModel]:
    mapped_items = []
    if section not in _JSON_MAP:
        return mapped_items

    section_map = _JSON_MAP[section]
    if "object" in section_map:
        for selector, model in section_map["object"].items():
            if selector == "*":
                found_obj = data
            else:
                found_obj = jmespath.search(selector, data)

            if found_obj:
                mapped_items.append(model(**found_obj))

    if "list" in section_map:
        for selector, model in section_map["list"].items():
            if selector == "*":
                found_list = data
            else:
                found_list = jmespath.search(selector, data)

            for item in found_list:
                mapped_items.append(model(**item))

    return mapped_items
