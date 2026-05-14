class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = {}
        res = 0

        for item in nums:
            values[item] = 1
        

        for item in nums:
            if item - 1 not in values:
                tmp = 1
                while item + 1 in values:
                    tmp += 1
                    item = item + 1
                
                res = max(res, tmp)
        
        return res