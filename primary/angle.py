from decimal import Decimal


class Angle():
    val: Decimal
    ANGLE_ERROR_TOLARANCE = 0.05

    def __init__(self, val: Decimal) -> None:
        self.val = val

    def is90(self) -> bool:
        return abs(90 - self.val) < self.ANGLE_ERROR_TOLARANCE

    def is45(self) -> bool:
        return abs(45 - self.val) < self.ANGLE_ERROR_TOLARANCE
