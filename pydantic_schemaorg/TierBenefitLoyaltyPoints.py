from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.TierBenefitEnumeration import TierBenefitEnumeration


class TierBenefitLoyaltyPoints(TierBenefitEnumeration):
    """Benefit of the tier is earning of loyalty points.

    See: https://schema.org/TierBenefitLoyaltyPoints
    Model depth: 5
    """

    type_: str = Field(default="TierBenefitLoyaltyPoints", alias="@type", Literal=True)
