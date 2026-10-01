class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0, 0) # inclusive
        n = len(s)
        mem = [[None for _ in range(n)] for _ in range(n)]
        def is_pal(i: int, j: int):
            if i == j or i - 1 == j:
                return True
            if i > j or i < 0 or j >= n:
                return False
            if mem[i][j] != None:
                return mem[i][j]
            if s[i] != s[j]:
                return False
            mem[i][j] = is_pal(i + 1, j - 1)
            return mem[i][j]
        for i in range(n):
            for j in range(i+1, n):
                if not is_pal(i, j):
                    continue
                if j - i < res[1] - res[0]:
                    continue
                res = (i, j)
        return s[res[0]:res[1]+1]
            
            
            
