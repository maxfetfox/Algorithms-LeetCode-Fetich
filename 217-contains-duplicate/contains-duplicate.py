class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        h = {}

        for num in nums:
            if h.get(num) != None:
                return True
            else:
                h[num] = '+'
        return False