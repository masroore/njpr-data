import glob
import os
import asyncio
import jmespath
import orjson as json
import slugify
from pydbantic import Database
import db_schema, json_schema

from generated import schema, extra

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


def split_label(s: str) -> tuple[int, str]:
    parts = s.split(" ", 1)
    return int(parts[0]), slugify.slugify(parts[1], separator="_")


async def pydantize(f):
    print(os.path.basename(f))
    with open(f, "r") as fp:
        data = json.loads(fp.read())

    j = json_schema.MunicipalityData(**data["primaryData"]["municipalityData"])
    d = db_schema.MunicipalityData(**j.dict())

    exit(0)

    rates_data = jmespath.search("primaryData.taxRates", data)
    # print(rates_data)
    # dict_to_snake(rates_data)
    taxRates = extra.TaxRates(**rates_data)

    tax_rows = {}
    for k, v in rates_data.items():
        if k.startswith("20"):
            (year, field) = split_label(k)
            row = tax_rows.get(year, {"year": year})

            if v:
                v = v.replace("%", "")
                row.update({field: float(v)})
            else:
                row.update({field: None})

            tax_rows[year] = row

    for tr in tax_rows.values():
        rate = extra.MunicipalityTaxRate(**tr)
        taxRates.tax_rates.append(rate)

    del data["primaryData"]["taxRates"]
    """
    data['primaryData']['taxRates'] = taxRates.dict()
    print(taxRates)
    print(data['primaryData']['taxRates'])
    exit(0)
    """

    property = schema.Model(**data)
    property.primary_data.tax_rates = taxRates

    await property.primary_data.municipality_data.insert()
    await property.primary_data.municipality_data.save()
    with open(os.path.abspath("./out/" + os.path.basename(f)), "wb") as fp:
        fp.write(json.dumps(property.dict(), option=json.OPT_INDENT_2))


async def run():
    db = await Database.create(
        "sqlite:///test.db",
        tables=[
            db_schema.MunicipalityData,
        ],
    )

    for f in glob.glob("./scrapes/*.json"):
        await pydantize(f)
        break


if __name__ == "__main__":
    asyncio.run(main=run())
