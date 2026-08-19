"""A single level (floor) of the parking lot.

Free spots are bucketed by size into a min-heap of spot ids, so:
  - allocation (`try_allocate`) is O(log n) instead of scanning every spot
    on the level for a free one
  - the lowest id is always handed out first, which (given ids are
    assigned in a stable order at construction time) gives a deterministic
    "closest to the entrance first" allocation order for free
  - reservation (popping the id) and assignment (spot.assign) happen
    together under one lock, so two threads can never be handed the same
    spot — this is what the concurrency test in test_parking_lot.py checks
"""

from __future__ import annotations

import heapq
import threading
from typing import Dict, List, Optional

from .spot import ParkingSpot
from .vehicle import Vehicle, VehicleSize


class Level:
    def __init__(self, level_number: int, spots_by_size: Dict[VehicleSize, int]) -> None:
        """spots_by_size, e.g. {VehicleSize.MOTORCYCLE: 10, VehicleSize.COMPACT: 40,
        VehicleSize.LARGE: 5}, describes how many spots of each size this level has."""
        self.level_number = level_number
        self._lock = threading.Lock()
        self._spots: Dict[str, ParkingSpot] = {} # key is str: spot_id
        self._free_by_size: Dict[VehicleSize, List[str]] = {size: [] for size in VehicleSize}

        counter = 0
        for size, count in spots_by_size.items():
            for _ in range(count):
                # spot_id strings are pushed into a min-heap (heapq.heappush).
                # Because Python compares strings lexicographically,
                # zero-padding ensures that numerical order and alphabetical
                # order match:
                #
                # Creating a padded id for each spot. Counter has to be
                # zero-padded to 4 digits to ensure that the smallest number is
                # always the smallest string.
                spot_id = f"L{level_number}-{size.name[:1]}{counter:04d}"
                # Store the spot in a dictionary for fast lookup by ID.
                self._spots[spot_id] = ParkingSpot(id=spot_id, level=level_number, size=size)
                # Add the spot ID to the min-heap for this size.
                # min-heap is chosen to fetch the lexicographically smallest id
                # O(log n) time complexity for "nearest to the door" meaning
                # smallest spot number, because string comparison works that way
                heapq.heappush(self._free_by_size[size], spot_id)
                counter += 1

    def available_count(self, size: VehicleSize) -> int:
        with self._lock:
            return len(self._free_by_size[size])

    def try_allocate(self, size: VehicleSize, vehicle: Vehicle) -> Optional[ParkingSpot]:
        """Atomically reserve a free spot of exactly `size` for `vehicle`,
        or return None if this level has no free spot of that size."""
        with self._lock:
            pool = self._free_by_size[size]
            if not pool:
                return None
            spot_id = heapq.heappop(pool)
            spot = self._spots[spot_id]
            spot.assign(vehicle)
            return spot

    def release(self, spot: ParkingSpot) -> None:
        with self._lock:
            spot.release()
            heapq.heappush(self._free_by_size[spot.size], spot.id)
