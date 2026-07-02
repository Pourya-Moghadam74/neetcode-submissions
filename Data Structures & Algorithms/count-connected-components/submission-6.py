class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)

            for nei in adj[i]:
                dfs(nei)
            
        
        res = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res