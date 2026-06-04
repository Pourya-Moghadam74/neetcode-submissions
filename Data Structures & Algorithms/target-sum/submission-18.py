class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, curSum):
            if i == len(nums):
                return 1 if curSum == target else 0
            
            
            add = dfs(i + 1, curSum + nums[i])
            sub = dfs(i + 1, curSum - nums[i])

            return add + sub
        
        return dfs(0, 0)