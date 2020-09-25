# Edit Distance
# Given two strings str1 and str2 and below operations that can
# be performed on str1. Find minimum number of edits (operations)
# required to convert ‘str1’ into ‘str2’.
# Operations are insert, remove, replace; costs are same.

def edit_rec(i,j):
    if i == 0:
        return j
    if j == 0:
        return i
    if str1[i-1] == str2[j-1]:
        return edit_rec(i-1,j-1)
    else:
        return 1 + min(edit_rec(i-1,j), edit_rec(i,j-1), edit_rec(i-1,j-1))

def edit_dp(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == 0:
        return j
    if j == 0:
        return i
    if str1[i-1] == str2[j-1]:
        dp[i][j] = edit_dp(i-1,j-1)
    else:
        dp[i][j] = 1 + min(edit_dp(i-1,j),
                       edit_dp(i,j-1),
                       edit_dp(i-1,j-1))
    return dp[i][j]

if __name__ == '__main__':
    str1 = "sunday"
    str2 = "saturday"
    m, n = len(str1), len(str2)
    dp = [[-1]*(n+1) for _ in range(m+1)]
    # ans = edit_rec(m,n)
    ans = edit_dp(m,n)
    print(ans)
