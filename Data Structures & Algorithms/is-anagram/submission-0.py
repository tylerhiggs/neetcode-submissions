class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for c in s:
            if c in ds:
                ds[c] += 1
                continue
            ds[c] = 1
        for c in t:
            if c in dt:
                dt[c] += 1
                continue
            dt[c] = 1
        for key in ds:
            if key not in dt or ds[key] != dt[key]:
                return False
        for key in dt:
            if key not in ds or ds[key] != dt[key]:
                return False
        return True