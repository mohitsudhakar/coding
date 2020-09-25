
def job():
    LT = [(L[i], T[i]) for i in range(len(L))]
    LT.sort(key=lambda lt: -lt[0]/lt[1])
    return LT

if __name__ == '__main__':
    L = [1,2,3,5,6]
    T = [2,4,1,3,2]
    ans = job()
    print(ans)