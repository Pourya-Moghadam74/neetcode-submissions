class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        processed = set()
        cycle = set()
        res = []

        def dfs(i):
            if i in cycle:
                return False
            
            if i in processed:
                return True
            
            cycle.add(i)

            for pre in preMap[i]:
                if not dfs(pre):
                    return False
            
            processed.add(i)
            cycle.remove(i)
            res.append(i)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return res