"""
Given an array nums, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

import collections

def maxSlidingWindow(nums: list, k: int) -> list:

    # Use queue to keep only useful elements, remove others
    # element is not useful if it is less than curr element, or
    # if it outside window
    # front of queue is max of every window

    max_window = []
    j = 0

    queue = collections.deque()

    while j < len(nums):
        # remove from front if outside window
        while queue and queue[0] < j-k+1:
            queue.popleft()

        # remove from back if less than curr num
        while queue and nums[queue[-1]] < nums[j]:
            queue.pop()

        # add curr num
        queue.append(j)

        # add front to max window
        if j >= k-1:
            max_window.append(nums[queue[0]])

        j += 1

    return max_window