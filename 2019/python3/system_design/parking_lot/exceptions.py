"""Errors raised by the parking lot's public API."""

from __future__ import annotations


class ParkingLotError(Exception):
    """Base class for all parking lot errors."""


class ParkingFullError(ParkingLotError):
    """Raised when no spot anywhere in the lot fits the vehicle."""


class InvalidTicketError(ParkingLotError):
    """Raised when leave() is called with an unknown or already-used ticket id."""
