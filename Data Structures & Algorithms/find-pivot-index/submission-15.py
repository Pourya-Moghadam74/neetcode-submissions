class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        sumsum = sum(nums)

        total = 0
        for i in range(n):
            total += nums[i]
            prefix[i + 1] = total

            if sumsum - prefix[i] - nums[i] == prefix[i]:
                return i
            
        return -1