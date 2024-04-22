from __future__ import annotations

from decimal import Decimal


class Distance:
    val: Decimal
    DISTANCE_ERROR_TOLARANCE = 0.05

    def __init__(self, val: Decimal) -> None:
        self.val = val

    def __str__(self) -> str:
        return f'{self.val}'

    def is_equal(self, other: Distance) -> bool:
        return abs(self.val - other.val) < self.DISTANCE_ERROR_TOLARANCE
