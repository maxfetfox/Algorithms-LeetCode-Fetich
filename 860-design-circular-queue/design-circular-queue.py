class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.q = [0] * self.size
        self.tail = self.head = self.count = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.size # убирает необходимость доп. проверок
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
