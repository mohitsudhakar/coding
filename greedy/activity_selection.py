
def activity():
    times.sort(key=lambda t: t[1])
    i = 0
    ans = 1
    for j in range(1, len(times)):
        if times[j][0] >= times[i][1]:
            ans += 1
            i = j
    return ans

if __name__ == '__main__':
    times = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
    ans = activity()
    print(ans)