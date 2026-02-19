class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(A, l, m, r):
            nl = m - l + 1
            nr = r - m

            L = [0] * nl
            R = [0] * nr

            for i in range(nl):
                L[i] = A[l + i]
            for i in range(nr):
                R[i] = A[m + 1 + i]

            i, j, k = 0, 0, l

            while i < nl and j < nr:
                if L[i] <= R[j]:
                    A[k] = L[i]
                    i += 1
                else:
                    A[k] = R[j]
                    j += 1
                k += 1

            while i < nl:
                A[k] = L[i]
                i += 1
                k += 1

            while j < nr:
                A[k] = R[j]
                j += 1
                k += 1

        def merge_sort(A, l, r):
            if l >= r:
                return
            m = (l + r) // 2
            merge_sort(A, l, m)
            merge_sort(A, m + 1, r)
            merge(A, l, m, r)

        merge_sort(nums, 0, len(nums) - 1)
        return nums