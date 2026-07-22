class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[i] < nums[mid]:
                i = mid
                continue
            if nums[mid] < nums[j]:
                j = mid
                continue
            return nums[j]
        return nums[j]