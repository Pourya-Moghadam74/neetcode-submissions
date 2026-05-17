class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x != y:
                tmp = abs(x - y)
                heapq.heappush_max(stones, tmp)
            
        if stones:
            return stones[0]
        else:
            return 0