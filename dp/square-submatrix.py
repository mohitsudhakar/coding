# Largest Square submatrix of 1s - Given a 2D boolean array,
# find the largest square subarray of true values.
# The return value should be the side length of the largest
# square subarray.

def sub_rec(i,j):
    if i == 0 or j == 0:
        return arr[i][j]
    if not arr[i][j]:
        return 0
    if sub_rec(i-1,j) and sub_rec(i,j-1):
        return sub_rec(i-1,j-1) + 1
    return arr[i][j]

def sub_dp(i,j):
    if dp[i][j] != 0:
        return dp[i][j]
    if i == 0 or j == 0:
        dp[i][j] = arr[i][j]
        return dp[i][j]
    if not arr[i][j]:
        return 0
    if sub_dp(i-1,j) and sub_dp(i,j-1):
        dp[i][j] = sub_dp(i-1,j-1)+1
    else:
        dp[i][j] = arr[i][j]
    return dp[i][j]


if __name__ == '__main__':
    arr = [
        [1,1,0,1],
        [1,1,0,0],
        [0,0,0,1],
    ]
    m, n = len(arr), len(arr[0])
    dp = [[0]*(n) for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            ans = max(ans, sub_dp(i,j))
    print(dp)
    # ans = max([max(d) for d in dp])
    print(ans)
