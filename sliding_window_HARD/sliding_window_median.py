
def medianSlidingWindow(arr: list, k: int) -> list:

    # partition idea
    def partition(lo, hi):
        # choose a pivot
        p = hi
        i, j = lo, lo
        while j < hi:
            if nums[j] <= nums[p]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[i], nums[p] = nums[p], nums[i]
        return i

    def quickselect(lo, hi, n):
        if lo <= n <= hi:
            p = partition(lo, hi)
            if p == n:
                return nums[p]
            elif n < p:
                return quickselect(lo, p-1, n)
            else:
                return quickselect(p+1, hi, n)

    even = k & 1 == 0
    i = 0
    max_median = []
    while i < len(arr) - k + 1:
        nums = arr.copy()
        n = i + k//2
        median = quickselect(i, i+k-1, n)
        if even:
            n2 = n-1
            m2 = quickselect(i, i+k-1, n2)
            median += m2
            median /= 2
        max_median.append(median)
        i += 1

    return max_median

if __name__ == '__main__':
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = medianSlidingWindow(arr, k)
    print(res)
    assert res == [1,-1,-1,3,5,6]