class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        res = set()
        for i in range(len(s)):
            target = -s[i]
            j = i + 1
            k = len(s) - 1
            while j < k:
                if s[j] + s[k] == target:
                    res.add(tuple(sorted([s[i], s[j], s[k]])))
                    j += 1
                    continue
                if s[j] + s[k] < target:
                    j += 1
                    continue
                k -= 1
        return [list(i) for i in res]


