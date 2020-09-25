# Calculate binomial coefficient nCk

def binomial_rec(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_rec(n-1, k) + binomial_rec(n-1, k-1)

def binomial_dp(n, k):
    if dp[n][k] != 0:
        return dp[n][k]
    if k == 0 or k == n:
        return 1
    dp[n][k] = binomial_dp(n-1, k) + binomial_dp(n-1, k-1)
    return dp[n][k]

if __name__ == '__main__':
    N, K = 10, 3
    dp = [[0]*(K+1) for _ in range(N+1)]
    # ans = binomial_rec(N, K)
    ans = binomial_dp(N, K)
    print(ans)
