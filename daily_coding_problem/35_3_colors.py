"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the
array so that all the Rs come first, the Gs come second, and the Bs come last.
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become
['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

# O(N) time, constant space

def fn(arr):
    n = len(arr)
    i = 0
    for j in range(n):
        if arr[j] == 'R':
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    i = n-1
    for j in range(n-1, -1, -1):
        if arr[j] == 'B':
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1

if __name__ == '__main__':
    arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    fn(arr)
    print(arr)