# Given an array p[] which represents the chain of matrices such that
# the ith matrix Ai is of dimension p[i-1] x p[i]. We need to write a
# function MatrixChainOrder() that should return the minimum number
# of multiplications needed to multiply the chain.

def matrix_dp(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i+1 == j:
        return 0
    minij = 1e30
    for k in range(i+1,j):
        minij = min(minij, p[i]*p[k]*p[j] + matrix_dp(i, k) + matrix_dp(k, j))
    dp[i][j] = minij
    return dp[i][j]

def matrix_rec(i,j):
    if i+1 == j:    # make sure i<k<j exist
        return 0
    minij = 1e30
    for k in range(i+1, j):
        minij = min(minij, p[i]*p[k]*p[j] + matrix_rec(i, k) + matrix_rec(k, j))
    return minij

if __name__ == '__main__':
    p = [10,30,5,60, 10,30,5,60 ]
    dp = [[-1]*len(p) for _ in range(len(p))]
    import time
    start = time.time()
    ans = matrix_rec(0, len(p)-1)
    timerec = time.time() - start
    print(ans, timerec)
    start = time.time()
    ans = matrix_dp(0, len(p)-1)
    timedp = time.time() - start
    print(ans, timedp)
    print((timerec-timedp)/timerec*100, '% improvement')
