class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        best = 1
        i = 0
        win = set()
        for j in range(len(s)):
            if s[j] in win:
                while s[i] != s[j]:
                    if s[i] not in win:
                        print(list(win))
                        print(s, i, j, best)
                    win.remove(s[i])
                    i += 1
                i += 1
            win.add(s[j])
            best = max(best, j - i + 1)
        return best