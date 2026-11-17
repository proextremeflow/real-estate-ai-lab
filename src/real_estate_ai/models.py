"""Typy danych dla przyszłej wyceny; bez fikcyjnego modelu predykcyjnego."""
from dataclasses import dataclass
from decimal import Decimal
from typing import Literal


@dataclass(frozen=True)
class Property:
    city: str
    area_m2: Decimal
    rooms: int
    condition: str | None = None
    property_type: Literal["apartment", "house"] = "apartment"

    def __post_init__(self) -> None:
        if not self.city.strip():
            raise ValueError("City is required")
        if self.area_m2 <= 0:
            raise ValueError("Area must be positive")
        if self.rooms < 1:
            raise ValueError("Rooms must be at least one")
