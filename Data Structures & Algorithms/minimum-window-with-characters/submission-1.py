class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, s_count, t_set = [0] * 58, [0] * 58, set()
        for c in t:
            t_set.add(c)
            t_count[ord(c) - ord('A')] += 1
        i, j = 0, 0
        best = float('inf')
        best_win = (0, 0)
        while j <= len(s):
            valid = True
            for c in t_set:
                valid = valid and s_count[ord(c) - ord('A')] >= t_count[ord(c) - ord('A')]
            if valid:
                # record and remove ith char
                if j - i < best:
                    best = j - i
                    best_win = (i, j)
                s_count[ord(s[i]) - ord('A')] -= 1
                i += 1
                continue
            # extend window
            if j < len(s):
                s_count[ord(s[j]) - ord('A')] += 1
            j += 1
        return s[best_win[0]:best_win[1]]

        