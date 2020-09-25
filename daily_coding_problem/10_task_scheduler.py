"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import collections
import heapq

def fn(tasks, n: int) -> int:

    count = collections.Counter(tasks)
    heap = [(-count[c], c) for c in count]
    heapq.heapify(heap)
    ans = 0

    while heap:
        k = n+1
        lis = []
        while k > 0 and heap:
            freq, el = heapq.heappop(heap)
            lis.append((freq+1, el))
            k -= 1
            ans += 1
        for el in lis:
            if el[0] < 0:
                heapq.heappush(heap, el)
        if not heap:
            break
        # add idle time
        if k > 0:
            ans += k

    return ans

if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2
    res = fn(tasks, n)
    print(res)