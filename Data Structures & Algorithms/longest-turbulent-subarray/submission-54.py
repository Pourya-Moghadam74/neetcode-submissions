class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ""
        l = 0
        r = 1
        res = 1

        while r < len(arr):
            if arr[r] > arr[r - 1] and prev != ">":
                prev = ">"
                res = max(res, r - l + 1)
                r += 1
            
            elif arr[r] < arr[r - 1] and prev != "<":
                prev = "<"
                res = max(res, r - l + 1)
                r += 1
            
            else:
                if arr[r - 1] == arr[r]:
                    l = r
                    r += 1
                
                else:
                    l = r - 1
                
                prev = ""
        
        return res