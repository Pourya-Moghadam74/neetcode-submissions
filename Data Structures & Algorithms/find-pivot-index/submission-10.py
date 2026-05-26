class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        n = len(nums)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        print(prefix)
        for i in range(0, len(nums)):
            lefSum = prefix[i]
            rightSum = prefix[n] - prefix[i] - nums[i]
            if lefSum == rightSum:
                return i
        
        return -1