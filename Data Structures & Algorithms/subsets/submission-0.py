class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def help(i=0) -> List[List[int]]:
            if i == len(nums):
                return [[]]
            res = help(i + 1)
            return res + [[nums[i]] + item for item in res]
        return help()