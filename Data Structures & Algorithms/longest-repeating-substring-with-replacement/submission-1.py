class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        i = 0
        best = 0
        f = {c: 0 for c in s}
        for j in range(len(s)):
            f[s[j]] += 1
            maxf = max(maxf, f[s[j]])

            while j - i + 1 - maxf > k:
                f[s[i]] -= 1
                i += 1
            best = max(best, j - i + 1)
        return best