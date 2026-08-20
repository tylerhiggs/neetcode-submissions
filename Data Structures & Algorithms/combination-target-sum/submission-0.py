class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(i: int, current, total):
            if total == target:
                res.append(current[:])
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                current.append(nums[j])
                backtrack(j, current, total + nums[j])
                current.pop()
        backtrack(0, [], 0)
        return res
            

            
            