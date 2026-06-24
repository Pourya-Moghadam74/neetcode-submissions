class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        l, r = 0, 1
        prev = ""
        if len(arr) == 1:
            return 1
            
        while r < len(arr):

            if arr[r] > arr[r - 1] and prev != ">":
                prev = ">"
                r += 1
            
            elif arr[r] < arr[r - 1] and prev != "<":
                prev = "<"
                r += 1
            
            else:
                if arr[r] == arr[r - 1]:
                    l = r
                    r = r + 1
                else:
                    l = r - 1
                prev = ""

            res = max(res, r - l)
        
        return res
