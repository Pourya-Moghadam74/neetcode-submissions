class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(list)

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set()
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart

            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if dfs(nei, node):
                    cycle.add(node)

                    if node == cycleStart:
                        return False
                    
                    return True
                
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        
        return []
