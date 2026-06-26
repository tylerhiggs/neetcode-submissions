class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c not in d:
                stack.append(c)
                continue
            if not len(stack):
                return False
            open_c = stack.pop()
            if d[c] == open_c:
                continue
            return False
        return not len(stack)
