from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class ReducedRelevanceForChildrenConsideration(AdultOrientedEnumeration):
    """A general code for cases where relevance to children is reduced, e.g. adult education,"
     "mortgages, retirement-related products, etc.

    See: https://schema.org/ReducedRelevanceForChildrenConsideration
    Model depth: 5
    """

    type_: str = Field(
        default="ReducedRelevanceForChildrenConsideration", alias="@type", Literal=True
    )
