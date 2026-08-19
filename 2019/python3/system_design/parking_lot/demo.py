"""Quick usage demo. Run with: python -m parking_lot.demo"""

from .exceptions import ParkingFullError
from .level import Level
from .parking_lot import ParkingLot
from .vehicle import Bus, Car, Motorcycle, VehicleSize


def build_two_level_lot() -> ParkingLot:
    level0 = Level(0, {VehicleSize.MOTORCYCLE: 2, VehicleSize.COMPACT: 3, VehicleSize.LARGE: 1})
    level1 = Level(1, {VehicleSize.MOTORCYCLE: 2, VehicleSize.COMPACT: 3, VehicleSize.LARGE: 1})
    return ParkingLot([level0, level1])


def main() -> None:
    lot = build_two_level_lot()
    print("Initial availability:", {s.name: c for s, c in lot.availability().items()})

    t1 = lot.park_vehicle(Car("CAR-001"))
    lot.park_vehicle(Motorcycle("BIKE-001"))
    lot.park_vehicle(Bus("BUS-001"))
    print("After parking 1 car, 1 motorcycle, 1 bus:",
          {s.name: c for s, c in lot.availability().items()})

    receipt = lot.leave(t1.id)
    print(f"CAR-001 left. Fee: ${receipt.fee}")
    print("After CAR-001 leaves:", {s.name: c for s, c in lot.availability().items()})

    # Drain the remaining large spots to show ParkingFullError firing.
    filled = 0
    try:
        while True:
            filled += 1
            lot.park_vehicle(Bus(f"BUS-FILL-{filled}"))
    except ParkingFullError as e:
        print(f"Expected failure after filling {filled - 1} more large spot(s):", e)


if __name__ == "__main__":
    main()
