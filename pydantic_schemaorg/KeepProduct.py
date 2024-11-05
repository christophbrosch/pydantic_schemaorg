from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class KeepProduct(ReturnMethodEnumeration):
    """Specifies that the consumer can keep the product, even when receiving a refund or store"
     "credit.

    See: https://schema.org/KeepProduct
    Model depth: 5
    """

    type_: str = Field(default="KeepProduct", alias="@type", Literal=True)
