"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""

def power_set(arr, i, curr_set):

    res.append(curr_set)

    for j in range(i, len(arr)):
        power_set(arr, j+1, curr_set+[arr[j]])


if __name__ == '__main__':

    arr = [1,2,3]
    res = []
    power_set(arr, 0, [])
    print(res)