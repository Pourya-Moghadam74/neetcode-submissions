class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        total = sum(nums)

        totalSum = 0
        for i in range(len(nums)):
            if prefix[i] == total - prefix[i] - nums[i]:
                return i
            totalSum += nums[i]
            prefix[i + 1] = totalSum
        
        return -1