
if __name__ == '__main__':

    a, b = tuple(map(int, input().split()))

    i = 0
    while a <= b:
        a *= 3
        b *= 2
        i += 1
    print(i)