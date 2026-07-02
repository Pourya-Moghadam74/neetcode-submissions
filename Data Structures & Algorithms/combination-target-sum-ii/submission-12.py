class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(i, curSum):
            if curSum == target:
                res.append(path[:])
                return
            
            if curSum > target or i >= len(candidates):
                return
            
            path.append(candidates[i])
            take = dfs(i + 1, curSum + candidates[i])

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            path.pop()
            skip = dfs(i + 1, curSum)
            
        dfs(0, 0)

        return res