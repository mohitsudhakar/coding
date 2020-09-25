"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def fn(arr):
    # f(i) = ans till index i
    # f(i) = max(arr[i] + f(i-2), f(i-1))
    #               choose         dont
    def rec(i):
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]

        dp[i] = max(rec(i-1), arr[i] + rec(i-2))
        return dp[i]

    dp = [-1]*(len(arr))
    return rec(len(arr)-1)

if __name__ == '__main__':

    res = fn([5,1,1,5])
    print(res)
    res = fn([2,4,6,2,5])
    print(res)