# Partition problem is to determine whether a given set can be
# partitioned into two subsets such that the sum of elements in
# both subsets is equal.

def partition_rec(i, total, curr):
    if i == 0:
        return False
    if curr == total:
        return True
    return partition_rec(i-1, total, curr + arr[i-1]) or partition_rec(i-1, total, curr)

def partition_dp(i, total, curr):
    if dp[i][curr] != -1:
        return dp[i][curr]
    if i == 0:
        return False
    if curr == total:
        return True
    dp[i][curr] = partition_rec(i-1, total, curr + arr[i-1]) or partition_rec(i-1, total, curr)
    return dp[i][curr]

if __name__ == '__main__':
    arr = [1,5,11,5,2]
    total = sum(arr)
    m = len(arr)
    if total % 2 == 1:
        print(False)
        exit(0)
    curr = 0
    dp = [[-1]*(total//2+1) for _ in range(m+1)]
    # ans = partition_rec(m, total//2, 0)
    ans = partition_dp(m, total//2, 0)
    print(ans)
