"""
This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one
with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic
substring of "bananas" is "anana".
"""

def lps(i,j):
    if (i,j) in dp:
        return dp[i,j]
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    dp[i,j] = s[i+1:j]
    return dp[i,j]

if __name__ == '__main__':
    # s = "aabcdcb"
    s = "bananas"
    ans = ""
    dp = {}
    for k in range(len(s)-1):
        ans = max(ans, lps(k,k), lps(k,k+1), key=len)
    print(ans)