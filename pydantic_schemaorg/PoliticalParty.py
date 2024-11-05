from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class PoliticalParty(Organization):
    """Organization: Political Party.

    See: https://schema.org/PoliticalParty
    Model depth: 3
    """

    type_: str = Field(default="PoliticalParty", alias="@type", Literal=True)
