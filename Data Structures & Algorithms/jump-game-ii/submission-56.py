class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if i in cache:
                return cache[i]

            end = min(len(nums) - 1, nums[i] + i)
            res = float("inf")
            for j in range(i + 1, end + 1):
                res = min(res, dfs(j))
            
            cache[i] = res + 1
            return cache[i]

        return dfs(0)