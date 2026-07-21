class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in (num1, num2):
            return "0"
        
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
            digit1 = ord(num1[i]) - ord("0")

            for j in range(n2 - 1, -1, -1):
                digit2 = ord(num2[j]) - ord("0")

                position = i + j + 1
                total = res[position] + (digit1 * digit2)
                res[position] = total % 10
                res[position - 1] += total // 10
        
        prod = "".join(map(str, res))
        return prod.lstrip("0")