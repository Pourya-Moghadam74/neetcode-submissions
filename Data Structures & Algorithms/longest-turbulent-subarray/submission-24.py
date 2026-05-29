class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ""
        res = 1
        l, r = 0, 0
        
        while r < len(arr) - 1:
            if arr[r] < arr[r + 1] and prev != "<":
                r += 1
                prev = "<"
            
            elif arr[r] > arr[r + 1] and prev != ">":
                r += 1
                prev = ">"
            
            else:
                if arr[r] == arr[r + 1]:
                    l = r + 1
                    r += 1
                else:
                    l = r
                    r + 1
                
                prev = ""
            
            res = max(res, r - l + 1)
        
        return res