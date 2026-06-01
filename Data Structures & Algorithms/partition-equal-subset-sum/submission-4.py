class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        cache = {}

        def dfs(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            if totalSum - curSum == curSum:
                cache[(i, curSum)] = True
                return True
            
            if i >= len(nums):
                cache[(i, curSum)] = False
                return False
            
            cache[(i, curSum)] = dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum)
            return cache[(i, curSum)]
        
        
        return dfs(0, 0)