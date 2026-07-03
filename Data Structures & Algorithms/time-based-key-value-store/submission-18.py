class TimeMap:

    def __init__(self):
        self.arr = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key] = [(value, timestamp)]
        
        else:
            self.arr[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.arr:
            return ""

        l, r = 0, len(self.arr[key]) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            mid = self.arr[key][m]
            if timestamp == mid[1]:
                return mid[0]
            
            elif timestamp > mid[1]:
                res = mid[0]
                l = m + 1
            
            else:
                r = m - 1
        return res