class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        size1, size2 = len(s1), len(s2)
        counts1, counts2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        # no more counts1 modifications
        matches = 0
        for c in range(26):
            matches += (1 if counts1[c] == counts2[c] else 0)
        i = 0
        for j in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # add new element included on right of window
            index = ord(s2[j]) - ord('a')
            counts2[index] += 1
            if counts1[index] == counts2[index]:
                matches += 1
            elif counts1[index] + 1 == counts2[index]:
                matches -= 1
            # remove left element of window
            index = ord(s2[i]) - ord('a')
            counts2[index] -= 1
            if counts1[index] == counts2[index]:
                matches += 1
            elif counts1[index] == counts2[index] + 1:
                matches -= 1
            
            i += 1
            
            
                
        return matches == 26
            