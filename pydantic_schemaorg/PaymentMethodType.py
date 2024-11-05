from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PaymentMethodType(Enumeration):
    """The type of payment method, only for generic payment types, specific forms of payments,"
     "like card payment should be expressed using subclasses of PaymentMethod.

    See: https://schema.org/PaymentMethodType
    Model depth: 4
    """

    type_: str = Field(default="PaymentMethodType", alias="@type", Literal=True)
