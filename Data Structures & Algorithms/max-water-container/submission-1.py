class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        i, j = 0, len(heights) - 1
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            best = max(best, area)
            if heights[i] < heights[j]:
                i += 1
                continue
            j -= 1
        return best