class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s_pos = sorted(enumerate(position), key=lambda x:x[1])
        finish_times = [(target - s_pos[i][1]) / speed[s_pos[i][0]] for i in range(len(speed))]
        # 1, 2, 3, 4, 1
        # 4, 3, 2, 1, 3
        current_max = -float('inf')
        res = 0
        for t in finish_times[::-1]:
            if t <= current_max:
                continue
            current_max = t
            res += 1
        return res
                
