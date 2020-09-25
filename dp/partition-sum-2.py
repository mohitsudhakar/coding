# Partition a set into two subsets such that the difference of subset
# sums is minimum
# Given a set of integers, the task is to divide it in to two sets
# S1 and S2 such that the absolute difference between their sums is
# minimum.
# If there is a set S with n elements, then if we assume Subset1
# has m elements, Subset2 must have n-m elements and the value of
# abs(sum(Subset1) – sum(Subset2)) should be minimum.

def partition_rec(i, total, curr):
    if i == 0:
        return abs((total - curr) - curr)
    return min(partition_rec(i-1, total, curr + arr[i-1]), partition_rec(i-1, total, curr))

def partition_dp(i, total, curr):
    if dp[i][curr] != -1:
        return dp[i][curr]
    if i == 0:
        return abs((total - curr) - curr)
    dp[i][curr] = min(partition_rec(i-1, total, curr + arr[i-1]), partition_rec(i-1, total, curr))
    return dp[i][curr]


if __name__ == '__main__':
    arr = [1,6,11,5]
    total = sum(arr)
    m = len(arr)
    curr = 0
    dp = [[-1]*(total+1) for _ in range(m+1)]
    # ans = partition_rec(m, total, 0)
    ans = partition_dp(m, total, 0)
    print(ans)