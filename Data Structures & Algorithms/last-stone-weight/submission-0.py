class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-w for w in stones]
        heapq.heapify(h)
        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x == y:
                continue
            heapq.heappush(h, y - x)
        return -h[0] if len(h) else 0
