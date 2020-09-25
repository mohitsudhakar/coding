# Coin change problem - Given an integer representing a given
# amount of change, write a function to compute the minimum number
# of coins required to make that amount of change. You can assume
# that there is always a 1¢ coin.

def coin_rec(c):
    if c == 0:
        return 0
    min_num = float('inf')
    for coin in coins:
        if c-coin >= 0:
            min_num = min(min_num, coin_rec(c-coin))
    return min_num + 1

def coin_dp(c):
    if dp[c] != -1:
        return dp[c]
    if c == 0:
        return 0
    min_num = float('inf')
    for coin in coins:
        if c-coin >= 0:
            min_num = min(min_num, coin_dp(c-coin))
    dp[c] = min_num + 1
    return dp[c]

if __name__ == '__main__':
    coins = [1,2,6,10]
    change = 12
    dp = [-1]*(change+1)
    ans = coin_dp(change)
    print(ans)

