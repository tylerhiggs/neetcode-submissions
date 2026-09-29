class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [None for _ in range(n+1)]
        mem[0] = 1
        def help(i: int) -> int:
            if i < 0:
                return 0
            if mem[i] != None:
                return mem[i]
            mem[i] = help(i-1) + help(i-2)
            return mem[i]
        return help(n)