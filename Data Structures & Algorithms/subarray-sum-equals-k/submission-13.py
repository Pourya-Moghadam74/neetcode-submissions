class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        count = {0: 1}
        res = 0

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
            diff = prefix[i + 1] - k

            if diff in count:
                res += count[diff]
            
            count[prefix[i + 1]] = 1 + count.get(prefix[i + 1], 0)
        

        return res