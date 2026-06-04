class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        res = []
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -= 1
                    dfs()
                    count[num] += 1
                    perm.pop()
                
        
        dfs()

        return res

