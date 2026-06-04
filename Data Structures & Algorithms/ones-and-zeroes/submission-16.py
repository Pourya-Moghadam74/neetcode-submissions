class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dfs(i, zeros, ones):
            if zeros > m or ones > n:
                return float("-inf")

            if i == len(strs):
                return 0

            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]

            z = strs[i].count("0")
            o = strs[i].count("1")

            take = 1 + dfs(i + 1, zeros + z, ones + o)
            skip = dfs(i + 1, zeros, ones)

            memo[(i, zeros, ones)] = max(take, skip)
            return memo[(i, zeros, ones)]

        return dfs(0, 0, 0)