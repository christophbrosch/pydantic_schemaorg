import re
from typing import Optional, Dict, Any, Pattern, Union
from pydantic import BaseModel, Field
from pydantic_core import core_schema, validate_core_schema

# Define the regex pattern globally.
_url_regex_cache: Union[Pattern[str], None] = None


def ISO8601Date_regex() -> Pattern[str]:
    global _url_regex_cache
    if _url_regex_cache is None:
        _url_regex_cache = re.compile(
            r"(?P<year>-?(?:[1-9][0-9]*)?[0-9]{4})-?(?P<month>1[0-2]|0[1-9])?-?(?P<day>3[01]|0[1-9]|[12][0-9])?(T(?P<hour>(2[0-3]|[01][0-9])))?(\:(?P<minute>[0-5][0-9]))?(\:(?P<second>[0-5][0-9]))?(\.(?P<microsecond>[0-9]+))?([+-](?P<timezone>([0-9]{2}\:[0-9]{2})|Z))?",
            re.IGNORECASE,
        )
    return _url_regex_cache


class ISO8601Date:
    strip_whitespace = True
    min_length = 1
    max_length = 2**16

    def __init__(
        self,
        date: str,
        *,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
        microsecond: Optional[int] = None,
        tz: Optional[str] = None,
    ) -> None:
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.tz = tz

    @classmethod
    def build(
        cls,
        date: str,
        *,
        year: int,
        month: Optional[int] = None,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
        microsecond: Optional[int] = None,
        tz: Optional[str] = None,
    ) -> str:
        date = ""
        if year:
            date += str(year)
        if month:
            date += f"-{month:02}"
        if day:
            date += f"-{day:02}"
        if hour:
            date += f"T{hour:02}"
        if minute:
            date += f":{minute:02}"
        if second:
            date += f":{second:02}"
        if microsecond:
            date += f".{microsecond}"
        return date

    @classmethod
    def validate(cls, value: Any) -> "ISO8601Date":
        value = str(value)
        if cls.strip_whitespace:
            value = value.strip()
        date_str = value

        m = ISO8601Date_regex().match(date_str)
        if not m:
            raise ValueError("ISO8601Date regex failed unexpectedly")

        parts = m.groupdict()
        parts = cls.validate_parts(parts)
        if m.end() != len(date_str):
            raise ValueError("Invalid ISO8601 date")

        validated_date = cls(
            date_str,
            year=int(parts["year"]),
            month=int(parts["month"]) if parts["month"] else None,
            day=int(parts["day"]) if parts["day"] else None,
            hour=int(parts["hour"]) if parts["hour"] else None,
            minute=int(parts["minute"]) if parts["minute"] else None,
            second=int(parts["second"]) if parts["second"] else None,
            microsecond=int(parts["microsecond"]) if parts["microsecond"] else None,
            tz=parts["tz"],
        )
        return validated_date

    @classmethod
    def validate_parts(
        cls, parts: Dict[str, Optional[str]]
    ) -> Dict[str, Union[str, int]]:
        parts_order = [
            "year",
            "month",
            "day",
            "hour",
            "minute",
            "second",
            "microsecond",
            "tz",
        ]
        for part_order in parts_order:
            parts[part_order] = parts.get(part_order, None)
            if parts[part_order] is not None and part_order != "tz":
                parts[part_order] = int(parts[part_order])
        return parts

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler) -> Any:
        return core_schema.str_schema(
            ref="ISO8601Date",
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls, schema: Dict[str, Any], handler
    ) -> Dict[str, Any]:
        schema.update(
            {
                "type": "string",
                "format": "ISO8601",
                "minLength": cls.min_length,
                "maxLength": cls.max_length,
            }
        )
        return schema
