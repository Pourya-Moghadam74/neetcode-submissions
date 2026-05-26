class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        values = { 0 : 1 }

        for num in nums:
            currSum += num
            diff = currSum - k

            res += values.get(diff, 0)
            
            values[currSum] = 1 + values.get(currSum, 0)
        
        return res