class TimeMap:

    def __init__(self):
        self.arr = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key] = [(value, timestamp)]
        else:
            self.arr[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.arr:
            return res
        
        values = self.arr[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] == timestamp:
                return values[m][0]
            
            elif values[m][1] > timestamp:
                r = m - 1
            
            else:
                res = values[m][0]
                l = m + 1
        
        return res
