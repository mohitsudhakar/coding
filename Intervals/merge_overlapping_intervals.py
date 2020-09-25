

def merge_overlapping_intervals(intervals):
    print('Sort by start')
    intervals.sort()    # sort by start
    # intervals.sort(key=lambda i: i[1])    # sort by end
    stack = []
    for interval in intervals:
        if stack and interval[0] < stack[-1][1]:
            top = stack.pop()
            stack.append((min(top[0], interval[0]), max(top[1], interval[1])))
        else:
            stack.append(interval)
        print(stack)


if __name__ == '__main__':

    arr = [(10,12), (15,25), (0,15), (5,15)]
    # arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]

    merge_overlapping_intervals(arr)