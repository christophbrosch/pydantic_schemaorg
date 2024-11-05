from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class ListPrice(PriceTypeEnumeration):
    """Represents the list price of an offered product.

    See: https://schema.org/ListPrice
    Model depth: 5
    """

    type_: str = Field(default="ListPrice", alias="@type", Literal=True)
