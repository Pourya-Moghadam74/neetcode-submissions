class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        one = [0] * n
        one[-1] = 1
        res = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            tmp = digits[i] + one[i] + res[i + 1]
            res[i + 1] = tmp % 10
            res[i] += tmp // 10

        return res if res[0] != 0 else res[1:]