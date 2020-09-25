
if __name__ == '__main__':

    matrix = []
    r,c = 0,0
    for i in range(5):
        row = list(map(int, input().split()))
        if 1 in row:
            r = i
        matrix.append(row)

    for i in range(5):
        if matrix[r][i] == 1:
            c = i
            break
    rr = abs(r-2)
    cc = abs(c-2)
    print(rr+cc)