# Fibonacci numbers - Given an integer n, write a function that
# will return the nth Fibonacci number.

def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_dp(i):
    if dp[i] != -1:
        return dp[i]
    if i == 0:
        return 0
    if i == 1:
        return 1
    dp[i] = fib_dp(i-1) + fib_dp(i-2)
    return dp[i]

if __name__ == '__main__':
    n = 50
    # ans = fib_rec(n)
    dp = [-1]*(n+1)
    ans = fib_dp(n)
    print(ans)
