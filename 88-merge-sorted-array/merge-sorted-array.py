class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, ind = m - 1, n - 1, m + n - 1
        temp_lst = nums1[:m]
        # временный список для хранения значений из num1
        while i >= 0 or j >= 0:
            if j < 0: # если один список пуст, проходимся по оставшемуся
                nums1[ind] = temp_lst[i]
                i -= 1
                ind -= 1
            elif i < 0:
                nums1[ind] = nums2[j]
                j -= 1
                ind -= 1
            elif temp_lst[i] >= nums2[j]: # >= в случае, если обе переменные равны друг другу
                nums1[ind] = temp_lst[i]
                i -= 1
                ind -= 1
            elif nums2[j] > temp_lst[i]:
                nums1[ind] = nums2[j]
                j -= 1
                ind -= 1