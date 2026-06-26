class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1 for _ in nums], [1 for _ in nums]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[-i - 1] = suffix[-i] * nums[-i]
        return [prefix[i] * suffix[i] for i in range(len(nums))]

        