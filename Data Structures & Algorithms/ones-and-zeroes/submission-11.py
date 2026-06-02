class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}

        def dfs(i, zeroCount, oneCount):
            if (i, zeroCount, oneCount) in cache:
                return cache[(i, zeroCount, oneCount)]

            if zeroCount > m or oneCount > n:
                return float("-inf")
            
            if i >= len(strs):
                return 0

            take = 1 + dfs(i + 1, zeroCount + strs[i].count("0"), oneCount + strs[i].count("1"))
            skip = dfs(i + 1, zeroCount, oneCount)
            cache[(i, zeroCount, oneCount)] = max(take, skip)

            return cache[(i, zeroCount, oneCount)]
        
        return dfs(0, 0, 0)

