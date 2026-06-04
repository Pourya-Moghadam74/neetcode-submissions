class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            if i == len(nums):
                return 1 if curSum == target else 0
            
            cache[(i, curSum)] = dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])
            return cache[(i, curSum)]

        return dfs(0, 0)