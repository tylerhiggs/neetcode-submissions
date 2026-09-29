class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mem = [None for _ in range(n)]
        def what_cost(i=0) -> int:
            if i >= len(cost):
                return 0
            if mem[i] != None:
                return mem[i]
            mem[i] = min(what_cost(i + 1), what_cost(i + 2)) + cost[i]
            return mem[i]
        return min(what_cost(), what_cost(1))
            