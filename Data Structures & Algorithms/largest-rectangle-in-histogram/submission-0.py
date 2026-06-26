class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        left_most = [-1] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_most[i] = stack[-1]
            stack.append(i)
        stack = []
        right_most = [len(heights)] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_most[i] = stack[-1]
            stack.append(i)
        best = 0
        for i in range(len(heights)):
            width = right_most[i] - left_most[i] - 1
            best = max(best, width * heights[i])
        return best

        