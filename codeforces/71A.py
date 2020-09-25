
if __name__ == '__main__':

    num_tests = int(input())
    for t in range(num_tests):
        word = input()
        l = len(word)
        if l > 10:
            word = word[0] + str(l-2) + word[l-1]
        print(word)