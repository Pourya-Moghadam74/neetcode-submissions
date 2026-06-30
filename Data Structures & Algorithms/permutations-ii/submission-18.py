class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num , 0)
        
        res = []
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    path.pop()
            
        
        dfs()

        return res