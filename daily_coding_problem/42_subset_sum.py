"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S
that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

def subsetSum(arr, i, sum, res):
    if sum == 0:
        ans.append(res)
        return True
    poss = False
    for j in range(i, len(arr)):
        if sum - arr[j] >= 0:
            poss = subsetSum(arr, j+1, sum-arr[j], res+[arr[j]])

    return poss

if __name__ == '__main__':
    S = [12, 1, 61, 5, 9, 2]
    k = 24
    ans = []
    subsetSum(S, 0, k, [])
    print(ans)