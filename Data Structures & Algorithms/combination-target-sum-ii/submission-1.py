class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def backtrack(i: int, current: List[int], total=0):
            if total == target:
                res.add(tuple(current))
                return
            if total > target or i == len(candidates):
                return
            current.append(candidates[i])
            backtrack(i+1, current, candidates[i] + total)
            current.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i + 1, current, total)
        backtrack(0, [])
        return [list(item) for item in res]