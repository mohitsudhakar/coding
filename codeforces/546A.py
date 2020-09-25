
def func(k, n, w):
    if w <= 0:
        return 0
    s = 0
    i = 1
    while i <= w:
        s += i*k
        i += 1
    if s <= n:
        return 0
    return s-n

if __name__ == '__main__':

    k, n, w = tuple(map(int, input().split()))
    print(func(k, n, w))
