
if __name__ == '__main__':

    s = list(input())
    if s[0].islower():
        s[0] = s[0].upper()
    print(''.join(s))