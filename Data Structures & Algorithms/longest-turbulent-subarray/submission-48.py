class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 0
        res = 1
        prev = ""

        while r < len(arr) - 1:
            if arr[r] < arr[r + 1] and prev != "<":
                prev = "<"
                r += 1
            
            elif arr[r] > arr[r + 1] and prev != ">":
                prev = ">"
                r += 1

            else:
                if arr[r] == arr[r + 1]:
                    l = r + 1
                    r += 1
                else:
                    l = r
                prev = ""

            res = max(res, r - l + 1)

        return res