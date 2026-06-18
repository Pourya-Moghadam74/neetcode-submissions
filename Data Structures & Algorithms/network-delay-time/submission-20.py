class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = {}
        minHeap = [(0, k)] #time, node
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []

        for u, v, t in times:
            adj[u].append((t, v))

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)

            if n1 in shortest:
                continue
            
            shortest[n1] = t1

            for t2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (t2 + t1, n2))
                
        return max(shortest.values()) if len(shortest) == n else -1



        
