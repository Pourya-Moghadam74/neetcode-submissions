class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        visited = set()

        def dfs(i, par):
            if i in visited:
                return
            
            visited.add(i)
            for nei in adj[i]:
                if nei == par:
                    continue
                
                dfs(nei, i)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        
        return res