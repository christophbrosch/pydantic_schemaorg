from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OnlineBusiness import OnlineBusiness


class OnlineStore(OnlineBusiness):
    """An eCommerce site.

    See: https://schema.org/OnlineStore
    Model depth: 4
    """

    type_: str = Field(default="OnlineStore", alias="@type", Literal=True)
