class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        def dfs(i,par):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adj[i]:
                if nei == par:
                    continue
                
                dfs(nei, i)
            
            return True

        res = 0
        for i in range(n):
            if dfs(i, -1) == True:
                res += 1
        
        return res