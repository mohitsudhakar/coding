# Min Cost Path Sum

def mcp_rec(i,j):
    if i == 0 and j == 0:
        return cost[0][0]
    elif i == 0:
        return cost[0][j] + mcp_rec(0, j-1)
    elif j == 0:
        return cost[i][0] + mcp_rec(i-1, 0)

    return cost[i][j] + min(mcp_rec(i-1, j), mcp_rec(i, j-1), mcp_rec(i-1, j-1))

def mcp_dp(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == 0 and j == 0:
        return cost[0][0]
    elif i == 0:
        dp[0][j] = cost[0][j] + mcp_dp(0, j-1)
        return dp[0][j]
    elif j == 0:
        dp[i][0] = cost[i][0] + mcp_dp(i-1, 0)
        return dp[i][0]
    dp[i][j] = cost[i][j] + min(mcp_dp(i-1, j), mcp_dp(i, j-1), mcp_dp(i-1, j-1))
    return dp[i][j]

if __name__ == '__main__':
    cost = [
        [1,2,3],
        [4,8,2],
        [1,5,3]
    ]
    m, n = len(cost), len(cost[0])
    dp = [[-1]*n for _ in range(m)]
    ans = mcp_rec(m-1,n-1)
    print(ans)
    ans = mcp_dp(m-1,n-1)
    print(ans)