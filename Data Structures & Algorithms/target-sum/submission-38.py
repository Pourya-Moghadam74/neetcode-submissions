class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            pos = dfs(i + 1, curSum + nums[i])
            neg = dfs(i + 1, curSum - nums[i])
            cache[(i, curSum)] = pos + neg
            return pos + neg

        return dfs(0, 0)

         