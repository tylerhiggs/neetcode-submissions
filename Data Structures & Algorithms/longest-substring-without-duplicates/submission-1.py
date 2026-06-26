class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f = { c: 0 for c in s}
        used = set()
        r = 0
        best = 0
        for l in range(len(s)):
            while r < len(s) and not len(used):
                f[s[r]] += 1
                if f[s[r]] > 1:
                    used.add(s[r])
                    r += 1
                    break
                best = max(best, r-l + 1)
                r += 1

            f[s[l]] -= 1
            if f[s[l]] == 1:
                used.remove(s[l])
        return best
                

