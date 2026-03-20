class Solution:
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