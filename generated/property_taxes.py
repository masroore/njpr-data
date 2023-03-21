# generated by datamodel-codegen:
#   filename:  propertyTaxes.json
#   timestamp: 2023-03-21T08:04:23+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class PropertyTax(BaseModel):
    amount: Optional[float] = None
    year: Optional[int] = None
    land: Optional[int] = None
    improved: Optional[int] = None
    total: Optional[int] = None
    match_method: Optional[str] = Field(None, alias="matchMethod")
    difference_currency: Optional[int] = Field(None, alias="differenceCurrency")
    difference_percent: Optional[float] = Field(None, alias="differencePercent")
    amount_diff: Optional[float] = Field(None, alias="amountDiff")
    amount_diff_currency: Optional[float] = Field(None, alias="amountDiffCurrency")


class Model(BaseModel):
    property_taxes: Optional[list[PropertyTax]] = Field(None, alias="propertyTaxes")
