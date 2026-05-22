class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i == len(nums) - 1:
                return 0
            
            if i in cache:
                return cache[i]
            
            res = float('inf')
            for j in range(i + 1, min(len(nums), nums[i] + i + 1)):
                res = min(res, 1 + dfs(j))
            
            cache[i] = res
            return res

        return dfs(0)