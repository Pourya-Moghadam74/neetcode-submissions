class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        cache = {}
        
        def dfs(i, curSum):
            if curSum == target:
                return True
            
            if curSum > target or i >= len(nums):
                return False
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            take = dfs(i + 1, curSum + nums[i])
            skip = dfs(i + 1, curSum)

            cache[(i, curSum)] = take or skip
            return take or skip
        
        return dfs(0, 0)