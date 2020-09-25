
if __name__ == '__main__':

    n, k = tuple(map(int, input().split()))
    lis = list(map(int, input().split()))
    count = k
    if lis[k-1] == 0:
        i = k-1
        while i >= 0 and lis[i] == 0:
            count -= 1
            i -= 1
    else:
        for i in range(k, n):
            if lis[i] == lis[k-1]:
                count += 1
    print(count)