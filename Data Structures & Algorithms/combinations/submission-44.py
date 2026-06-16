class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            if i > n:
                return
            
            for j in range(i, n + 1):
                comb.append(j)
                dfs(j + 1, comb)
                comb.pop()
            
        dfs(1, [])

        return res