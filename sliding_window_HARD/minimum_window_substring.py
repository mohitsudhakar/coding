"""
Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique
minimum window in S.
"""

import collections

def minWindow(s: str, t: str) -> str:

    # sliding window
    # keep count of chars in dic and match count of new char with count of char in t

    counts = collections.Counter(t)
    dic = {}
    i, j = 0, 0
    uniq = 0
    min_len = float('inf')
    min_str = ""

    while j < len(s):

        # update count dic
        dic[s[j]] = dic.get(s[j], 0) + 1

        # update unique
        if dic[s[j]] == counts[s[j]]:
            uniq += 1

        # update min_len for valid str
        while i <= j and uniq == len(counts):

            # update dic
            dic[s[i]] -= 1

            # update unique
            if s[i] in dic and dic[s[i]] < counts[s[i]]:
                uniq -= 1

            # update min_len
            if j-i+1 < min_len:
                min_len = j-i+1
                min_str = s[i:j+1]

            i += 1

        j += 1

    return min_str
