class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = [-num for num in nums[:k]]
        heapq.heapify(h)
        f = {num: 0 for num in nums}
        ans = []
        for i in range(k):
            f[nums[i]] += 1
            heapq.heappush(h, -nums[i])
        for i in range(len(nums) - k):
            while f[-h[0]] == 0:
                heapq.heappop(h)
            ans.append(-h[0])
            f[nums[i]] -= 1
            f[nums[i+k]] += 1
            heapq.heappush(h, -nums[i+k])
        while f[-h[0]] == 0:
            heapq.heappop(h)
        ans.append(-h[0])
        return ans