class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        def dfs(i):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in count:
                if count[num] > 0:
                    count[num] -= 1
                    path.append(num)
                    dfs(i + 1)
                    path.pop()
                    count[num] += 1
        
        dfs(0)

        return res