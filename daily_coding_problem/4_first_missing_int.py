"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def fn(nums):
    i = 0
    while i < len(nums):
        if nums[i] <= 0 or nums[i] > len(nums) or nums[nums[i]-1] == nums[i]:
            i += 1
        else:
            nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        print(i, nums)

    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1



if __name__ == '__main__':
    res = fn([3,4,-1,1])
    print(res)