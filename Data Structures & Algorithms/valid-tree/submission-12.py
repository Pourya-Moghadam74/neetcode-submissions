class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = set()

        def dfs(i, par):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adj[i]:
                if nei == par:
                    continue
                
                if dfs(nei, i) == False:
                    return False
                
            return True

        return dfs(0, -1) and len(visited) == n

