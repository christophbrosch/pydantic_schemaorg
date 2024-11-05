from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class CertificationStatusEnumeration(Enumeration):
    """Enumerates the different statuses of a Certification (Active and Inactive).

    See: https://schema.org/CertificationStatusEnumeration
    Model depth: 4
    """

    type_: str = Field(
        default="CertificationStatusEnumeration", alias="@type", Literal=True
    )
