class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        posfix = [1] * (n + 1)
        res = [0] * n

        for i in range(n):
            prefix[i + 1] = prefix[i] * nums[i]

        for i in range(n - 1, -1, -1):
            posfix[i - 1] = posfix[i] * nums[i]

        for i in range(n):
            res[i] = prefix[i] * posfix[i]
        

        return res
        
