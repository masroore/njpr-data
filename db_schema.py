from typing import Optional

from pydantic import Field
from pydbantic import DataBaseModel, PrimaryKey
from sqlalchemy import Integer


class MunicipalityData(DataBaseModel):
    id: int | None = PrimaryKey(sqlalchemy_type=Integer, default=None)
    municipality: Optional[str] = Field(None)
    county: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    codebook_homepage: Optional[str] = Field(None)
    codebook_zoning: Optional[str] = Field(None)
    website: Optional[str] = Field(None)
    clerk_website: Optional[str] = Field(None)
    opra_url: Optional[str] = Field(None)
    clerk_name: Optional[str] = Field(None)
    clerk_email: Optional[str] = Field(None)
    d_clerk_name: Optional[str] = Field(None)
    d_clerk_email: Optional[str] = Field(None)
    clerk_phone: Optional[str] = Field(None)
    d_clerk_phone: Optional[str] = Field(None)
    clerk_fax: Optional[str] = Field(None)
    assessor_name: Optional[str] = Field(None)
    assessor_email: Optional[str] = Field(None)
    assessor_phone: Optional[str] = Field(None)
    assessor_website: Optional[str] = Field(None)
    eng_name: Optional[str] = Field(None)
    eng_phone: Optional[str] = Field(None)
    eng_email: Optional[str] = Field(None)
    eng_website: Optional[str] = Field(None)
