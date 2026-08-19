class MedianFinder:

    def __init__(self):
        self.min_h = [] # top half + 1 or 0
        self.max_h = [] # bottom half

    def addNum(self, num: int) -> None:
        if not self.min_h:
            self.min_h.append(num)
            return

        median = -heapq.heappop(self.max_h) if len(self.min_h) == len(self.max_h) else heapq.heappop(self.min_h)
        if num > median:
            heapq.heappush(self.min_h, num)
            heapq.heappush(self.max_h, -median)
        else:
            heapq.heappush(self.min_h, median)
            heapq.heappush(self.max_h, -num)

    def findMedian(self) -> float:
        return (-self.max_h[0] + self.min_h[0]) / 2 if len(self.max_h) == len(self.min_h) else self.min_h[0]
        