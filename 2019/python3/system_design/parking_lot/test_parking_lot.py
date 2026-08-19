"""Unit + concurrency tests.

Run with:
    python -m pytest parking_lot/test_parking_lot.py -v
or, without pytest installed:
    python -m unittest parking_lot.test_parking_lot -v
"""

import threading
import unittest

from parking_lot.exceptions import InvalidTicketError, ParkingFullError
from parking_lot.level import Level
from parking_lot.parking_lot import ParkingLot
from parking_lot.vehicle import Bus, Car, Motorcycle, VehicleSize


def small_lot() -> ParkingLot:
    level0 = Level(0, {VehicleSize.MOTORCYCLE: 1, VehicleSize.COMPACT: 1, VehicleSize.LARGE: 1})
    return ParkingLot([level0])


class ParkingLotTests(unittest.TestCase):
    def test_park_and_availability(self):
        lot = small_lot()
        self.assertEqual(lot.availability()[VehicleSize.COMPACT], 1)
        lot.park_vehicle(Car("A"))
        self.assertEqual(lot.availability()[VehicleSize.COMPACT], 0)

    def test_vehicle_takes_matching_spot_first(self):
        lot = small_lot()
        lot.park_vehicle(Motorcycle("M1"))
        avail = lot.availability()
        self.assertEqual(avail[VehicleSize.MOTORCYCLE], 0)
        self.assertEqual(avail[VehicleSize.COMPACT], 1)  # untouched
        self.assertEqual(avail[VehicleSize.LARGE], 1)    # untouched

    def test_motorcycle_overflows_into_compact_then_large(self):
        lot = small_lot()
        lot.park_vehicle(Motorcycle("M1"))  # takes the motorcycle spot
        lot.park_vehicle(Motorcycle("M2"))  # overflows into the compact spot
        avail = lot.availability()
        self.assertEqual(avail[VehicleSize.COMPACT], 0)
        self.assertEqual(avail[VehicleSize.LARGE], 1)

    def test_park_full_raises(self):
        lot = small_lot()
        lot.park_vehicle(Bus("B1"))  # takes the only large spot
        with self.assertRaises(ParkingFullError):
            lot.park_vehicle(Bus("B2"))

    def test_leave_frees_spot_and_rejects_reuse(self):
        lot = small_lot()
        ticket = lot.park_vehicle(Car("A"))
        self.assertEqual(lot.availability()[VehicleSize.COMPACT], 0)

        receipt = lot.leave(ticket.id)
        self.assertEqual(receipt.license_plate, "A")
        self.assertEqual(lot.availability()[VehicleSize.COMPACT], 1)

        with self.assertRaises(InvalidTicketError):
            lot.leave(ticket.id)  # ticket already used

    def test_unknown_ticket_raises(self):
        lot = small_lot()
        with self.assertRaises(InvalidTicketError):
            lot.leave("not-a-real-ticket-id")

    def test_concurrent_parking_never_double_books_a_spot(self):
        """The test that actually matters: fire more concurrent allocation
        requests than there are matching spots and assert successes exactly
        equal the spot count, with no spot ever handed to two vehicles."""
        level0 = Level(0, {VehicleSize.COMPACT: 5})
        lot = ParkingLot([level0])

        results = []
        results_lock = threading.Lock()

        def try_park(i: int) -> None:
            try:
                ticket = lot.park_vehicle(Car(f"CAR-{i}"))
                with results_lock:
                    results.append(ticket.spot.id)
            except ParkingFullError:
                pass

        threads = [threading.Thread(target=try_park, args=(i,)) for i in range(50)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(len(results), 5, "exactly 5 of 50 concurrent requests should succeed")
        self.assertEqual(len(set(results)), 5, "no spot should ever be handed out twice")


if __name__ == "__main__":
    unittest.main()
