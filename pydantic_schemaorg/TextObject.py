from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class TextObject(MediaObject):
    """A text file. The text can be unformatted or contain markup, html, etc.

    See: https://schema.org/TextObject
    Model depth: 4
    """

    type_: str = Field(default="TextObject", alias="@type", Literal=True)
