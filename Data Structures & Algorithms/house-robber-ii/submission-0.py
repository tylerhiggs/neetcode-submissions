class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        if n == 1:
            return nums[0]
        mem = [[None, None] for _ in range(n)]
        def sub(i: int, includes_first: int) -> int: # 0 or 1 for includes_first
            if includes_first and i == n - 1:
                return 0
            if i > n - 1:
                return 0
            if mem[i][includes_first] != None:
                return mem[i][includes_first]
            mem[i][includes_first] = max(nums[i] + sub(i + 2, includes_first), sub(i + 1, includes_first))
            return mem[i][includes_first]
        return max(nums[0] + sub(2, 1), sub(1, 0))
            
