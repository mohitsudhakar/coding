
if __name__ == '__main__':

    n = int(input())
    tram = 0
    ans = 0
    for i in range(n):
        ex, ent = tuple(map(int, input().split()))
        tram = tram - ex + ent
        ans = max(ans, tram)
    print(ans)