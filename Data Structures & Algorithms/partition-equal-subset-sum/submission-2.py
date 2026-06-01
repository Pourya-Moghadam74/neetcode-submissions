class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        def dfs(i, curSum):
            if totalSum - curSum == curSum:
                return True
            
            if i >= len(nums):
                return False
            
            return dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum)
        
        
        return dfs(0, 0)