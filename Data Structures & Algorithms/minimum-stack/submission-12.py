class MinStack:

    s = []
    h = []
    f = {}
    def __init__(self):
        heapq.heapify(self.h)
        self.h = []
        self.f = {}
        

    def push(self, val: int) -> None:
        self.s.append(val)
        heapq.heappush(self.h, val)
        if val in self.f:
            self.f[val] += 1
        else:
            self.f[val] = 1

    def pop(self) -> None:
        val = self.s.pop()
        self.f[val] -= 1

    def top(self) -> int:
        return self.s[-1] if len(self.s) else -1

    def getMin(self) -> int:
        while self.h[0] in self.f and self.f[self.h[0]] == 0:
            heapq.heappop(self.h)
        return self.h[0]
