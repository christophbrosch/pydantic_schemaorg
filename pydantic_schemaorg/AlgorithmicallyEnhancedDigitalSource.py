from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration


class AlgorithmicallyEnhancedDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/algorithmicallyEnhanced\">algorithmically"
     "enhanced</a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital"
     "source type</a> vocabulary.

    See: https://schema.org/AlgorithmicallyEnhancedDigitalSource
    Model depth: 6
    """

    type_: str = Field(
        default="AlgorithmicallyEnhancedDigitalSource", alias="@type", Literal=True
    )
