class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dfs(i):
            if i == n:
                return 1
            
            if i > n:
                return 0
            
            if i in cache:
                return cache[i]
            
            count = 0
            count += dfs(i + 1)
            count += dfs(i + 2)
            cache[i] = count
            
            return count
        
        return dfs(0)
            