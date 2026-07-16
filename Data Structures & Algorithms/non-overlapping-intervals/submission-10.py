class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curEnd = float("-inf")
        res = 0

        for i in intervals:
            if i[0] < curEnd:
                curEnd = min(curEnd, i[1])
                res += 1
            else:
                curEnd = i[1]
        
        return res