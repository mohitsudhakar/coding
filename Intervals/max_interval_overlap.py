"""
Consider a big party where a log register for guest’s entry and exit times is maintained.
Find the time at which there are maximum guests in the party.

1. Brute force is to find, min and max time and count number of guests for each time
This is O(N*(max-min)) time O(max-min) space

2. Sort start and end, and traverse both in merge fashion
    if start <= end, add to curr, else remove from curr
    keep track of max people
O(NlogN) solution
    curr = number of people in room


arr = [(1,4), (2,5), (9,12), (5,9), (5,12)]
"""

def get_min_max(intervals):
    max_time = 0
    min_time = float('inf')
    for interval in intervals:
        min_time = min(min_time, interval[0])
        max_time = max(max_time, interval[1])
    return min_time, max_time

def max_overlap_3(intervals):
    """
    O(N) solution with aux array
    """
    _, max_time = get_min_max(intervals)
    aux = [0]*(max_time+2)
    for start,end in intervals:
        aux[start] += 1
        aux[end+1] -= 1
    for i in range(1,len(aux)):
        aux[i] += aux[i-1]

    ans = max(enumerate(aux), key=lambda c: c[1])
    print(ans[1], 'at time',ans[0])

def max_overlap_2(intervals):
    """
    O(NlogN) solution
    curr = number of people in room
    Sort start and end, and traverse both in merge fashion
    if start <= end, add to curr, else remove from curr
    keep track of max people
    """

    start = [i[0] for i in intervals]
    finish = [i[1] for i in intervals]
    start.sort()
    finish.sort()
    i, j = 0, 0
    curr = 0
    ans = 0
    while i < len(intervals) and j < len(intervals):
        if start[i] <= finish[j]:
            curr += 1
            i += 1
        else:
            curr -= 1
            j += 1
        ans = max(ans, curr)
    print(ans, 'at time', i)
    return ans

def max_overlap_1(intervals):
    """
    Brute force, as described above
    """
    min_time, max_time = get_min_max(intervals)

    count = [0]*(max_time - min_time + 1)
    for interval in intervals:
        for i in range(interval[0], interval[1]+1):
            count[i-min_time] += 1

    ans = max(enumerate(count), key=lambda c: c[1])
    print(ans[1], 'at time',ans[0] + min_time)


if __name__ == '__main__':

    # arr = [(10,12), (15,25), (0,15), (5,15)]
    # arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    arr = [(1,4), (2,5), (9,12), (5,9), (5,12)]
    # arr = [[0, 30],[5, 10],[15, 20]]

    max_overlap_3(arr)
