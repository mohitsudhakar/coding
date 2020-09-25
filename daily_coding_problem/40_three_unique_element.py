"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
def fn(nums):
    ones = 0
    twos = 0
    for num in nums:
        twos = twos | (ones & num)
        ones = ones ^ num
        common_bit_mask = ~ (ones & twos)
        ones = ones & common_bit_mask
        twos = twos & common_bit_mask
    return ones

if __name__ == '__main__':
    arr = [6, 1, 3, 3, 3, 6, 6]
    res = fn(arr)
    print(res)