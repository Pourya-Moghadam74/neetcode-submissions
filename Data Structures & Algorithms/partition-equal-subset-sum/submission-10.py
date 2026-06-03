class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        n = len(nums)
        cache = {}

        def dfs(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            if 2 * curSum == totalSum:
                cache[i, curSum] = True
                return True

            if i >= n:
                return False
            
            take = dfs(i + 1, curSum + nums[i])
            skip = dfs(i + 1, curSum)
            cache[(i, curSum)] = take or skip
            return take or skip
        
        return dfs(0, 0)
