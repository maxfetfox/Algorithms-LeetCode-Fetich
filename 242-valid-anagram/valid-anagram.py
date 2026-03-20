class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = [0] * 26

        if len(s) != len(t):
            return False

        for letter in s:
            h[ord(letter) - 97] += 1

        for letter in t:
            h[ord(letter) - 97] -= 1

        for num in h:
            if num != 0:
                return False

        return True