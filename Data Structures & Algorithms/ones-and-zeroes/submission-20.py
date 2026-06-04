class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}

        def dfs(i, zerosCount, onesCount):
            if zerosCount > m or onesCount > n:
                return float("-inf")

            if i == len(strs):
                return 0

            if (i, zerosCount, onesCount) in cache:
                return cache[(i, zerosCount, onesCount)]

            tmpZero = strs[i].count("0")
            tmpOne = strs[i].count("1")

            take = 1 + dfs(i + 1, zerosCount + tmpZero, onesCount + tmpOne)
            skip = dfs(i + 1, zerosCount, onesCount)

            cache[(i, zerosCount, onesCount)] = max(take, skip)
            return cache[(i, zerosCount, onesCount)]

        return dfs(0, 0, 0)