
def comb(s, n):

    for i in range(n):
        curr = ''
        for j in range(i, n):
            curr += s[j]
            ans.append(curr)


if __name__ == '__main__':
    s = 'abca'
    s = list(s)
    # s.sort()
    ans = []
    comb(s, len(s))
    print(ans)
