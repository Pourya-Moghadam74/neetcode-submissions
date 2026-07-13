class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        visited = set()
        heap = [(0, 0)] #dist, i
        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        while len(visited) < len(points):
            d, n = heapq.heappop(heap)
            if n in visited:
                continue
                
            total += d
            visited.add(n)

            for i in range(len(points)):
                if i in visited:
                    continue
                
                heapq.heappush(heap, (manhattan(n, i), i))
        
        return total

