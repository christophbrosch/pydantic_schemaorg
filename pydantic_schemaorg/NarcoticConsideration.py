from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class NarcoticConsideration(AdultOrientedEnumeration):
    """Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html),"
     "for example marijuana or heroin.

    See: https://schema.org/NarcoticConsideration
    Model depth: 5
    """

    type_: str = Field(default="NarcoticConsideration", alias="@type", Literal=True)
