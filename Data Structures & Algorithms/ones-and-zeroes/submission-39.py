class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}

        def dfs(i, ones, zeros):
            if ones > m or zeros > n:
                return float("-inf")
            
            if i >= len(strs):
                return 0

            if (i, ones, zeros) in cache:
                return cache[(i, ones, zeros)]

            oCount = strs[i].count("0")
            zCount = strs[i].count("1")

            take = 1 + dfs(i + 1, ones + oCount, zeros + zCount)
            skip = dfs(i + 1, ones, zeros)
            cache[(i, ones, zeros)] = max(take, skip)

            return cache[(i, ones, zeros)]

        return dfs(0, 0, 0)