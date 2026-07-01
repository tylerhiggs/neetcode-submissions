class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest_from_i = []
        biggest = -float("inf")
        for p in prices[::-1]:
            largest_from_i.append(max(biggest, p))
            biggest = largest_from_i[-1]
        res = 0
        for i in range(len(prices)):
            res = max(res, largest_from_i[-i - 1] - prices[i])
        return res
