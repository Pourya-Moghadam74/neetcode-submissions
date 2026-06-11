class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        res = 1
        prev = ""

        for r in range(1, len(arr)):
            if arr[r] > arr[r - 1] and prev != ">":
                prev = ">"
            
            elif arr[r] < arr[r - 1] and prev != "<":
                prev = "<"
            
            else:
                if arr[r] == arr[r - 1]:
                    l = r
                    prev = ""
                else:
                    l = r - 1
                    prev = "<" if arr[r] < arr[r - 1] else ">"
            
            res = max(res, r - l + 1)
        
        return res
            