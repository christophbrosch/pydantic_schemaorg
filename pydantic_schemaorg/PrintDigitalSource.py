from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration


class PrintDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/print\">print</a>'"
     "using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital"
     "source type</a> vocabulary.

    See: https://schema.org/PrintDigitalSource
    Model depth: 6
    """

    type_: str = Field(default="PrintDigitalSource", alias="@type", Literal=True)
