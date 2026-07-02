class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            dist = (p[0] ** 2) + (p[1] ** 2)
            heap.append((dist, p))
        
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res