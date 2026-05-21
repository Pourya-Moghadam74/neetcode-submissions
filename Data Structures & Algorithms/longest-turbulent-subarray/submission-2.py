class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                if arr[r - 1] == arr[r]:
                    l = r
                    r = r + 1
                    prev = ""
                else:
                    if arr[r - 1] > arr[r]:
                        prev = ">"
                    else:
                        prev = "<"
                    l = r - 1
                    r = r + 1

        return res
                