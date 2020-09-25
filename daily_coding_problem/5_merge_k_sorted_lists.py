"""
Return a new sorted merged list from K sorted lists, each with size N.
"""

import heapq

def fn(lis):
    heap = []
    for i in range(len(lis)):
        heapq.heappush(heap, (lis[i][0], 0, i))

    while heap:
        el, i, row = heapq.heappop(heap)
        yield el
        if i + 1 < len(lis[row]):
            heapq.heappush(heap, (lis[row][i+1], i+1, row))

if __name__ == '__main__':

    arr = [[1,3,5,7,9],[2,4,6,8],[3,6,9],[4,8,9]]
    res = fn(arr)
    for i in range(15):
        print(next(res))