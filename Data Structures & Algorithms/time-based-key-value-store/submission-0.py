class TimeMap:

    def __init__(self):
        self.d = {} # key -> [value, timestamp][]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((value, timestamp))
            return
        self.d[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        values = self.d[key]
        i, j = 0, len(values) - 1
        if values[-1][1] <= timestamp:
            return values[-1][0]
        while i <= j:
            mid = (i + j) // 2
            if values[mid][1] < timestamp:
                if mid + 1 < len(values) and values[mid + 1][1] > timestamp:
                    return values[mid][0]
                i = mid + 1
                continue
            if timestamp < values[mid][1]:
                j = mid - 1
                continue
            return values[mid][0]
        return ""
