# 0-1 Knapsack
# Given a list of items with values and weights, as well
# as a max weight, find the maximum value you can generate
# from items, where the sum of the weights is less than or
# equal to the max.

def knapsack_rec(rem_wt, i):
    if rem_wt == 0 or i == 0:
        return 0

    if rem_wt - weights[i-1] >= 0:
        # can choose
        return max(knapsack_rec(rem_wt - weights[i-1], i-1) + values[i-1], # choose
                   knapsack_rec(rem_wt, i-1))                              # don't choose
    else:
        # can't choose
        return knapsack_rec(rem_wt, i-1)

def knapsack_dp(rem_wt, i):
    if dp[rem_wt][i] != -1:
        return dp[rem_wt][i]

    if rem_wt == 0 or i == 0:
        dp[rem_wt][i] = 0
        return 0

    if rem_wt - weights[i-1] >= 0:
        dp[rem_wt][i] = max(knapsack_dp(rem_wt - weights[i-1], i-1) + values[i-1],
                            knapsack_dp(rem_wt, i-1))
    else:
        dp[rem_wt][i] = knapsack_dp(rem_wt, i-1)
    return dp[rem_wt][i]

if __name__ == '__main__':

    weights = [1,2,3]
    values = [6,10,12]
    max_weight = 5
    n = len(values)
    dp = [[-1]*(n+1) for _ in range(max_weight+1)]
    # ans = knapsack_rec(max_weight, n)
    ans = knapsack_dp(max_weight, n)
    print(ans)

