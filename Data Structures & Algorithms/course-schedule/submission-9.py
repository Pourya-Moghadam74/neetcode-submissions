class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        cycle = set()

        def dfs(node):

            if node in cycle:
                return False

            if node in visited:
                return True
            
            cycle.add(node)
            visited.add(node)
            for pre in preMap[node]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(node)
            
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True