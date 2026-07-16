class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = []

        for n in nums:
            heapq.heappush(minH, n)
            while len(minH) > k:
                heapq.heappop(minH)
        
        return minH[0]