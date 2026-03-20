class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        h1 = {}
        h2 = {}
        ans = []

        for num in nums1:
            if h1.get(num) is None:
                h1[num] = 0

        for num in nums2:
            if h2.get(num) is None:
                h2[num] = 0

        for key in h1.keys():
            if h2.get(key) is not None:
                ans.append(key)
        return ans