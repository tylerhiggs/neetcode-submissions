class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = {c: 0 for c in s}
        max_f = 0
        l = 0
        res = 0
        for r in range(len(s)):
            f[s[r]] += 1
            max_f = max(max_f, f[s[r]])
            while r - l + 1 - max_f > k:
                f[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res