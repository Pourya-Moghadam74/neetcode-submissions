class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        path = {}
        adj = {}
        heap = [(1, start_node)]

        for i in range(n):
            adj[i] = []
        
        for (s, d), prob in zip(edges, succProb):
            adj[s].append((d, prob))
            adj[d].append((s, prob))
        
        while heap:
            prob1, n1 = heapq.heappop_max(heap)
            if n1 in path:
                continue
            
            path[n1] = prob1

            for n2, prob2 in adj[n1]:
                if n2 not in path:
                    heapq.heappush_max(heap, (prob1 * prob2, n2))
            
        
        if end_node in path:
            return path[end_node]
        
        else:
            return 0