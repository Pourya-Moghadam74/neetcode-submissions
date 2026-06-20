class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            
            if i in cache:
                return cache[i]

            end = min(len(nums) - 1, nums[i] + i)
            
            if end == len(nums) - 1:
                cache[i] = True
                return True
            
            for j in range(i + 1, end + 1):
                if dfs(j):
                    cache[i] = True
                    return True
            cache[i] = False
            return False
        
        return dfs(0)