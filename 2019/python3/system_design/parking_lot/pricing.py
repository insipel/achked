"""Pluggable pricing strategy, deliberately decoupled from allocation.

Kept as its own interface so pricing can change (flat rate, per-minute,
surge pricing, membership discounts) without touching ParkingLot or the
allocation logic at all.
"""

from __future__ import annotations

import math
from typing import Dict, Optional, Protocol

from .ticket import Ticket
from .vehicle import VehicleSize

DEFAULT_HOURLY_RATES: Dict[VehicleSize, float] = {
    VehicleSize.MOTORCYCLE: 1.0,
    VehicleSize.COMPACT: 2.5,
    VehicleSize.LARGE: 5.0,
}


class PricingStrategy(Protocol):
    def compute_fee(self, ticket: Ticket, exit_time: float) -> float:
        ...


class HourlyPricingStrategy:
    """Charges per full hour (rounded up, one-hour minimum), by the
    vehicle's size class."""

    def __init__(self, rates: Optional[Dict[VehicleSize, float]] = None) -> None:
        self.rates = rates or DEFAULT_HOURLY_RATES

    def compute_fee(self, ticket: Ticket, exit_time: float) -> float:
        duration_hours = max(0.0, (exit_time - ticket.entry_time) / 3600)
        billable_hours = max(1, math.ceil(duration_hours))
        rate = self.rates[ticket.vehicle.size]
        return round(billable_hours * rate, 2)
