class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        best = 0
    
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            best = max(best, area)

            if heights[i] > heights[j]:
                j -= 1
                continue
            i += 1
        return best