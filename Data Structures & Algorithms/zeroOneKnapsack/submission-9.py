class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}

        def dfs(i, capacity):
            if (i, capacity) in cache:
                return cache[(i, capacity)]

            if i == len(profit):
                cache[(i, capacity)] = 0
                return 0
            
            if capacity < 0:
                cache[(i, capacity)] = 0
                return 0
            
            skip = dfs(i + 1, capacity)
            include = 0
            if capacity >= weight[i]:
                include = profit[i] + dfs(i + 1, capacity - weight[i])

            cache[(i, capacity)] = max(skip, include)
            return cache[(i, capacity)]
        
        return dfs(0, capacity)
