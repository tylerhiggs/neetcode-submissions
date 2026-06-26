class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if nums[i] < nums[mid]:
                if nums[i] <= target <= nums[mid]:
                    j = mid - 1
                    continue
                i = mid + 1
                continue
            if nums[mid] <= target <= nums[j]:
                i = mid + 1
                continue
            j = mid - 1
        return -1 if nums[i] != target and nums[j] != target else (i if nums[i] == target else j)