class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0,0)] #(dist, index)
        visited = set()
        res = 0
        
        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        while len(visited) < len(points):
            dist, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            res += dist

            for j in range(len(points)):
                if j not in visited:
                    heapq.heappush(heap, (manhattan(i, j), j))
        
        return res