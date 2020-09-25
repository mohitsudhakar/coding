from random import randint

def sample(x, count):
    if count == 1:
        return x

    replace = randint(1, count)
    if replace == count-1:
        return x
    else:
        return replace

if __name__ == '__main__':
    inp = [0,1,2,3,4,5,6,7,8,9]
    should = [1]
    for i in range(1,10):
        should.append(should[-1] + 1/(i+1))
    should = [should[-1]-should[i] for i in range(len(should)-1)]
    print(should)
    cnt = [0]*(len(inp))
    total = 100000
    for _ in range(total):
        count = 1
        for i in inp:
            s = sample(i, count)
            count += 1
            cnt[s-1] += 1
    probs = [c/total for c in cnt]
    print(probs)
