class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rows = len(coins)
        cols = amount + 1

        dp = [[float("inf")] * cols for _ in range(rows)]

        for r in range(rows):
            dp[r][0] = 0

        for c in range(1, cols):
            if c >= coins[0]:
                dp[0][c] = 1 + dp[0][c - coins[0]]

        for r in range(1, rows):
            for c in range(1, cols):
                skip = dp[r - 1][c]

                take = float("inf")
                if c >= coins[r]:
                    take = 1 + dp[r][c - coins[r]]

                dp[r][c] = min(skip, take)

        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1