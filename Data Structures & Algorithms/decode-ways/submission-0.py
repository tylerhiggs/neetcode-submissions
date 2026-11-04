class Solution:
    def numDecodings(self, s: str) -> int:
        numsToLetters = { f"{i+1}": chr(ord('A') + i) for i in range(26)}
        mem = [None for _ in s]
        if not s:
            return 0
        def help(i: int) -> int:
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if mem[i] != None:
                return mem[i]
            mem[i] = 0
            if s[i] in numsToLetters:
                mem[i] += help(i + 1)
            if s[i:i+2] in numsToLetters:
                mem[i] += help(i + 2)
            return mem[i]
        return help(0)
            