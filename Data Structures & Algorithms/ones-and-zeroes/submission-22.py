class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}

        def dfs(i, zerosCount, onesCount, curLen):
            if zerosCount > m or onesCount > n:
                return float("-inf")

            if i == len(strs):
                return curLen

            if (i, zerosCount, onesCount, curLen) in cache:
                return cache[(i, zerosCount, onesCount, curLen)]

            tmpZero = strs[i].count("0")
            tmpOne = strs[i].count("1")

            take = dfs(i + 1, zerosCount + tmpZero, onesCount + tmpOne, curLen + 1)
            skip = dfs(i + 1, zerosCount, onesCount, curLen)

            cache[(i, zerosCount, onesCount, curLen)] = max(take, skip)
            return cache[(i, zerosCount, onesCount, curLen)]

        return dfs(0, 0, 0, 0)