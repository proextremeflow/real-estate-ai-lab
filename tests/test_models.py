from decimal import Decimal
import pytest
from real_estate_ai.models import Property


def test_valid_property():
    property_ = Property(city="Kołobrzeg", area_m2=Decimal("47.5"), rooms=2)
    assert property_.area_m2 == Decimal("47.5")


@pytest.mark.parametrize("area,rooms", [("0", 2), ("40", 0)])
def test_invalid_property(area, rooms):
    with pytest.raises(ValueError):
        Property(city="Kołobrzeg", area_m2=Decimal(area), rooms=rooms)
