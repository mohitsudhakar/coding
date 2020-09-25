"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the
new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def fn(arr):
    # find left and right side products
    left, right = [], []
    l = len(arr)
    cumm, i = 1, 0
    while i < l:
        left.append(cumm)
        cumm *= arr[i]
        i += 1
    cumm, i = 1, l-1
    while i >= 0:
        right.insert(0, cumm)
        cumm *= arr[i]
        i -= 1
    prod = []
    for i in range(l):
        prod.append(left[i]*right[i])
    return prod


if __name__ == '__main__':
    res = fn([1,2,3,4,5])
    print(res)