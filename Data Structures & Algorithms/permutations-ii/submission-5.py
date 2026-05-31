class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        def dfs(comb):
            if len(comb) == len(nums):
                res.append(comb[:])
                return
            
            for num in count:
                if count[num] > 0:
                    comb.append(num)
                    count[num] -= 1
                    dfs(comb)
                    comb.pop()
                    count[num] += 1
        
        dfs([])

        return res