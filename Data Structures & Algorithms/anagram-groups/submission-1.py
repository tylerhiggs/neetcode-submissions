class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cs = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        def getKey(s: str):
            freq = {c: 0 for c in cs}
            for c in s:
                freq[c] += 1
            return tuple(freq[c] for c in cs)
        dic = {}
        for s in strs:
            key = getKey(s)
            if key in dic:
                dic[key].append(s)
                continue
            dic[key] = [s]
        return [dic[k] for k in dic]
        