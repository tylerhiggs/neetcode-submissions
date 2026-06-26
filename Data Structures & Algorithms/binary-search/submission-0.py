class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (j + i) // 2
            if nums[mid] < target:
                i = mid + 1
                continue
            if nums[mid] > target:
                j = mid - 1
                continue
            return mid
        return -1 if nums[i] != target and nums[j] != target else i