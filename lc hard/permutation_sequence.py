import math

def getPermutation(n: int, k: int) -> str:

    numbers = [i for i in range(1,n+1)]
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        permutation += str(numbers[index])
        numbers.pop(index)
        # numbers.remove(numbers[index])

    return permutation

if __name__ == '__main__':

    print(getPermutation(4, 9))