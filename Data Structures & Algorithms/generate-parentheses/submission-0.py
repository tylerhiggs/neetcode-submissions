class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current = []
        
        def x(o, c):
            if o == c == n:
                res.append(''.join(current))
                return
            if o < n:
                current.append('(')
                x(o+1, c)
                current.pop()
            if c < o:
                current.append(')')
                x(o, c+1)
                current.pop()
        x(0, 0)
        return res