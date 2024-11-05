from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PaymentMethodType import PaymentMethodType


class DirectDebit(PaymentMethodType):
    """Payment in advance by direct debit from the bank, equivalent to <code>http://purl.org/goodrelations/v1#DirectDebit</code>.

    See: https://schema.org/DirectDebit
    Model depth: 5
    """

    type_: str = Field(default="DirectDebit", alias="@type", Literal=True)
