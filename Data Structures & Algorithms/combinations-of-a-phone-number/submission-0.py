class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        nums = [int(c) for c in digits]
        res = []
        letters = [None, None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        def help(current=[], i=0):
            if i == len(nums):
                res.append("".join(current))
                return
            for c in letters[nums[i]]:
                current.append(c)
                help(current, i+1)
                current.pop()
        help()
        return res
            