from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration


class DigitalCaptureDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/digitalCapture\">digital"
     "capture</a></a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital"
     "source type</a> vocabulary.

    See: https://schema.org/DigitalCaptureDigitalSource
    Model depth: 6
    """

    type_: str = Field(
        default="DigitalCaptureDigitalSource", alias="@type", Literal=True
    )