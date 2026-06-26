class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = sorted([(nums[i], i) for i in range(len(nums))], key=lambda x:x[0] )
        i, j = 0, len(nums)-1
        while i < j:
            if s[i][0] + s[j][0] == target:
                return sorted([s[i][1], s[j][1]])
            if s[i][0] + s[j][0] < target:
                i += 1
                continue
            j -= 1
        return False