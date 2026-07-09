class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for p in points:
            dist = (p[0] ** 2) + (p[1] ** 2)
            heapq.heappush_max(maxHeap, (dist, p))
            while len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        
        res = []
        for p in maxHeap:
            res.append(p[1])
        
        return res