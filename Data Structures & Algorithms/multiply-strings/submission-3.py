class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res1 = 0
        n1 = len(num1)
        for i in range(n1 - 1, -1, -1):
            res1 += (10 ** (n1 - 1 - i)) * (ord(num1[i]) - ord("0"))
        
        res2 = 0
        n2 = len(num2)
        for j in range(n2 - 1, -1, -1):
            res2 += (10 ** (n2 - 1 - j)) * (ord(num2[j]) - ord("0"))
        
        return str(res1 * res2)