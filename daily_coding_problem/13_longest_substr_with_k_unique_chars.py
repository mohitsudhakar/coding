"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
import collections

def fn(string, k):
    curr_start = curr_end = 0
    max_start = 0
    max_len = 0

    count = dict()
    for i in range(len(string)):
        count[string[i]] = count.get(string[i], 0) + 1
        curr_end += 1

        while len(count) > k:
            if string[curr_start] in count and count[string[curr_start]] > 0:
                count[string[curr_start]] -= 1
                if count[string[curr_start]] == 0:
                    del count[string[curr_start]]
                curr_start += 1

        if curr_end - curr_start + 1 > max_len:
            max_len = curr_end - curr_start + 1
            max_start = curr_start
    return string[max_start:max_start+max_len+1]

if __name__ == '__main__':

    s = "aabacbebebe"
    k = 3
    res = fn(s, k)
    print(res, len(res))
