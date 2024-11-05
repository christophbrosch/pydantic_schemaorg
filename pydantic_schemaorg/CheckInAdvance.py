from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PaymentMethodType import PaymentMethodType


class CheckInAdvance(PaymentMethodType):
    """Payment in advance by sending a check, equivalent to <code>http://purl.org/goodrelations/v1#CheckInAdvance</code>.

    See: https://schema.org/CheckInAdvance
    Model depth: 5
    """

    type_: str = Field(default="CheckInAdvance", alias="@type", Literal=True)
