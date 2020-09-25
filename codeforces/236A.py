import collections
if __name__ == '__main__':

    s = input()
    count = collections.Counter(s)
    if len(count) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')