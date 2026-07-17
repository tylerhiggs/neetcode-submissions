class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(enumerate(position), key=lambda x:x[1]) # [(old_idx, val)]
        times = [(target - pos[1]) / speed[pos[0]] for pos in ps] # speed = distance / time -> time = distance / speed
        s = []
        # times: [3,4,5,2,3,2,1,6]
        for time in times:
            while len(s) and time >= s[-1]:
                s.pop()
            s.append(time)
        return len(s)
        
