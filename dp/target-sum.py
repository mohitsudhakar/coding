# Target Sum
# Given an array of integers, nums and a target value T,
# find the number of ways that you can add and subtract the
# values in nums to add up to T.

def target_rec(i, curr):
    if i == n:
        return 1 if curr == T else 0
    return target_rec(i+1, curr + nums[i]) + target_rec(i+1, curr - nums[i])

def target_dp(i, curr):
    print(i, curr)
    if i == n:
        dp[i][curr] = 1 if curr == T else 0
        return dp[i][curr]
    if dp[i][curr] != -1:
        return dp[i][curr]
    dp[i][curr] = target_dp(i+1, curr + nums[i]) + target_dp(i+1, curr - nums[i])
    return dp[i][curr]

if __name__ == '__main__':
    nums = [1,1,1,1,1]
    n = len(nums)
    T = 3
    dp = [[-1]*(2*sum(nums)+1) for _ in range(n+1)]
    # ans = target_rec(0, 0)
    ans = target_dp(0, 0)
    print(ans)
    print(dp)
