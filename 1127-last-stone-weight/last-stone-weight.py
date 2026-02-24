class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        def max_heapify(nums: list, i: int, size: int) -> None:
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
    
        def build_max_heap(nums: list) -> None:
            n = len(nums)
    
            for i in range((n - 2) // 2, -1, -1):
                max_heapify(nums, i, n)
    
        def take_max(nums: list) -> int:
            maximal = nums[0]
            nums[0] = nums[-1]
            del nums[-1]
            if len(nums) > 0:
                max_heapify(nums, 0, len(nums))
            return maximal
    
        def add(nums: list, item: int) -> None:
            nums.append(item)
            i = len(nums) - 1
            while i > 0:
                j = (i - 1) // 2
                if nums[j] >= nums[i]:
                    break
                nums[j], nums[i] = nums[i], nums[j]
                i = j
    
        build_max_heap(stones)
    
        while len(stones) > 1:
            y = take_max(stones)
            x = take_max(stones)
            if y != x:
                add(stones, y - x)
    
        if stones:
            return stones[0]
        return 0