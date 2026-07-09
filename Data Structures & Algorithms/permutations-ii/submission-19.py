class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        path = []

        def dfs(i):
            if i >= len(nums):
                res.append(path[:])
                return
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    path.append(n)
                    dfs(i + 1)
                    count[n] += 1
                    path.pop()
            
        dfs(0)

        return res