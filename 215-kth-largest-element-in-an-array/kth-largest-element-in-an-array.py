class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def max_heapify(nums, i, size):
            while True:
                left = 2 * i + 1
                right = 2 * i + 2

                if left < size and nums[left] > nums[i]:
                    largest = left
                else:
                    largest = i

                if right < size and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    break

                nums[i], nums[largest] = nums[largest], nums[i]

                i = largest

        def build_max_heap(nums):
            n = len(nums)

            for i in range((n - 2) // 2, -1, -1):
                max_heapify(nums, i, n)

        def heapsort(nums):
            n = len(nums)

            build_max_heap(nums)

            size = n
            for i in range(n - 1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                size -= 1
                max_heapify(nums, 0, size)

            return nums
        return heapsort(nums)[-k]