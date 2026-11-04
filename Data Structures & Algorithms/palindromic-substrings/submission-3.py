class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        def help(l: int, r: int) -> int:
            res = 0
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        for i in range(n):
            ans += help(i, i)
            ans += help(i, i + 1)
        return ans