class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        maxHeap = [(1, start_node)]
        adj = defaultdict(list)

        for (s, d), p in zip(edges, succProb):
            adj[s].append((d, p))
            adj[d].append((s, p))
        
        path = {}

        while maxHeap:
            prob, node = heapq.heappop_max(maxHeap)

            if node in path:
                continue
            
            path[node] = prob

            for n2, p2 in adj[node]:
                if n2 not in path:
                    heapq.heappush_max(maxHeap, (prob * p2, n2))
        

        if end_node not in path:
            return 0
        
        return path[end_node]