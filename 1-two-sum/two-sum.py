class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in h.keys():
                return [h[diff], i]
            h[nums[i]] = i
        return []