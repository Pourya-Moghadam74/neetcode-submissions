class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = {}
        res = 0

        for i in range(len(nums)):
            values[nums[i]] = 1
        
        for num in nums:
            if num - 1 not in values:
                tmp = 1
                while num + 1 in values:
                    tmp += 1
                    num = num + 1
                
                res = max(res, tmp)
            


        return res
            
            

