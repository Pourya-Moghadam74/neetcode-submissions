class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        room = 0
        max_room = 0
        s, e = 0, 0
        
        while s < len(start):
            if start[s] < end[e]:
                room += 1
                s += 1
            
            else:
                room -= 1
                e += 1
            max_room = max(max_room, room)
        
        return max_room