from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.TierBenefitEnumeration import TierBenefitEnumeration


class TierBenefitLoyaltyPrice(TierBenefitEnumeration):
    """Benefit of the tier is a members-only price.

    See: https://schema.org/TierBenefitLoyaltyPrice
    Model depth: 5
    """

    type_: str = Field(default="TierBenefitLoyaltyPrice", alias="@type", Literal=True)
