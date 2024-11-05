from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration


class DataDrivenMediaDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/dataDrivenMedia\">data"
     "driven media</a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital"
     "source type</a> vocabulary.

    See: https://schema.org/DataDrivenMediaDigitalSource
    Model depth: 6
    """

    type_: str = Field(
        default="DataDrivenMediaDigitalSource", alias="@type", Literal=True
    )
