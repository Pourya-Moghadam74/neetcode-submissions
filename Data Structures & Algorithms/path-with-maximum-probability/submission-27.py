class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        path = {}
        adj = {}
        maxHeap = [(1, start_node)]

        for i in range(n):
            adj[i] = []

        for (s, d), prob in zip(edges, succProb):
            adj[s].append((d, prob))
            adj[d].append((s, prob))
        
        while maxHeap:
            prob, n = heapq.heappop_max(maxHeap)
            if n in path:
                continue
            
            path[n] = prob

            for n2, prob2 in adj[n]:
                if n2 not in path:
                    heapq.heappush_max(maxHeap, ((prob * prob2), n2))
        
        return path.get(end_node, 0)