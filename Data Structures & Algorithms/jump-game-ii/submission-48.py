class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i == len(nums) - 1:
                return 0

            if i >= len(nums):
                return float('inf')

            if i in cache:
                return cache[i]

            end = min(len(nums) - 1, nums[i] + i)
            if end == len(nums) - 1:
                return 1
            
            res = float('inf')
            for j in range(i + 1, end + 1):
                res = min(res, 1 + dfs(j))
            
            cache[i] = res
            return res
        
        return dfs(0)
            