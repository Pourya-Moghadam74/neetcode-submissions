class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        minHeap = [(0, 0)]
        total = 0

        def manhattan(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        while len(visited) != len(points):
            d1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            total += d1

            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(minHeap, (manhattan(n1, i), i))
                
        return total