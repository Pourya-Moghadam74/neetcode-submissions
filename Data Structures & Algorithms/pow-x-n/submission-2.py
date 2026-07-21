class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            res *= x
        
        print(res)
        if n < 0:
            return 1 / res
        
        if n == 0:
            return 1
        
        if n > 0:
            return res