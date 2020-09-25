"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number of conference rooms required.


Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
"""

import heapq
def minMeetingRooms(intervals):
    # sort the intervals by start time
    intervals.sort()
    heap = []
    rooms = 0
    for interval in intervals:
        if heap and interval[0] >= heap[0]:
            heapq.heappop(heap)
        else:
            rooms += 1
        heapq.heappush(heap, interval[1])


    print(intervals, '\t meeting rooms reqd', rooms)
    return rooms

if __name__ == '__main__':

    # arr = [(10,12), (15,25), (0,15), (5,15)]
    # arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    arr = [(1,4), (2,5), (9,12), (5,9), (5,12)]
    # arr = [[0, 30],[5, 10],[15, 20]]

    assert 2 == minMeetingRooms(arr)
    assert 2 == minMeetingRooms([[0, 30],[5, 10],[15, 20]])
    assert 1 == minMeetingRooms([[7,10],[2,4]])