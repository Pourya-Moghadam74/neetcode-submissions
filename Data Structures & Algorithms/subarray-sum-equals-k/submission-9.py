class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        values = { 0 : 1 }
        res = 0

        total = 0
        for i in range(len(nums)):
            total += nums[i]
            dif = total - k

            if dif in values:
                res += values[dif]
            
            values[total] = 1 + values.get(total, 0)

        return res