"""Vehicle types and the size hierarchy they park under."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum


class VehicleSize(IntEnum):
    """Ordered so `vehicle.size <= spot.size` means "fits in".

    MOTORCYCLE < COMPACT < LARGE: a motorcycle fits any spot, a car fits
    a compact or large spot, a bus only fits a large spot. Being an
    IntEnum (rather than a flat equality-only enum) is what makes the
    "smaller vehicle can overflow into a bigger spot" rule a one-line
    comparison instead of a lookup table.
    """

    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


@dataclass
class Vehicle:
    """Base vehicle. license_plate is treated as the vehicle's identity."""

    license_plate: str
    size: VehicleSize

    def fits_in(self, spot_size: VehicleSize) -> bool:
        return self.size <= spot_size


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate, VehicleSize.MOTORCYCLE)


class Car(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate, VehicleSize.COMPACT)


class Bus(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate, VehicleSize.LARGE)
