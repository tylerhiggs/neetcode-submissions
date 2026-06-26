class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        i, j = 0, len(nums) - 1
        while i < j - 1:
            mid = (i + j) // 2
            if nums[i] < nums[mid]:
                i = mid
            if nums[mid] < nums[j]:
                j = mid
        return min(nums[i:j+1])