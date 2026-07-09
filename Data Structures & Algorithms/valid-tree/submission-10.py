class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        def dfs(i, par):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adj[i]:
                if nei == par:
                    continue
                
                if dfs(nei, i) == False:
                    return False
            
        dfs(0, -1)

        if len(visited) != n:
            return False
        
        if len(edges) != n - 1:
            return False
        
        return True
        
        