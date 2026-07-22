class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1 # inclusive window
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
                continue
            j = mid - 1
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j
        return -1
