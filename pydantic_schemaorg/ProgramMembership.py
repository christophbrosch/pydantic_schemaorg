from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ProgramMembership(Intangible):
    """Used to describe membership in a loyalty programs (e.g. \"StarAliance\"), traveler"
     "clubs (e.g. \"AAA\"), purchase clubs (\"Safeway Club\"), etc.

    See: https://schema.org/ProgramMembership
    Model depth: 3
    """

    type_: str = Field(default="ProgramMembership", alias="@type", Literal=True)
    members: Optional[
        Union[List[Union["Organization", "Person", str]], "Organization", "Person", str]
    ] = Field(
        default=None,
        description="A member of this organization.",
    )
    member: Optional[
        Union[List[Union["Organization", "Person", str]], "Organization", "Person", str]
    ] = Field(
        default=None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
        "organizations; ProgramMembership is typically for individuals.",
    )
    membershipPointsEarned: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "QuantitativeValue", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The number of membership points earned by the member. If necessary, the unitText can"
        "be used to express the units the points are issued in. (E.g. stars, miles, etc.)",
    )
    programName: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The program providing the membership. It is preferable to use [:program](https://schema.org/program)"
        "instead.",
    )
    hostingOrganization: Optional[
        Union[List[Union["Organization", str]], "Organization", str]
    ] = Field(
        default=None,
        description="The Organization (airline, travelers' club, retailer, etc.) the membership is made"
        "with or which offers the MemberProgram.",
    )
    membershipNumber: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A unique identifier for the membership.",
    )
    program: Optional[
        Union[List[Union["MemberProgram", str]], "MemberProgram", str]
    ] = Field(
        default=None,
        description="The [MemberProgram](https://schema.org/MemberProgram) associated with a [ProgramMembership](https://schema.org/ProgramMembership).",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MemberProgram import MemberProgram
