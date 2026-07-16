class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0 for _ in temperatures]
        for j in range(len(temperatures)):
            while len(s) and temperatures[j] > temperatures[s[-1]]:
                res[s[-1]] = j - s[-1]
                s.pop()
            s.append(j)
        return res