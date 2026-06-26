class Solution:
    def trap(self, height: List[int]) -> int:
        lr = []
        rl = []

        tallest_yet = 0
        for h in height:
            tallest_yet = max(tallest_yet, h)
            lr.append(tallest_yet - h)
        tallest_yet = 0
        for h in height[::-1]:
            tallest_yet = max(tallest_yet, h)
            rl.append(tallest_yet - h)
        return sum([min(lr[i], rl[len(height)-i-1]) for i in range(len(height))])
            