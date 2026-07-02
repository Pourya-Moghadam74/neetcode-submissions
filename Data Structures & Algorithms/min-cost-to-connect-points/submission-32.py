class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)]

        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        res = 0
        visited = set()
        while len(visited) < len(points):
            d, n = heapq.heappop(heap)

            if n in visited:
                continue
            
            visited.add(n)
            res += d

            for j in range(len(points)):
                if j not in visited:
                    heapq.heappush(heap, (manhattan(n, j), j))
            
        
        return res

