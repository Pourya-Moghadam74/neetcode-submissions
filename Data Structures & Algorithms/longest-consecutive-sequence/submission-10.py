class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        if len(nums) == 0:
            return 0
            
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        res = 1
        
        for num in nums:
            if num - 1 not in count and num + 1 in count:
                tmp = 1
                while (num + 1) in count:
                    num = num + 1
                    tmp += 1
            
                res = max(res, tmp)

        return res