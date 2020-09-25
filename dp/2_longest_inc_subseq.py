# Longest Increasing Subsequence
# Find the length of the longest subsequence of a given sequence
# such that all elements of the subsequence are sorted in increasing
# order.

global maxval

def lis_rec(i):
    if i == 1:
        return 1
    global maxval
    maxTillI = 1
    for j in range(1,i):
        res = lis_rec(j)
        if arr[j-1] < arr[i-1]:
            maxTillI = max(maxTillI, res + 1)
    maxval = max(maxval, maxTillI)
    return maxTillI

def lis_dp(i):
    if dp[i] != -1:
        return dp[i]
    maxTillI = 1
    satisfies = []
    for j in range(1,i):
        res = lis_rec(j)
        if arr[i-1] % arr[j-1] == 0:
            maxTillI = max(maxTillI, res + 1)
            satisfies.append(arr[j-1])
    # maxval = max(maxval, maxTillI)
    dp[i] = maxTillI
    satisfies.append(arr[i-1])
    store[i] = satisfies
    return dp[i]

import collections
if __name__ == '__main__':
    arr = [11, 22, 9, 33, 21, 50, 44, 60, 55, 66]
    # arr = [4,8,10,240]
    n = len(arr)
    maxval = 1
    dp = [-1]*(n+1)
    store = collections.defaultdict(list)
    dp[0] = 1
    # lis_rec(n)
    lis_dp(n)
    print(max(dp))
    print(store[n])