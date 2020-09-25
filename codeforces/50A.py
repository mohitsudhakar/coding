
if __name__ == '__main__':

    m, n = tuple(map(int, input().split()))
    ans = 0
    if m%2 == 0:
        ans = n * (m//2)
    elif n%2 == 0:
        ans = m * (n//2)
    else:
        ans = (m*n) // 2
    print(ans)
