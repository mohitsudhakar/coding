
if __name__ == '__main__':

    n, t = tuple(map(int, input().split()))

    s = input()

    for i in range(t):
        s = s.replace('BG', 'GB')
    print(s)
