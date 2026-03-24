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

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}

        for string in strs:
            sorted_key = ''.join(sorted([lttr for lttr in string]))

            if sorted_key not in h.keys():
                h[sorted_key] = []

            h[sorted_key].append(string)

        return [value for value in h.values()]