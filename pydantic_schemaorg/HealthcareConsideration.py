from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class HealthcareConsideration(AdultOrientedEnumeration):
    """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

    See: https://schema.org/HealthcareConsideration
    Model depth: 5
    """

    type_: str = Field(default="HealthcareConsideration", alias="@type", Literal=True)
