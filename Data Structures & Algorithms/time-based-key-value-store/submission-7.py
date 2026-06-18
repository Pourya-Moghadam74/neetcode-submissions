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
        
        value = self.arr[key]
        l, r = 0, len(value) - 1

        while l <= r:
            m = (l + r) // 2
            if value[m][1] == timestamp:
                return value[m][0]
            
            elif value[m][1] > timestamp:
                r = m - 1
            
            else:
                res = value[m][0]
                l = m + 1
        
        return res
        
