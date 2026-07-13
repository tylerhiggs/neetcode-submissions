class Solution:
    def isValid(self, s: str) -> bool:
        d = { '}': '{', ')': '(', ']': '[' }
        stack = []
        for c in s:
            if c in d:
                if not len(stack) or d[c] != stack[-1]:
                    return False
                stack.pop()
                continue
            stack.append(c)
        return len(stack) == 0
