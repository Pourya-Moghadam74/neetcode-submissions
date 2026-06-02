class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, currSum):
            if (i, currSum) in cache:
                return cache[(i, currSum)]

            if i == len(nums):
                if currSum == target:
                    return 1
                return 0

            if i > len(nums):
                return 0
            
            cache[(i + 1, currSum + nums[i])] = dfs(i + 1, currSum + nums[i])
            cache[(i + 1, currSum - nums[i])] = dfs(i + 1, currSum - nums[i])

            return cache[(i + 1, currSum + nums[i])] + cache[(i + 1, currSum - nums[i])]

        return dfs(0, 0)