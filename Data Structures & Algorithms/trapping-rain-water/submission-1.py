class Solution:
    def trap(self, height: List[int]) -> int:
        ltr = []
        top = 0
        for h in height:
            top = max(top, h)
            ltr.append(top - h)
        top = 0
        rtl = []
        for h in height[::-1]:
            top = max(top, h)
            rtl.append(top - h)
        return sum([min(ltr[i], rtl[-i - 1]) for i in range(len(height))])
