class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        cache = {}

        def dfs(i, curSum):
            if curSum > target:
                return False
            
            if curSum == target:
                return True
            
            if i >= len(nums):
                return False
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            take = dfs(i + 1, curSum + nums[i])
            skip = dfs(i + 1, curSum)
            cache[(i, curSum)] = take or skip
            
            return cache[(i, curSum)]
        
        return dfs(0, 0)