class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {c: 0 for c in s}
        for c in s:
            freq[c] += 1
        for c in t:
            if c not in freq:
                return False
            freq[c] -= 1
        for c in freq:
            if freq[c] != 0:
                return False
        return True
        