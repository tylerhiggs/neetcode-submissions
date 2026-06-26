class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        c_to_i = {c: i for (i, c) in enumerate('abcdefghijklmnopqrstuvwxyz')}
        for s in strs:
            t = [0 for _ in range(26)]
            for c in s:
                t[c_to_i[c]] += 1
            if tuple(t) in d:
                d[tuple(t)].append(s)
                continue
            d[tuple(t)] = [s]
        return [d[key] for key in d]