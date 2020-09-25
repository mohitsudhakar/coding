# Longest palindromic subsequence

def lps_rec(i,j):
    if i == j:
        return 1
    if i > j:
        return 0
    if string[i] == string[j]:
        return lps_rec(i+1, j-1) + 2
    else:
        return max(lps_rec(i+1, j), lps_rec(i, j-1))

if __name__ == '__main__':
    string = 'abcbabbabd' # 7
    l = len(string)
    dp = [[-1]*l for _ in range(l)]
    ans = lps_rec(0, l-1)
    print(ans)
