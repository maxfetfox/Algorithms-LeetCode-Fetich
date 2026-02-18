class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            elif letters[mid] <= target:
                left = mid + 1
        if left < len(letters):
            # Возвращаем letters[left], потому что это первый элемент, подходящий под > target
            return letters[left]
        return letters[0]