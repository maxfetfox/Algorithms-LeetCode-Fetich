class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        self.k = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def bubble_up(self, i: int) -> None:
        while i > 0:
            j = (i - 1) // 2
            if self.min_heap[j] <= self.min_heap[i]:
                break
            self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]
            i = j

    def bubble_down(self, i: int) -> None:
        size = len(self.min_heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < size and self.min_heap[left] < self.min_heap[smallest]:
                smallest = left
            if right < size and self.min_heap[right] < self.min_heap[smallest]:
                smallest = right
            if smallest == i:
                break

            self.min_heap[i], self.min_heap[smallest] = self.min_heap[smallest], self.min_heap[i]
            i = smallest

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            self.min_heap.append(val)
            self.bubble_up(len(self.min_heap) - 1)
        else:
            if val > self.min_heap[0]:
                self.min_heap[0] = val
                self.bubble_down(0)

        return self.min_heap[0]