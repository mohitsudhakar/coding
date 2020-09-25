
if __name__ == '__main__':
    ans = list(map(int, input().split('+')))
    ans = list(sorted(ans))
    ans = '+'.join(list(map(str, ans)))
    print(ans)

