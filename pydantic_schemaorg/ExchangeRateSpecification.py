from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class ExchangeRateSpecification(StructuredValue):
    """A structured value representing exchange rate.

    See: https://schema.org/ExchangeRateSpecification
    Model depth: 4
    """

    type_: str = Field(default="ExchangeRateSpecification", alias="@type", Literal=True)
    currency: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The currency in which the monetary amount is expressed. Use standard formats: [ISO 4217"
        'currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker'
        "symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies,"
        'e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)'
        '(LETS) and other currency types, e.g. "Ithaca HOUR".',
    )
    currentExchangeRate: Optional[
        Union[List[Union["UnitPriceSpecification", str]], "UnitPriceSpecification", str]
    ] = Field(
        default=None,
        description="The current price of a currency.",
    )
    exchangeRateSpread: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "MonetaryAmount", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "MonetaryAmount",
            str,
        ]
    ] = Field(
        default=None,
        description="The difference between the price at which a broker or other intermediary buys and sells"
        "foreign currency.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.UnitPriceSpecification import UnitPriceSpecification
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
