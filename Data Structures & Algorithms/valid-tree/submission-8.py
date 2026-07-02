class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        cycle = set()
        adj = defaultdict(list)

        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        def dfs(i, parent):
            if i in cycle:
                return False
            
            if i in visited:
                return True
            
            cycle.add(i)

            for nei in adj[i]:
                if nei == parent:
                    continue
                
                if dfs(nei, i) == False:
                    return False
            
            cycle.remove(i)
            visited.add(i)
            return True
        
        for i in range(n):
            if dfs(i, -1) == False:
                return False
        
        return True if len(edges) == n - 1 else False