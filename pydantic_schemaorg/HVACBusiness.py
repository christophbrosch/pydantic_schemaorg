from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """A business that provides Heating, Ventilation and Air Conditioning services.

    See: https://schema.org/HVACBusiness
    Model depth: 5
    """

    type_: str = Field(default="HVACBusiness", alias="@type", Literal=True)
