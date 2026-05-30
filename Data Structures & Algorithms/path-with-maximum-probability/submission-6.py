class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        maxPath = {}
        adj = {}
        maxHeap = [[1, start_node]]
        for i in range(n):
            adj[i] = []
            
        for (s, d), prob in zip(edges, succProb):
            adj[s].append([prob, d])
            adj[d].append([prob, s])

        while maxHeap:
            prob, n1 = heapq.heappop_max(maxHeap)
            
            if end_node in maxPath:
                return maxPath[end_node]

            if n1 in maxPath:
                continue
            
            maxPath[n1] = prob
            for prob2, n2 in adj[n1]:
                if n2 not in maxPath:
                    heapq.heappush_max(maxHeap, [prob * prob2, n2])  


        if end_node in maxPath:
            return maxPath[end_node]
        else:
            return 0
            
        
        