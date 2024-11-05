from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct
from pydantic_schemaorg.PaymentMethod import PaymentMethod


class PaymentService(FinancialProduct, PaymentMethod):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization.

    See: https://schema.org/PaymentService
    Model depth: 4
    """

    type_: str = Field(default="PaymentService", alias="@type", Literal=True)
