class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        f1 = [0 for _ in range(26)]
        for c in s1:
            f1[ord(c) - 97] += 1
        # ord('a') is 97
        t1 = tuple(f1)
        f = [0 for _ in range(26)]
        for i in range(len(s1)):
            f[ord(s2[i]) - 97] += 1
        if t1 == tuple(f):
            return True
        for l in range(1, len(s2) - len(s1) + 1):
            f[ord(s2[l - 1]) - 97] -= 1
            f[ord(s2[l + len(s1) - 1]) - 97] += 1
            if t1 == tuple(f):
                return True
        return False