class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        totalCost = 0
        visited = {}
        minHeap = [[0, 0]] #cost, i

        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        while len(visited) < len(points):
            cost, n = heapq.heappop(minHeap)
            if n in visited:
                continue
            
            visited[n] = 1
            totalCost += cost

            for j in range(len(points)):
                if j not in visited:
                    heapq.heappush(minHeap, [manhattan(n, j), j])
            
        
        return totalCost
