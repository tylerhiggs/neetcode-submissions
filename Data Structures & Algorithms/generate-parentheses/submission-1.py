class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def help(current: List[str], opens=0, closes=0):
            if len(current) == 2 * n:
                res.append("".join(current))
                return
            if opens < n:
                current.append('(')
                help(current, opens + 1, closes)
                current.pop()
            if closes < opens:
                current.append(')')
                help(current, opens, closes + 1)
                current.pop()
        help([])
        return res