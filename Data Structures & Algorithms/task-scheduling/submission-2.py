class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f = {task: 0 for task in tasks}
        no_ops = 0
        for task in tasks:
            f[task] += 1
        h = []
        for task in f:
            h.append([-f[task], task])
        heapq.heapify(h)
        while h:
            used = []
            for i in range(n + 1):
                if not used and not h:
                    break
                if not h:
                    no_ops += n + 1 - i
                    break
                used.append(heapq.heappop(h))
                used[-1][0] += 1
                if not used[-1][0]:
                    used.pop()
            for task in used:
                heapq.heappush(h, task)

        return len(tasks) + no_ops