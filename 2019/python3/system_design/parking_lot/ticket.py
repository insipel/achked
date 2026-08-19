"""Parking ticket issued on entry; used to reclaim/free a spot on exit.

Keying exits off a ticket id (O(1) dict lookup) rather than searching the
lot for a matching vehicle is what keeps `leave()` cheap regardless of how
many spots are occupied.
"""

from __future__ import annotations

from dataclasses import dataclass

from .spot import ParkingSpot
from .vehicle import Vehicle


@dataclass
class Ticket:
    id: str
    vehicle: Vehicle
    spot: ParkingSpot
    entry_time: float  # unix timestamp, set at park_vehicle() time
