from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Physician import Physician


class PhysiciansOffice(Physician):
    """A doctor's office or clinic.

    See: https://schema.org/PhysiciansOffice
    Model depth: 5
    """

    type_: str = Field(default="PhysiciansOffice", alias="@type", Literal=True)
