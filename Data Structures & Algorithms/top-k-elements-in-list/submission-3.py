class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))] # buckets[i] has frequency i + 1
        freq = {n: 0 for n in nums}
        for num in nums:
            freq[num] += 1
        for num in freq:
            buckets[freq[num] - 1].append(num)
        return [item for bucket in buckets for item in bucket][-k:]

