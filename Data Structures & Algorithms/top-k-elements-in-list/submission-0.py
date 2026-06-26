class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {num: 0 for num in nums}
        buckets = [[] for _ in range(len(nums) + 1)]
        # get frequencies into f
        for num in nums:
            f[num] += 1
        # put into buckets
        for key in f:
            buckets[f[key]].append(key)
        res = []
        for bucket in buckets[::-1]:
            for num in bucket:
                res.append(num)
            if len(res) >= k:
                return res