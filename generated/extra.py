from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field


class TaxRate(BaseModel):
    year: int = Field(...)
    tax_rate: Optional[str] = Field(None)
    ratio: Optional[str] = Field(None)


class TaxRates(BaseModel):
    municipality: str = Field(None, alias="MUNICIPALITY")
    county: str = Field(None, alias="COUNTY")
    town: str = Field(None, alias="TOWN")
    tax_rates: list[TaxRate] = []
