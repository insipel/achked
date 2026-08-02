# Min-Heap of (int, List[int]) in Python

## Goal
Implement a min-heap where each element is `(key: int, vector: List[int])`, ordered by `key`.

## Simple approach: raw `heapq`
`heapq` compares tuples element-wise, so it works directly on `(int, list)` tuples. Ties on the
int only fall through to comparing the lists (which works fine for ints, just element-by-element).

```python
import heapq

heap = []
heapq.heappush(heap, (5, [1, 2, 3]))
heapq.heappush(heap, (2, [4, 5]))
heapq.heappush(heap, (8, [6]))

smallest = heap[0]              # peek, O(1)
key, vec = heapq.heappop(heap)  # pop min, O(log n)
```

## Wrapper class approach
Avoids ever comparing the vectors on ties, and gives a nicer API.

```python
import heapq
from dataclasses import dataclass, field
from typing import List

@dataclass(order=True)
class HeapItem:
    key: int
    vector: List[int] = field(compare=False)  # excluded from comparisons

class MinHeap:
    def __init__(self):
        self._heap = []

    def push(self, key: int, vector: List[int]) -> None:
        heapq.heappush(self._heap, HeapItem(key, vector))

    def pop(self) -> HeapItem:
        return heapq.heappop(self._heap)

    def peek(self) -> HeapItem:
        return self._heap[0]

    def __len__(self) -> int:
        return len(self._heap)
```

Usage:

```python
h = MinHeap()
h.push(5, [1, 2, 3])
h.push(2, [4, 5])
item = h.pop()   # HeapItem(key=2, vector=[4, 5])
```

## Discussion notes

**`@dataclass(order=True)`**
Auto-generates comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`) based on fields in
declaration order — this is what lets `heapq` do `item_a < item_b` on `HeapItem` instances.
Without it, only `__eq__` is generated, and `heapq.heappush`/`heappop` would raise:
`TypeError: '<' not supported between instances of 'HeapItem'`.

Comparisons walk fields in order (`key` first, then `vector`), like comparing tuples
`(self.key, self.vector)` — hence needing `compare=False` on `vector` to exclude it.

**`vector: List[int] = field(compare=False)`**
Looks like a default-value assignment but isn't. `field()` is a sentinel that `@dataclass`
intercepts at class-creation time — it configures how the field is treated (included in
`__init__`, `__repr__`, comparisons, hashing, etc.) rather than becoming an actual default.

Here it means: `vector` is still required (no default, must be passed to `__init__`), but
excluded from generated comparisons.

To also give it a default (mutable types need `default_factory`, not `default`, to avoid
sharing one list across instances):

```python
vector: List[int] = field(default_factory=list, compare=False)
```

Other common `field()` options:
- `repr=False` — hide from `__repr__`
- `hash=False` — exclude from `__hash__`
- `init=False` — don't accept in `__init__` (usually paired with `default`/`default_factory`)
