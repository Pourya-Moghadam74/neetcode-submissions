class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}

        def dfs(i, curWeight):
            if curWeight > capacity:
                return float("-inf")
            
            if i >= len(profit):
                return 0

            if (i, curWeight) in cache:
                return cache[(i, curWeight)]

            take = profit[i] + dfs(i + 1, curWeight + weight[i])
            skip = dfs(i + 1, curWeight)
            cache[(i, curWeight)] = max(take, skip)
            return cache[(i, curWeight)]
        
        return dfs(0, 0)
