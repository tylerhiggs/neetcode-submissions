class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m, n = max(piles), len(piles)
        '''
        You can never go to another pile in the same hour,
        so at very best, you can do 1 pile per hour, meaning
        `m` is upper bound for `k`
        '''
        i, j = 1, m # inclusive lower and upper bound on `k`
        while i < j:
            k = (i + j) // 2
            # if k == j:
            #     return i + 
            total = sum([math.ceil(float(b) / k) for b in piles])
            if total <= h:
                j = k
                continue
            i = k + 1
        return j