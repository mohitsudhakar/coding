
def fun(nums):

    max_len = 0
    i = 0
    while i < len(nums)-1:
        j = i
        d = nums[i+1] - nums[i]
        while j < len(nums)-1 and nums[j+1] - nums[j] == d:
            j += 1
        if max_len < j - i + 1:
            max_len = j - i + 1
            i = j
        else:
            i += 1

    return max_len

if __name__ == '__main__':

    T = int(input())
    tests = []
    while T:
        n = int(input())
        tests.append(list(map(int, input().strip().split(' '))))
        T -= 1

    i = 1
    for t in tests:
        print('Case #'+str(i) + ": "+ str(fun(t)))
        i += 1
