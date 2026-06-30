class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        s = set(nums)
        starts = [num for num in nums if num - 1 not in s]
        best = 1
        for num in starts:
            current = num
            while current in s:
                best = max(best, current - num + 1)
                current += 1
        return best

