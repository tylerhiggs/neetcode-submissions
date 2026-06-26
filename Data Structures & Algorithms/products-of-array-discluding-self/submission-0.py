class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        prod_without_zero = 1
        for num in nums:
            prod *= num
            zeros += 1 if not num else 0
            if not num and zeros == 1:
                continue
            prod_without_zero *= num
        if zeros > 1:
            return [0] * len(nums)
        return [int(prod / num) if num else prod_without_zero for num in nums]