class Solution:
    def _merge(self, arr, left, mid, right):
        # Размеры левой и правой частей
        left_size = mid - left + 1
        right_size = right - mid

        L = [0] * left_size
        R = [0] * right_size

        # Копирование левой части
        for i in range(left_size):
            L[i] = arr[left + i]

        # Копирование правой части
        for j in range(right_size):
            R[j] = arr[mid + j + 1]

        i = 0  # индекс для L
        j = 0  # индекс для R
        k = left  # индекс для arr

        # Слияние L и R в arr
        while i < left_size and j < right_size:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Копирование в arr, если в L остались элементы
        while i < left_size:
            arr[k] = L[i]
            i += 1
            k += 1

        # Копирование в arr, если в R остались элементы
        while j < right_size:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.merge_sort(arr, left, mid)
        self.merge_sort(arr, mid + 1, right)
        self._merge(arr, left, mid, right)

    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if h.get(letter) is not None:
                h[letter] += 1
            else:
                h[letter] = 1

        for letter in t:
            if h.get(letter) is not None:
                h[letter] -= 1
            else:
                return False

        for num in h.values():
            if num != 0:
                return False

        return True

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}

        for string in strs:
            string_list = [lttr for lttr in string]
            self.merge_sort(string_list, 0, len(string) - 1)
            sorted_key = ''.join(string_list)

            if sorted_key not in h.keys():
                h[sorted_key] = []

            h[sorted_key].append(string)

        return [value for value in h.values()]