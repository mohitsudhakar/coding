
def perm(s, i, ans):
    if i == len(s)-1:
        ans.append(''.join(s))
    else:
        for j in range(i, len(s)):
            s[i], s[j] = s[j], s[i]
            perm(s, i+1, ans)
            s[i], s[j] = s[j], s[i]


def perm_without_dup(s, i, ans):
    if i == len(s)-1:
        ans.append(''.join(s))
    else:
        for j in range(i, len(s)):
            if j > i and s[j] == s[i]:
                continue
            s[i], s[j] = s[j], s[i]
            perm_without_dup(s, i+1, ans)
            s[i], s[j] = s[j], s[i]


if __name__ == '__main__':
    s = 'abca'
    s = list(s)
    s.sort()
    with_dup = []
    without_dup = []
    perm(s, 0, with_dup)
    perm_without_dup(s, 0, without_dup)
    print('With duplicates', len(with_dup))

    print(with_dup)
    print('Without dups', len(without_dup))
    print(without_dup)
