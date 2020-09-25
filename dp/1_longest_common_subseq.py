# Longest Common Subsequence
# Given two sequences, find the length of longest subsequence
# present in both of them.

def lcs_rec(i,j):
    if i == 0 or j == 0:
        return 0
    if str1[i-1] == str2[j-1]:
        return 1 + lcs_rec(i-1,j-1)
    else:
        return max(lcs_rec(i-1,j), lcs_rec(i,j-1))

def lcs_dp(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == 0 or j == 0:
        return 0
    if str1[i-1] == str2[j-1]:
        dp[i][j] = 1 + lcs_dp(i-1,j-1)
    else:
        dp[i][j] = max(lcs_dp(i-1,j), lcs_dp(i,j-1))
    return dp[i][j]

if __name__ == '__main__':
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    m, n = len(str1), len(str2)
    dp = [[-1]*(n+1) for _ in range(m+1)]
    # ans = lcs_rec(m,n)
    ans = lcs_dp(m,n)
    print(ans)
