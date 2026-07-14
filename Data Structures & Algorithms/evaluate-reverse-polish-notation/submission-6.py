class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = '+-*/'
        s = []
        for tok in tokens:
            if tok == '+':
                s[-2] = s[-2] + s[-1]
                s.pop()
                continue
            if tok == '-':
                s[-2] = s[-2] - s[-1]
                s.pop()
                continue
            if tok == '*':
                s[-2] = s[-2] * s[-1]
                s.pop()
                continue
            if tok == '/':
                s[-2] = int(float(s[-2]) / s[-1])
                s.pop()
                continue
            s.append(int(tok))
        print(s)
        return s[0]