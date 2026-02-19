class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right: # область поиска пуста
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid # возвращение индекса, если элемент найден
            elif nums[mid] > target:
                right = mid - 1 # уменьшение границы
            elif nums[mid] < target:
                left = mid + 1
        return -1