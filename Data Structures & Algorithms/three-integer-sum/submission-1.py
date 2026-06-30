class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        so = sorted(nums)
        res = set()
        for k in range(len(so) - 2):
            # target = 1, i = 2, j = 5
            target = -so[k]
            i, j = k + 1, len(so) - 1
            while i < j:
                s = so[i] + so[j]
                if s < target:
                    i += 1
                    continue
                if s > target:
                    j -= 1
                    continue
                res.add((so[k], so[i], so[j]))
                i += 1
        return list(res)