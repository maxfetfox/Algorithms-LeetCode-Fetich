class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []

        def bubble_up(i: int) -> None:
            while i > 0:
                j = (i - 1) // 2
                if max_heap[j][0] >= max_heap[i][0]:
                    break
                max_heap[i], max_heap[j] = max_heap[j], max_heap[i]
                i = j

        def bubble_down(i: int) -> None:
            size = len(max_heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < size and max_heap[left][0] > max_heap[largest][0]:
                    largest = left
                if right < size and max_heap[right][0] > max_heap[largest][0]:
                    largest = right
                if largest == i:
                    break

                max_heap[i], max_heap[largest] = max_heap[largest], max_heap[i]
                i = largest

        for x, y in points:
            distance = x ** 2 + y ** 2
            if len(max_heap) < k:
                max_heap.append((distance, [x, y]))
                bubble_up(len(max_heap) - 1)
            else:
                if distance < max_heap[0][0]:
                    max_heap[0] = (distance, [x, y])
                    bubble_down(0)

        result = []
        for item in max_heap:
            result.append(item[1])
        return result

