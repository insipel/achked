from typing import List


class MyCircularQueue:
    def __init__(self, k: int):
        self.buffer: List[int] = [0] * k   # k pre-allocated slots
        self.capacity = k
        self.size = 0                      # how many slots are currently filled
        self.front = 0                     # index of the oldest element

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        write_index = (self.front + self.size) % self.capacity
        self.buffer[write_index] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.buffer[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear_index = (self.front + self.size - 1) % self.capacity
        return self.buffer[rear_index]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
