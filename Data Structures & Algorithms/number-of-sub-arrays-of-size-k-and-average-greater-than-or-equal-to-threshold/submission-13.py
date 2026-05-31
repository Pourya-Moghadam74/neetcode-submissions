class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefix = [0] * (len(arr) + 1)
        total = 0

        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] + arr[i]
        
        r = k - 1
        res = 0
        while r < len(arr):
            if prefix[r + 1] - prefix[r - k + 1] >= threshold * k:
                res += 1
            
            r += 1

        return res
        

