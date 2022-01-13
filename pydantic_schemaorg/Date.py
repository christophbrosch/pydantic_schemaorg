from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.DataType import DataType


class Date(DataType):
    """A date value in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).

    See: https://schema.org/Date
    Model depth: 5
    """

    type_: str = Field("Date", const=True, alias="@type")


if TYPE_CHECKING:

    Date.update_forward_refs()