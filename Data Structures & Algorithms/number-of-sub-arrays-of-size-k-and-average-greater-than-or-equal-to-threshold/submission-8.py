class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        res = 0
        l = 0
        r = 0

        while r < len(arr):
            total += arr[r]

            if (r - l + 1) < k:
                r += 1
            
            elif (r - l + 1) > k:
                total -= arr[l]
                l += 1
            
            else:
                if total / k >= threshold:
                    res += 1

                r += 1
                total -= arr[l]
                l += 1
        
        return res