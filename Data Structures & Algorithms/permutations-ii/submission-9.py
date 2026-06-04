class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        res = []
        path = []
        for num in nums:
            count[num] += 1
        
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    dfs()
                    path.pop()
                    count[num] += 1
            
        dfs()

        return res
