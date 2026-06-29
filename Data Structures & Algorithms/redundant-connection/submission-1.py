class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(src, target, visited):
            if src == target:
                return True
            
            visited.add(src)

            for nei in adj[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False
        

        for a, b in edges:
            visited = set()

            if a in adj and b in adj and dfs(a, b, visited):
                return [a, b]
            
            adj[a].append(b)
            adj[b].append(a)