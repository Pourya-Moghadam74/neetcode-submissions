class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        if not nums:
            return 0
        for n in nums:
            if n - 1 not in count:
                start = n
                while n + 1 in count:
                    n += 1
                res = max(res, n - start + 1)
        
        return res