"""ParkingLot: the public facade. park_vehicle() / leave() are the whole API."""

from __future__ import annotations

import threading
import time
import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional

from .allocation_strategy import AllocationStrategy, SmallestFitFirstStrategy
from .exceptions import InvalidTicketError, ParkingFullError
from .level import Level
from .pricing import HourlyPricingStrategy, PricingStrategy
from .ticket import Ticket
from .vehicle import Vehicle, VehicleSize


@dataclass
class Receipt:
    ticket_id: str
    license_plate: str
    entry_time: float
    exit_time: float
    fee: float


class ParkingLot:
    def __init__(
        self,
        levels: List[Level],
        allocation_strategy: Optional[AllocationStrategy] = None,
        pricing_strategy: Optional[PricingStrategy] = None,
    ) -> None:
        self._levels = levels
        self._levels_by_number: Dict[int, Level] = {lvl.level_number: lvl for lvl in levels}
        self._allocation_strategy = allocation_strategy or SmallestFitFirstStrategy()
        self._pricing_strategy = pricing_strategy or HourlyPricingStrategy()
        self._tickets: Dict[str, Ticket] = {}
        self._tickets_lock = threading.Lock()

    def park_vehicle(self, vehicle: Vehicle) -> Ticket:
        spot = self._allocation_strategy.find_and_allocate(self._levels, vehicle)
        if spot is None:
            raise ParkingFullError(
                f"No spot available for {vehicle.license_plate} (size={vehicle.size.name})"
            )
        ticket = Ticket(id=str(uuid.uuid4()), vehicle=vehicle, spot=spot, entry_time=time.time())
        with self._tickets_lock:
            self._tickets[ticket.id] = ticket
        return ticket

    def leave(self, ticket_id: str) -> Receipt:
        with self._tickets_lock:
            ticket = self._tickets.pop(ticket_id, None)
        if ticket is None:
            raise InvalidTicketError(f"Unknown or already-used ticket id: {ticket_id}")

        level = self._levels_by_number[ticket.spot.level]
        level.release(ticket.spot)

        exit_time = time.time()
        fee = self._pricing_strategy.compute_fee(ticket, exit_time)
        return Receipt(
            ticket_id=ticket.id,
            license_plate=ticket.vehicle.license_plate,
            entry_time=ticket.entry_time,
            exit_time=exit_time,
            fee=fee,
        )

    def availability(self) -> Dict[VehicleSize, int]:
        totals = {size: 0 for size in VehicleSize}
        for level in self._levels:
            for size in VehicleSize:
                totals[size] += level.available_count(size)
        return totals
