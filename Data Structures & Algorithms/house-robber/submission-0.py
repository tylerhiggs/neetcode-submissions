class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [None for _ in range(n)]
        def sub(i: int) -> int:
            if i > n - 1:
                return 0
            if mem[i] != None:
                return mem[i]
            mem[i] = max(nums[i] + sub(i + 2), sub(i + 1))
            return mem[i]
        return sub(0)