class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        n = len(arr)
        prev = ""
        l = 0
        r = 1

        while r < n:
            if arr[r] > arr[r - 1] and prev != ">":
                r += 1
                prev = ">"
            
            elif arr[r] < arr[r - 1] and prev != "<":
                r += 1
                prev = "<"
            
            else:
                if arr[r] == arr[r - 1]:
                    l = r
                    r += 1
                else:
                    l = r - 1

                prev = ""
            
            res = max(res, r - l)

        return res      


            
