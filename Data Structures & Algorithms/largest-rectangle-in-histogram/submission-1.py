class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_smallest_right = [n for _ in range(n)]
        next_smallest_left = [-1 for _ in range(n)]
        s = []
        for i in range(n):
            while len(s) and heights[i] <= heights[s[-1]]:
                s.pop()
            if len(s):
                next_smallest_left[i] = s[-1]
            s.append(i)
        s = []
        for i in range(n-1, -1, -1):
            while len(s) and heights[i] <= heights[s[-1]]:
                s.pop()
            if len(s):
                next_smallest_right[i] = s[-1]
            s.append(i)
        best = 0
        for i in range(n):
            best = max(best, heights[i] * (next_smallest_right[i] - 1 - next_smallest_left[i] - 1 + 1))
        return best
