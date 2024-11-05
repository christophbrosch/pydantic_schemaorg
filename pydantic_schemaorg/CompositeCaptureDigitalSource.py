from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration


class CompositeCaptureDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/compositeCapture\">composite"
     "capture</a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital"
     "source type</a> vocabulary.

    See: https://schema.org/CompositeCaptureDigitalSource
    Model depth: 6
    """

    type_: str = Field(
        default="CompositeCaptureDigitalSource", alias="@type", Literal=True
    )
