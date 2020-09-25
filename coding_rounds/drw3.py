

def shortestRunLengthEncoding(s: str, k: int) -> int:

    leftLength, rightLength = [0], [0]

    lastCount = 1
    for i in range(1, len(s)):
        leftLength.append(lastCount)
        if s[i] == s[i-1]:
            if lastCount in [1,9,99,999,9999,99999]:
                lastCount += 1
        else:
            lastCount = 1

    lastCount = 1
    for i in range(len(s)-2, -1, -1):
        rightLength.append(lastCount)
        if s[i] == s[i+1]:
            if lastCount in [1,9,99,999,9999,99999]:
                lastCount += 1
        else:
            lastCount = 1

    rightLength = rightLength[::-1]
    print('leftLength', leftLength)
    print('rightLength', rightLength)

    i = 0
    min_len = float('inf')
    curr_len = 0
    while i+k < len(s):
        if s[i] == s[i+k]:
            # merge
            break
        else:
            # take left + right
            curr_len = leftLength[i] + rightLength[i+k]
            min_len = min(min_len, curr_len)


if __name__ == '__main__':

    shortestRunLengthEncoding("AAAAAAAAAAABXXAAAAAAAAAA",3)