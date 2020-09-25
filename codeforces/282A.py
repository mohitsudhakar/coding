
if __name__ == '__main__':

    n = int(input())
    ans = 0
    for i in range(n):
        op = input()
        if '+' in op:
            ans += 1
        elif '-' in op:
            ans -= 1
    print(ans)