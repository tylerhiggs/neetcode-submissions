class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        heapq.heapify(self.h)
        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
            return self.h[0]
        if val < self.h[0]:
            return self.h[0]
        heapq.heappush(self.h, val)
        heapq.heappop(self.h)
        return self.h[0]