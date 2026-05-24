class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        count = {0: 1}
        res = 0

        for num in nums:
            currSum += num
            diff = currSum - k

            if diff in count:
                res += count[diff]
            
            count[currSum] = 1 + count.get(currSum, 0)
        
        return res
        
