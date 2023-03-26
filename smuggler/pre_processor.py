import re
from typing import Pattern, Any
from functools import lru_cache
import jmespath
import slugify

from .models import StatisticTypes

_UNDER_SCORE_1: Pattern[str] = re.compile(r"([^_])([A-Z][a-z]+)")
_UNDER_SCORE_2: Pattern[str] = re.compile("([a-z0-9])([A-Z])")
_disallowed_chars = ["-", "(", ")"]


def _to_snake(txt: str) -> str:
    subbed = _UNDER_SCORE_1.sub(r"\1_\2", txt)
    return _UNDER_SCORE_2.sub(r"\1_\2", subbed).lower()


@lru_cache()
def sanitize_attribute_name(txt: str) -> str:
    # sanitize characters like ()-
    for c in _disallowed_chars:
        txt = txt.replace(c, "_")
    txt = txt.rstrip("_")
    return _to_snake(txt)


def canonicalize_json_data(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    result: dict[Any, Any] = {}
    for k, v in data.items():
        if isinstance(k, str):
            key = sanitize_attribute_name(k)
        else:
            key = k

        if isinstance(v, str):
            if v:
                v = v.strip()
                if len(v) == 0:
                    v = None
            else:
                v = None

        if isinstance(v, dict):
            result[key] = canonicalize_json_data(v, sort_keys)
        elif isinstance(v, list):
            result[key] = [
                canonicalize_json_data(x, sort_keys) if isinstance(x, dict) else x for x in v
            ]
        elif isinstance(v, tuple):
            result[key] = tuple(
                canonicalize_json_data(x, sort_keys) if isinstance(x, dict) else x for x in v
            )
        else:
            result[key] = v  # data[k]

    return dict(sorted(result.items())) if sort_keys else result


def sort_dict(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    return dict(sorted(data.items())) if sort_keys else data


def property_information_reshape_geolocations(src_data: dict[Any, Any]) -> dict[Any, Any]:
    if "primary_data" not in src_data:
        return src_data

    property_info = src_data['primary_data']['property_information']
    j_path = """primary_data.property_information.{
        %(prefix)slatitude: %(property)s.lat,
        %(prefix)slongitude: %(property)s.lng
    }
    """

    flatten = {
        "lat_lng": "property_",
        "parcel_centroid": "parcel_centroid_",
        "rooftop": "rooftop_",
    }

    for prop, prefix in flatten.items():
        lat_lng = jmespath.search(
            j_path % dict(prefix=prefix, property=prop), src_data
        )
        del property_info[prop]
        property_info.update(lat_lng)

    return src_data


def rename_attributes(src_data: dict[Any, Any], prefix: str) -> dict[Any, Any]:
    search_list = ['id', ]
    for attr in search_list:
        if attr in src_data:
            val = src_data[attr]
            del src_data[attr]
            # src_data[prefix + attr] = val
            src_data.update({f'{prefix}{attr}': val})

    return src_data


def property_information_purge_redundant_attributes(src_data: dict[Any, Any]) -> dict[Any, Any]:
    search_list = ['id', ]
    return src_data


def reshape_property_information(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    if "primary_data" not in data:
        return data

    data = property_information_reshape_geolocations(data)
    return data


def reshape_property_deeds(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    if "primary_data" not in data:
        return data
    return _rename_list_attribs(data, "property_deeds", 'display_', sort_keys)


def reshape_tax_rates(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    if "primary_data" not in data:
        return data
    # rename to municipality_tax_rates
    return sort_dict(data, sort_keys)


def split_label(s: str) -> tuple[int, str]:
    parts = s.split(" ", 1)
    return int(parts[0]), slugify.slugify(parts[1], separator="_")


def reshape_municipality_data(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    if "primary_data" not in data:
        return data
    muni = jmespath.search("primary_data.municipality_data", data)
    # muni = data["primary_data"]["municipality_data"]
    rename_attributes(muni, 'municipality_')

    rates_data = jmespath.search("primary_data.tax_rates", data)

    tax_rates = {}
    for k, v in rates_data.items():
        if k.startswith("20"):
            (year, field) = split_label(k)
            row = tax_rates.get(year, {"year": year})

            if v:
                v = v.replace("%", "")
                row.update({field: float(v)})
            else:
                row.update({field: None})

            tax_rates[year] = row

    tax_rates = [v for k, v in sorted(tax_rates.items())]
    del data["primary_data"]["tax_rates"]

    muni.update({
        "tax_rates": tax_rates
    })

    return sort_dict(data, sort_keys)


def purge_redundant_attribs(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    purge_list = ['municipality_documents', 'rating_description', ]
    for elem in purge_list:
        if "primary_data" in data and elem in data["primary_data"]:
            del data["primary_data"][elem]
        elif elem in data:
            del data[elem]

    return data


def _rename_list_attribs(data: dict[Any, Any], elem_name: str, prefix: str, sort_keys: bool) -> dict[Any, Any]:
    items = jmespath.search(f'primary_data.{elem_name}', data)
    result = []
    for item in items:
        item = rename_attributes(item, prefix)
        result.append(sort_dict(item, sort_keys))

    data["primary_data"][elem_name] = result
    return sort_dict(data, sort_keys)


def reshape_property_tax_maps(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    if "primary_data" not in data:
        return data
    return _rename_list_attribs(data, "property_tax_maps", 'display_', sort_keys)


def reshape_property_mortgages(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    if "primary_data" not in data:
        return data
    return _rename_list_attribs(data, "property_mortgages", 'display_', sort_keys)


def reshape_demographics(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    if 'quick_facts' not in data and 'sex' not in data:
        return data
    qfacts = data['quick_facts']
    data.update(qfacts)
    del data['quick_facts']

    demographic_stats = {
        StatisticTypes.AGE.name: StatisticTypes.AGE,
        StatisticTypes.SEX.name: StatisticTypes.SEX,
        StatisticTypes.INCOME.name: StatisticTypes.INCOME,
        StatisticTypes.EDUCATION.name: StatisticTypes.EDUCATION,
        StatisticTypes.HOUSEHOLD_SIZE.name: StatisticTypes.HOUSEHOLD_SIZE,
        StatisticTypes.RESIDENCE.name: StatisticTypes.RESIDENCE,
    }
    for name, typ in demographic_stats.items():
        for item in data[name.lower()]:
            item.update({'stat_type': typ})
    return data


_RESHAPERS = {
    "*": purge_redundant_attribs,
    "property_information": reshape_property_information,
    "tax_rates": reshape_tax_rates,
    "municipality_data": reshape_municipality_data,
    "property_deeds": reshape_property_deeds,
    "property_tax_maps": reshape_property_tax_maps,
    "property_mortgages": reshape_property_mortgages,
    "demographics": reshape_demographics,
}


def reshape_json_data(data: dict[Any, Any], sort_keys: bool) -> dict[Any, Any]:
    for _, func in _RESHAPERS.items():
        data = func(data=data, sort_keys=sort_keys)

    return data
