# Given array, find 3 numbers which sum to 0

def three_sum(arr):
    arr.sort()
    ans = []
    for i in range(0, len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        l = i+1
        r = len(arr)-1
        while l < r:
            total = arr[i] + arr[l] + arr[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                ans.append((arr[i], arr[l], arr[r]))
                # prevent duplicates
                while l < r and arr[l] == arr[l+1]:
                    l += 1
                while l < r and arr[r] == arr[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return ans

if __name__ == '__main__':
    array = [1, -2, -1, 0, -1, 1]
    print(three_sum(array))
