from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PaymentMethodType import PaymentMethodType


class PhoneCarrierPayment(PaymentMethodType):
    """Payment by billing via the phone carrier.

    See: https://schema.org/PhoneCarrierPayment
    Model depth: 5
    """

    type_: str = Field(default="PhoneCarrierPayment", alias="@type", Literal=True)
