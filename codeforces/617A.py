

if __name__ == '__main__':

    steps = int(input())

    if steps < 5:
        print(1)
    elif steps % 5 == 0:
        print(steps // 5)
    else:
        print(steps // 5 + 1)

