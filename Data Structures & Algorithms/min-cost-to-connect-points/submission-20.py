class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(a, b):
            return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])
        
        visited = set()
        n = len(points)
        minHeap = [(0, 0)]
        res = 0

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            res += cost

            for i in range(n):
                if i not in visited:
                    heapq.heappush(minHeap, (manhattan(node, i), i))
            
        return res