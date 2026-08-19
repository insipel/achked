"""A single parking spot."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .vehicle import Vehicle, VehicleSize


@dataclass
class ParkingSpot:
    id: str
    level: int
    size: VehicleSize
    vehicle: Optional[Vehicle] = None

    @property
    def is_free(self) -> bool:
        return self.vehicle is None

    def assign(self, vehicle: Vehicle) -> None:
        if not self.is_free:
            raise ValueError(f"Spot {self.id} is already occupied")
        self.vehicle = vehicle

    def release(self) -> Vehicle:
        if self.is_free:
            raise ValueError(f"Spot {self.id} is already free")
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle
