"""Pluggable spot allocation policy.

Kept as an interface (rather than inlined in ParkingLot) so the "which
free spot do we hand out" decision can change later — e.g. load-balanced
across levels, reserve a buffer near the entrance — without touching
ParkingLot or Level.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Protocol

from .spot import ParkingSpot
from .vehicle import Vehicle, VehicleSize

if TYPE_CHECKING:
    from .level import Level


class AllocationStrategy(Protocol):
    def find_and_allocate(self, levels: List["Level"], vehicle: Vehicle) -> Optional[ParkingSpot]:
        ...


class SmallestFitFirstStrategy:
    """Always hands out the smallest spot the vehicle fits in, so a
    motorcycle never occupies a large spot while a motorcycle-sized spot
    sits empty. Within a size class, levels are tried in list order (by
    convention, level 0 = closest to the entrance)."""

    def find_and_allocate(self, levels: List["Level"], vehicle: Vehicle) -> Optional[ParkingSpot]:
        for size in VehicleSize:
            if size < vehicle.size:
                continue
            for level in levels:
                spot = level.try_allocate(size, vehicle)
                if spot is not None:
                    return spot
        return None
