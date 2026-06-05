class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)
        target = totalSum // 2
        cache = {}

        def dfs(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            if curSum > target:
                return 0

            if i >= len(stones):
                return curSum

            skip = dfs(i + 1, curSum)
            take = dfs(i + 1, curSum + stones[i])
            cache[(i, curSum)] = max(take, skip)
            return cache[(i, curSum)]
        
        return totalSum - 2 * dfs(0, 0)