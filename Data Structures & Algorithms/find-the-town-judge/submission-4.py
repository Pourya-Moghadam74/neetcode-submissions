class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {}
        adj2 = {}

        for i in range(1, n + 1):
            adj[i] = []
            adj2[i] = []

        for a, b in trust:
            adj[b].append(a)
            adj2[a].append(b)
        for key in adj:
            if len(adj[key]) == n - 1 and not adj2[key]:
                return key
        
        return -1