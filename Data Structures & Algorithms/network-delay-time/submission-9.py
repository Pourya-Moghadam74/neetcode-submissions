class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = {}
        adj = {}
        minHeap = [[0, k]]

        for i in range(n + 1):
            adj[i] = []
        
        for u, v, t in times:
            adj[u].append([t, v])
        

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            

            for t, v in adj[n1]:
                if v not in shortest:
                    heapq.heappush(minHeap, [w1 + t, v])
                
        res = 0
        for i in range(1, n + 1):
            if i not in shortest:
                return -1
            else:
                res = max(res, shortest[i])
        
        return res