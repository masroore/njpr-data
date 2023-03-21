import os

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
    return (int(parts[0]), slugify.slugify(parts[1], separator='_'))


tax_rates = jmespath.search("primaryData.taxRates", data)
rates = extra.TaxRates(**tax_rates)
print(rates)

tax_rows = {}
for k, v in tax_rates.items():
    if k.startswith("20"):
        (year, field) = split_label(k)
        if year in tax_rows:
            row = tax_rows[year]
        else:
            row = {"year": year}

        print(year)
        print(field)
        print(v)
        print(row)
        print("\n")

        if v:
            v = v.replace('%', '')
            row.update({field: float(v)})
        else:
            row.update({field: None})

        tax_rows[year] = row
print(tax_rows)

for tr in tax_rows.values():
    rate = extra.TaxRate(**tr)
    rates.tax_rates.append(rate)

print(rates)

property = schema.Model(**data)
with open("pydantinc.json", "wb") as fp:
    fp.write(json.dumps(property.dict(), option=json.OPT_INDENT_2))
