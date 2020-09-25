"""

"""

def wordBreak(s, wordDict) -> bool:
    dic = set(wordDict)
    ans = []

    def f(i, lis):
        if i == 0:
            ans.append(lis)
            return True
        poss = False
        for j in range(i):
            if s[j:i] in dic and f(j, [s[j:i]] + lis):
                    poss = True
        return poss

    res = f(len(s), [])
    print(ans)
    print(res)

if __name__ == '__main__':
    wordBreak("bedanbathandbeyond", ['bed', 'bath', 'an','bedbath', 'and', 'beyond'])
