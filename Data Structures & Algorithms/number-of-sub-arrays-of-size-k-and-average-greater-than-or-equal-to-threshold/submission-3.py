class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        r = 0
        count = 0

        for l in range(len(arr)):
            if r == len(arr):
                break
                
            while r - l < k:
                total += arr[r]
                r += 1
            
            average = total / k
            if average >= threshold:
                count += 1

            total -= arr[l]
            

        return count
                
