class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")

        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                res = max(res, product)
        
        return res