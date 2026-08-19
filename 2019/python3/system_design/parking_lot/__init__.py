"""Parking Lot System — see README.md for the full design write-up.

Quick start:
    from parking_lot import ParkingLot, Level, Car, VehicleSize

    lot = ParkingLot([Level(0, {VehicleSize.COMPACT: 50})])
    ticket = lot.park_vehicle(Car("ABC-123"))
    receipt = lot.leave(ticket.id)
"""

from .exceptions import InvalidTicketError, ParkingFullError, ParkingLotError
from .level import Level
from .parking_lot import ParkingLot, Receipt
from .pricing import HourlyPricingStrategy
from .ticket import Ticket
from .vehicle import Bus, Car, Motorcycle, Vehicle, VehicleSize

__all__ = [
    "InvalidTicketError",
    "ParkingFullError",
    "ParkingLotError",
    "Level",
    "ParkingLot",
    "Receipt",
    "HourlyPricingStrategy",
    "Ticket",
    "Bus",
    "Car",
    "Motorcycle",
    "Vehicle",
    "VehicleSize",
]
