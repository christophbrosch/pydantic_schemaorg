from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration


class NegativeFilmDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/negativeFilm\">negative"
     "film</a></a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital"
     "source type</a> vocabulary.

    See: https://schema.org/NegativeFilmDigitalSource
    Model depth: 6
    """

    type_: str = Field(default="NegativeFilmDigitalSource", alias="@type", Literal=True)