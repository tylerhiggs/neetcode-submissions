class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mi, ma = 1, max(piles)
        res = ma
        while mi <= ma:
            mid = (mi + ma) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / mid)
            if hours > h:
                mi = mid + 1
            if hours <= h:
                ma = mid - 1
                res = mid
        return res