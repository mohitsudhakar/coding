"""
This problem was asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def two_sum(arr, k):
    dic = {}
    for a in arr:
        if k-a in dic:
            return True
        dic[a] = 1
    return False

if __name__ == '__main__':

    res = two_sum([10, 15, 3, 7], k=19)
    print(res)