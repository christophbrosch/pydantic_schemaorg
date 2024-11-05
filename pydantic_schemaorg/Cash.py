from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PaymentMethodType import PaymentMethodType


class Cash(PaymentMethodType):
    """Payment using cash, on premises, equivalent to <code>http://purl.org/goodrelations/v1#Cash</code>.

    See: https://schema.org/Cash
    Model depth: 5
    """

    type_: str = Field(default="Cash", alias="@type", Literal=True)
