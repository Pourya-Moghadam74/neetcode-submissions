class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        l, r = 0, 1
        prev = ""

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != "<":
                prev = "<"
                r += 1
            
            elif arr[r - 1] > arr[r] and prev != ">":
                prev = ">"
                r += 1
            
            else:
                if arr[r - 1] == arr[r]:
                    l = r
                    r += 1
                else:
                    l = r - 1

                prev = ""

            res = max(res, r - l)
        return res