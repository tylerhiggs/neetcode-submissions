class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest_yet = float('inf')
        best = 0
        for p in prices:
            smallest_yet = min(smallest_yet, p)
            best = max(best, p - smallest_yet)
        return best

                