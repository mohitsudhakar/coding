"""
Given a set of N intervals, the task is to find the maximal set of mutually disjoint intervals.
Two intervals [i, j] & [k, l] are said to be disjoint if they do not have any point in common.
"""

def maximal_set(intervals):

    intervals.sort(key=lambda i: i[1])
    prev_added = intervals[0][1] # end of first interval
    ans = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] > prev_added:
            ans.append(intervals[i])
            prev_added = intervals[i][1]
    print('max non overlapping intervals: ', ans)
    return ans


if __name__ == '__main__':
    # arr = [(10,12), (15,25), (0,15), (5,15)]
    arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]
    # arr = [(1,4), (2,5), (9,12), (5,9), (5,12)]
    # arr = [[1,4], [2,3], [4,6], [8,9]]

    maximal_set(arr)