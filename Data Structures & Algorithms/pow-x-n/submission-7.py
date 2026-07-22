class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dfs(x, n):
            if n == 0:
                return 1
            
            if x == 0:
                return 0
            
            if n % 2 == 0:
                res = dfs(x, n // 2)
                return res ** 2
            
            else:
                res = dfs(x, n // 2)
                return x * (res ** 2)
            
        
        res = dfs(x, abs(n))
        if n < 0:
            return 1 / res
        
        return res