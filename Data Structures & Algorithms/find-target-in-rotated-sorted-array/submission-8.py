class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            if nums[i] < nums[j]:
                if nums[mid] < target:
                    i = mid + 1
                    continue
                j = mid - 1
                continue
            if nums[mid] < nums[j]:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                    continue
                j = mid - 1
                continue
            if nums[i] <= target < nums[mid]:
                j = mid - 1
                continue
            i = mid + 1
        return i if nums[i] == target else -1 if i + 1 >= len(nums) or nums[i+1] != target else i+1
                
                