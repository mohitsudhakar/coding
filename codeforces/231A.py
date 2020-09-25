

if __name__ == '__main__':

    n = int(input())
    count = 0
    for i in range(n):
        line = input().split()
        line = list(map(int, line))
        if sum(line) >= 2:
            count += 1
    print(count)