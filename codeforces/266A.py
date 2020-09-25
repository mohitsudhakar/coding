
if __name__ == '__main__':

    n = int(input())
    s = input()
    remove = 0
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            remove += 1
        i += 1
    print(remove)