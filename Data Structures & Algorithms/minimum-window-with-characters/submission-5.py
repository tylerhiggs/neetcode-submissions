class Solution:
    def minWindow(self, s: str, t: str) -> str:
        z = ord('A')
        ord_z = ord('z')
        letters = [0 for _ in range(ord_z - z + 1)]
        for c in t:
            letters[ord(c) - z] += 1
        t = tuple(letters)
        
        f = [0 for _ in range(ord_z - z + 1)]
        i, j = 0, 0
        def enough():
            return len([i for i in range(len(t)) if t[i] > f[i]]) == 0
        while not enough():
            if j == len(s):
                return ""
            f[ord(s[j]) - z] += 1
            j += 1
        best = [i,j - 1] # 0,1
        f[ord(s[j-1]) - z] -= 1
        for k in range(j - 1, len(s)):
            f[ord(s[k]) - z] += 1
            while enough():
                if k - i < best[1] - best[0]:
                    best = [i, k]
                f[ord(s[i]) - z] -= 1
                i += 1
        return s[best[0]:best[1] + 1]
            
        