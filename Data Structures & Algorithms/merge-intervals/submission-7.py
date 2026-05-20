class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            
            elif intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            
            else:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            
        return res
