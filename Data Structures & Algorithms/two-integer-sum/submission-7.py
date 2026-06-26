class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = sorted(enumerate(nums), key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i < j:
            su = s[i][1] + s[j][1]
            if su == target:
                return sorted([s[i][0], s[j][0]])
            if su < target:
                i += 1
                continue
            j -= 1
        return sorted([s[i][0], s[j][0]])