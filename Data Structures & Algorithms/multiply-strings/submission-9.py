class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"

        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n2 - 1, -1, -1):
            for j in range(n1 - 1, -1, -1):
                position = i + j + 1
                tmp = res[position] + (int(num2[i]) * int(num1[j]))
                res[position] = tmp % 10
                res[position - 1] += tmp // 10
        
        res = "".join(map(str, res))
        return res.lstrip("0")