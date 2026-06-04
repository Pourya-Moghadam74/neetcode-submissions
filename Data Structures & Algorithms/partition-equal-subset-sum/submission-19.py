class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2:
            return False
        
        target = totalSum // 2

        def dfs(i, curSum):
            if curSum == target:
                return True
            
            if i >= len(nums):
                return False
            
            return dfs(i + 1, curSum + nums[i]) or dfs(i + 1, curSum)
        
        return dfs(0, 0)