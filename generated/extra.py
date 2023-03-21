from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class TaxRate(BaseModel):
    year: int
    tax_rate: Optional[float] = Field(None)
    ratio: Optional[float] = Field(None)


class TaxRates(BaseModel):
    municipality: str = Field(..., alias="MUNICIPALITY")
    county: str = Field(..., alias="COUNTY")
    town: str = Field(..., alias="TOWN")
    tax_rates: list[TaxRate] = []
