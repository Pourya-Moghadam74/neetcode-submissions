class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i, cache):            
            if i in cache:
                return cache[i]
            
            if i == n:
                cache[i] = 1
                return 1
            if i > n:
                cache[i] = 0
                return 0
            
            count = 0
            count += dfs(i + 1, cache)
            count += dfs(i + 2, cache)
            cache[i] = count
            return count
        
        return dfs(0, {})