"""
Given an array of intervals of start and end times, return the
count of meeting rooms needed
"""

def minMeetingRooms(intervals):
    intervals.sort(key=lambda u: u[0], reverse = True)
    s, e = intervals[0]
    m_count = 1
    for each in intervals[1:]:
        start,end = each
        if s < end and start < e: ##DeMorgans Law
            print("if", s, end, start, e)
            m_count += 1
        s, e = start, end
    return m_count



print(minMeetingRooms([[9,10], [10,11],[11,12], [10,11]]))

from heapq import heappop,heappush
def min_meeting_rooms_using_heapq( intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []
    res = 0
    # Push the end times to Min Heap
    # If the start time is is less than the min of Min Heap, increment count by 1
    # as two meetings would be in progress simultaneously
    for interval in intervals:
        if len(heap)==0 or heap[0]>interval[0]:
            res += 1
        else:
            heappop(heap)
        heappush(heap, interval[1])
    return res
print(min_meeting_rooms_using_heapq([[9,10], [10,11],[11,12], [10,11]]))