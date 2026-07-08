class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        curEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if curEnd > intervals[i][0]:
                res += 1
                curEnd = min(curEnd, intervals[i][1])
            else:
                curEnd = intervals[i][1]
        return res