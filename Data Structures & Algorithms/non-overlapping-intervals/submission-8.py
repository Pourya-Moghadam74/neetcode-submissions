class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curEnd = float("-inf")
        res = 0

        for i in intervals:
            if curEnd > i[0]:
                res += 1
                curEnd = min(curEnd, i[1])
            
            else:
                curEnd = i[1]
        
        return res