# Parking Lot System

Single-process, in-memory reference implementation of the classic
"design a parking lot" OOD interview question — allocate/free spots by
vehicle size, track availability. This is the working-code counterpart
to the design discussion it came out of; see the "what this deliberately
doesn't do" section at the bottom for the production-scale gaps that
were called out but not implemented here.

## File map

| File                     | Contents                                                              |
|---------------------------|------------------------------------------------------------------------|
| `vehicle.py`              | `VehicleSize` (ordered enum) and `Vehicle`/`Motorcycle`/`Car`/`Bus`     |
| `spot.py`                 | `ParkingSpot` — id, size, level, occupying vehicle                     |
| `level.py`                | `Level` — owns the spots on one floor and the free-spot pools          |
| `ticket.py`                | `Ticket` — issued on entry, used to free the spot on exit              |
| `pricing.py`               | `PricingStrategy` interface + `HourlyPricingStrategy`                  |
| `allocation_strategy.py`   | `AllocationStrategy` interface + `SmallestFitFirstStrategy`            |
| `parking_lot.py`           | `ParkingLot` — the public facade: `park_vehicle()` / `leave()`         |
| `exceptions.py`            | `ParkingFullError`, `InvalidTicketError`                               |
| `demo.py`                  | Runnable walkthrough (`python -m parking_lot.demo`)                    |
| `test_parking_lot.py`      | Unit tests + a concurrency regression test                             |

## Run it

```bash
python3 -m parking_lot.demo
python3 -m unittest parking_lot.test_parking_lot -v
# or, if pytest is installed:
python3 -m pytest test_parking_lot.py -v
```

## Design decisions and why

**Size is an ordered enum, not a flat category.** `VehicleSize` is an
`IntEnum` (`MOTORCYCLE < COMPACT < LARGE`), so "does this vehicle fit in
this spot" is `vehicle.size <= spot.size` — one comparison instead of a
lookup table — and a motorcycle can legally overflow into a compact or
large spot when its own size is full.

**Allocation always prefers the smallest fitting spot.**
`SmallestFitFirstStrategy` walks sizes from the vehicle's own size
upward, so a motorcycle never burns a large spot while a
motorcycle-sized one is free. This is the detail that's easy to miss if
you model spots as one flat pool.

**Free spots are bucketed per (level, size) in a heap, not scanned.**
`Level` keeps `Dict[VehicleSize, List[spot_id]]` as a min-heap, so
`try_allocate` is O(log n) instead of an O(n) scan over every spot on
the level, and the lowest id — closest to the entrance, by construction
order — is always handed out first.

**Exit is ticket-based, O(1), not a search.** `park_vehicle()` returns a
`Ticket`; `leave(ticket_id)` looks it up in a dict rather than searching
the lot for a matching license plate. This is also where duration-based
pricing naturally hangs off `ticket.entry_time`.

**Concurrency is handled per level, not globally or per-spot.** Reserving
a spot id (popping off the heap) and assigning the vehicle to it happen
atomically inside `Level`'s lock, so two threads racing to park never
get handed the same spot — see
`test_concurrent_parking_never_double_books_a_spot`, which fires 50
threads at 5 spots and asserts exactly 5 succeed with no spot reused.
A lock per level is a reasonable middle ground between one global lock
(correct but serializes the whole lot) and one lock per spot (finer
grained than this problem needs).

**Allocation and pricing are both pluggable interfaces.** `AllocationStrategy`
and `PricingStrategy` are `Protocol`s the `ParkingLot` depends on, not
inlined logic — swapping "smallest fit first" for "nearest to elevator"
or adding surge pricing doesn't touch `ParkingLot`, `Level`, or each
other.

## What this deliberately doesn't do

This is the in-memory, single-process version — correct and
concurrency-safe within one process, but there are known gaps if this
became a real multi-garage service, called out here rather than silently
glossed over:

- **Not durable / not multi-instance safe.** The free-spot pools live in
  process memory. Two instances behind a load balancer would each think
  they own the source of truth. A real deployment needs allocation to
  happen inside a DB transaction (e.g. `SELECT ... FOR UPDATE SKIP LOCKED`
  against a `parking_spots` table) instead of an in-memory heap + lock.
- **No idempotency key on `park_vehicle`.** A retried "vehicle entered"
  webhook from real gate hardware would allocate a second spot for the
  same plate. Production needs `park_vehicle` keyed on the gate's event
  id, not called blind.
- **No reconciliation against physical reality.** Sensors fail, people
  tailgate through gates. Nothing here detects drift between "system
  thinks this spot is free" and "a car is actually in it."
- **No latency/failure-mode budget.** There's a real gate arm on the
  other end of `park_vehicle` in production; this version doesn't model
  degraded-mode behavior (e.g. fail open with an attendant-issued ticket
  if the backing store is unreachable).
