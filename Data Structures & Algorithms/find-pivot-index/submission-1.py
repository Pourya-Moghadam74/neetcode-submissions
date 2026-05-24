class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        posfix = [0] * n

        total = 0
        for i in range(1, n):
            total += nums[i - 1]
            prefix[i] = total
        
        total = 0
        for i in range(n - 2, -1, -1):
            total += nums[i + 1]
            posfix[i] = total
        
        for i in range(n):
            if prefix[i] == posfix[i]:
                return i
        
        return -1