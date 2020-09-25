
def fun(n, a, b, c):

    arr = [0]*n
    mid = n//2
    l,r = mid, mid
    arr[mid] = n
    a -= c
    b -= c
    c -= 1
    while c:
        if r+1 < n:
            r += 1
            arr[r] = n
            c -= 1
        if c and l-1 >= 0:
            l -= 1
            arr[l] = n
            c -= 1

    # print(arr)
    # all c's added
    # look at a
    # from 0 to l, assign a cells
    # print(a, l, n)
    i = a-1
    an = n-1
    while i >= 0:
        arr[i] = an
        an -= 1
        i -= 1
    print(arr)

    for i in range(l-1, l-a, -1):
        arr[i] = 1
    an = n-1
    for i in range(l-a, -1, -1):
        arr[i] = an
        an -= 1

    for j in range(r+1, b):
        arr[j] = 1
    bn = n-1
    for j in range(b, n):
        arr[j] = bn
        bn -= 1

    # print(arr)
    return arr

if __name__ == '__main__':

    T = int(input())
    tests = []
    i = 1
    while T:
        n, a, b, c = tuple(map(int, input().strip().split(' ')))
        tests.append((n,a,b,c))
        T -= 1

    for n,a,b,c in tests:
        ans = fun(n,a,b,c)
        print('Case #'+str(i) + ": "+ str(ans))
        i += 1

