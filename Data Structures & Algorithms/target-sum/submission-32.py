class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            if i >= len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            
            add = dfs(i + 1, curSum + nums[i])
            sub = dfs(i + 1, curSum - nums[i])
            cache[(i, curSum)] = add + sub
            return add + sub
        
        return dfs(0, 0)
