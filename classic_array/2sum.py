# Return indices of 2 numbers in give array that sum to s

def two_sum(arr, s):
    dic = {}
    for i, a in enumerate(arr):
        if s-a in dic:
            return dic[s - a], i
        dic[a] = i
    return None

if __name__ == '__main__':
    sum_ = 10
    array = [1,2,3,4,5,7]
    print(two_sum(array, sum_))