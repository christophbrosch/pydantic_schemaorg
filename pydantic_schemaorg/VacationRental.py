from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class VacationRental(LodgingBusiness):
    """A kind of lodging business that focuses on renting single properties for limited time.

    See: https://schema.org/VacationRental
    Model depth: 5
    """

    type_: str = Field(default="VacationRental", alias="@type", Literal=True)
