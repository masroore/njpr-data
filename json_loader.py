import os
from camel_converter import dict_to_snake, to_snake

import jmespath
import orjson as json
import slugify
import snakecase
from generated import schema, extra

src_dir = os.path.abspath("json")

with open(src_dir + "/main.json", "r") as fp:
    data = json.loads(fp.read())

"""
muni_data = jmespath.search('primaryData.municipalityData', data)
munic = municipality_data.MunicipalityData(**muni_data)

deeds_list = jmespath.search('primaryData.propertyDeeds', data)

deeds = property_deeds.PropertyDeeds()
for deed_data in deeds_list:
    deeds.property_deeds.append(property_deeds.PropertyDeed(**deed_data))

print(munic)
print(deeds)
"""


def split_label(s: str):
    parts = s.split(" ", 1)
    return int(parts[0]), slugify.slugify(parts[1], separator='_')

rates_data = jmespath.search("primaryData.taxRates", data)
dict_to_snake(rates_data)
tax_rates = extra.TaxRates(**rates_data)

tax_rows = {}
for k, v in rates_data.items():
    if k.startswith("20"):
        (year, field) = split_label(k)
        row = tax_rows.get(year, {"year": year})

        if v:
            v = v.replace('%', '')
            row.update({field: float(v)})
        else:
            row.update({field: None})

        tax_rows[year] = row

for tr in tax_rows.values():
    rate = extra.TaxRate(**tr)
    tax_rates.tax_rates.append(rate)

print(tax_rates)

property = schema.Model(**data)
with open("pydantinc.json", "wb") as fp:
    fp.write(json.dumps(property.dict(), option=json.OPT_INDENT_2))
