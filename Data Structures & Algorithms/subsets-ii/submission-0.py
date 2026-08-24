class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(2**len(nums)):
            current = []
            bits = i
            for j in range(len(nums)):
                bit = bits % 2 == 1
                if bit:
                    current.append(nums[j])
                bits //=2
            current.sort()
            res.add(tuple(current))
        return list(res)