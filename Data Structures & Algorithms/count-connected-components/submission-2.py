class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                
                dfs(nei, node)
            
            return True

        res = 0
        for i in range(n):
            if dfs(i, -1) == True:
                res += 1
        

        return res