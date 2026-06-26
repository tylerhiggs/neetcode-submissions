class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]
        for i in range(1, len(tokens)):
            if tokens[i] not in '+-*/':
                stack.append(int(tokens[i]))
                continue
            prev = stack.pop()
            if tokens[i] == '+':
                stack[-1] += prev
                continue
            if tokens[i] == '-':
                stack[-1] -= prev
                continue
            if tokens[i] == '*':
                stack[-1] *= prev
                continue
            if tokens[i] == '/':
                stack_neg = stack[-1] < 0
                stack[-1] = abs(stack[-1]) // abs(prev)
                stack[-1] *= -1 if prev < 0 else 1
                stack[-1] *= -1 if stack_neg else 1
                continue
        print(stack)
        return stack[0]