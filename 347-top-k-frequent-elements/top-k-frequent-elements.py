class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequent_elements = {}
        for x in nums:
            if x in frequent_elements:
                frequent_elements[x] += 1
            else:
                frequent_elements[x] = 1

        min_heap = []

        def bubble_up(i: int) -> None:
            while i > 0:
                j = (i - 1) // 2
                if min_heap[j][0] <= min_heap[i][0]:
                    break
                min_heap[i], min_heap[j] = min_heap[j], min_heap[i]
                i = j

        def bubble_down(i: int) -> None:
            size = len(min_heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < size and min_heap[left][0] < min_heap[smallest][0]:
                    smallest = left
                if right < size and min_heap[right][0] < min_heap[smallest][0]:
                    smallest = right
                if smallest == i:
                    break

                min_heap[i], min_heap[smallest] = min_heap[smallest], min_heap[i]
                i = smallest

        for number, count in frequent_elements.items():
            if len(min_heap) < k:
                min_heap.append((count, number))
                bubble_up(len(min_heap) - 1)
            else:
                if count > min_heap[0][0]:
                    min_heap[0] = (count, number)
                    bubble_down(0)

        result = []
        for items in min_heap:
            result.append(items[1])
        return result