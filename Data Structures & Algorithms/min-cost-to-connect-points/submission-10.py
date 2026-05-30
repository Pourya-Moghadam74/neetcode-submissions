class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        n = len(points)
        visited = set()
        minHeap = [(0, 0)]
        totalCost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)

            if i in visited:
                continue
            
            visited.add(i)
            totalCost += cost

            for j in range(n):
                if j not in visited:
                    heapq.heappush(minHeap, (manhattan(i, j), j))
        
        return totalCost






        