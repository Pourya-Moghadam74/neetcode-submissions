class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        total = 0
        visited = set()
        minH = [(0, 0)]

        while len(visited) != len(points):
            d, n = heapq.heappop(minH)
            
            if n in visited:
                continue
            
            visited.add(n)
            total += d

            for p in range(len(points)):
                if p not in visited:
                    heapq.heappush(minH, (manhattan(n, p), p))
            
        return total



