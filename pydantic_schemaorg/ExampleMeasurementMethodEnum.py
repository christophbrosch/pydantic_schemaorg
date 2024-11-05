from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MeasurementMethodEnum import MeasurementMethodEnum


class ExampleMeasurementMethodEnum(MeasurementMethodEnum):
    """An example [[MeasurementMethodEnum]] (to remove when real enums are added).

    See: https://schema.org/ExampleMeasurementMethodEnum
    Model depth: 5
    """

    type_: str = Field(
        default="ExampleMeasurementMethodEnum", alias="@type", Literal=True
    )
