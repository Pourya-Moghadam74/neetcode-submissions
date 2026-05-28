class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        values = { 0 : 1 }
        n = len(nums)
        prefix = [0] * (n + 1)
        total = 0
        res = 0

        for i in range(n):
            total += nums[i]
            prefix[i + 1] = total
            diff = prefix[i + 1] - k

            if diff in values:
                res += values[diff]
            
            values[total] = 1 + values.get(total, 0)
        
        return res
