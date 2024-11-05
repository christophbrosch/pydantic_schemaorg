from typing import Optional, List

from pydantic import BaseModel, ValidationInfo, field_validator


class PydanticBase(BaseModel):
    name: str
    description: str
    valid_name: Optional[str] = None

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @field_validator("valid_name")
    def validate_name(cls, value) -> str:
        if not value:
            raise ValueError()
        elif value in {
            "class",
            "def",
            "from",
            "import",
            "return",
            "yield",
            "True",
            "False",
        }:
            return f"{value}_"
        if value[0].isdigit():
            return f"_{value}"
        return value


class PydanticField(PydanticBase):
    type: str


class Import(BaseModel):
    type: str
    classPath: str
    classes_: set


class PydanticClass(PydanticBase):
    fields: List[PydanticField]
    parents: List["PydanticClass"]
    depth: int = 1
    parent_imports: List[Import]
    field_imports: List[Import]
    pydantic_imports: List[Import] = []
    forward_refs: List[Import] = []
    filename: str = ""

    # TODO[pydantic]: We couldn't refactor the `validator`, please replace it by `field_validator` manually.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-validators for more information.
    @field_validator("filename")
    def validate_filename(cls, value) -> str:
        if not value:
            raise ValueError()
        filename = value
        if filename in {
            "class",
            "def",
            "from",
            "import",
            "return",
            "yield",
        }:
            return f"{filename}_"
        return value


PydanticClass.model_rebuild()
