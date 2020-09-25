import collections

def slidingWindowTemplate(s: str, t: str):
    res = []
    count = collections.Counter(t)
    uniq = len(count)

    start, end = 0, 0
    while end < len(s):

        c = s[end]
        if c in count:
            count[c] -= 1   # plus or minus one
            if count[c] == 0:
                uniq -= 1

        end += 1

        # increase start to make it valid/invalid again
        while uniq == 0:    # change uniq condition acc to question
            c = s[start]
            if c in count:
                count[c] += 1   # plus or minus one
                if count[c] > 0:
                    uniq += 1   # modify uniq acc to requirement

            """
            save/update result if find a target
            """

            start += 1

    return res

