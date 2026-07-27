class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((value, timestamp))
            return
        self.d[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        l = self.d.get(key, [])
        if not l:
            return ""
        i, j = 0, len(l) - 1 # inclusive
        while i < j:
            if l[i][1] > timestamp:
                return l[i-1][0] if i > 0 else ""
            mid = (i + j) // 2
            if l[mid][1] == timestamp:
                return l[mid][0]
            if l[mid][1] < timestamp:
                i = mid + 1
                continue
            j = mid - 1
        return l[i][0] if l[i][1] <= timestamp else l[i-1][0] if i > 0 else ""
