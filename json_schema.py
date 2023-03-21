from typing import Optional

from pydantic import BaseModel, Field


class MunicipalityData(BaseModel):
    municipality: Optional[str] = Field(None, alias="Municipality")
    county: Optional[str] = Field(None, alias="County")
    name: Optional[str] = Field(None, alias="Name")
    codebook_homepage: Optional[str] = Field(None, alias="Codebook_Homepage")
    codebook_zoning: Optional[str] = Field(None, alias="Codebook_Zoning")
    website: Optional[str] = Field(None, alias="Website")
    clerk_website: Optional[str] = Field(None, alias="Clerk_Website")
    opra_url: Optional[str] = Field(None, alias="OPRA_URL")
    clerk_name: Optional[str] = Field(None, alias="Clerk_Name")
    clerk_email: Optional[str] = Field(None, alias="Clerk_Email")
    d_clerk_name: Optional[str] = Field(None, alias="DClerk_Name")
    d_clerk_email: Optional[str] = Field(None, alias="DClerk_Email")
    clerk_phone: Optional[str] = Field(None, alias="Clerk_Phone")
    d_clerk_phone: Optional[str] = Field(None, alias="DClerk_Phone")
    clerk_fax: Optional[str] = Field(None, alias="Clerk_Fax")
    assessor_name: Optional[str] = Field(None, alias="Assessor_Name")
    assessor_email: Optional[str] = Field(None, alias="Assessor_Email")
    assessor_phone: Optional[str] = Field(None, alias="Assessor_Phone")
    assessor_website: Optional[str] = Field(None, alias="Assessor_Website")
    eng_name: Optional[str] = Field(None, alias="ENG_Name")
    eng_phone: Optional[str] = Field(None, alias="ENG_phone")
    eng_email: Optional[str] = Field(None, alias="ENG_Email")
    eng_website: Optional[str] = Field(None, alias="ENG_Website")
