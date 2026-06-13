class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2
        cache = {}

        def dfs(i, curSum):
            if curSum > target:
                return float("-inf")
            
            if i == len(stones):
                return curSum
            
            if curSum == target:
                return curSum
            
            if i > len(stones):
                return float("-inf")
            
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            take = dfs(i + 1, curSum + stones[i])
            skip = dfs(i + 1, curSum)

            cache[(i, curSum)] = max(take, skip)
            return cache[(i, curSum)]
        
        ans = dfs(0, 0)

        return sum(stones) - 2 * ans

            
