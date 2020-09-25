

def check_overlapping_intervals(intervals):
    print('Sort by start')
    intervals.sort()    # sort by start
    # intervals.sort(key=lambda i: i[1])    # sort by end
    isOverlap = False
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            isOverlap = True
            break
    print('isOverlap', isOverlap)

    print('Sort by end')
    # intervals.sort()    # sort by start
    intervals.sort(key=lambda i: i[1])    # sort by end
    isOverlap = False
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            isOverlap = True
            break
    print('isOverlap', isOverlap)



if __name__ == '__main__':

    arr = [(10,12), (15,25), (0,15), (5,15)]
    # arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]

    check_overlapping_intervals(arr)