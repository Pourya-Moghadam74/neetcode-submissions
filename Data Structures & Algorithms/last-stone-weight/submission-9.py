class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH = stones
        heapq.heapify_max(maxH)

        while len(maxH) >= 2:
            a, b = heapq.heappop_max(maxH), heapq.heappop_max(maxH)
            diff = a - b

            if diff:
                heapq.heappush_max(maxH, diff)
        

        if maxH:
            return maxH[0]
        
        return 0