import collections

def f(bids, totalShares):
    bids.sort(key=lambda bid: bid[3])
    bids.sort(key=lambda bid: bid[2], reverse=True)

    queue = bids.copy()
    touched = set()
    while totalShares > 0:
        if len(queue) == 1:
            return 0
        if queue[0][2] > queue[1][2]:
            totalShares = max(0, totalShares - queue[0][1])
            touched.add(queue[0][0])
            queue.pop(0)
        else:
            # find rightmost index where price is same as i=0
            right = 1
            while right < len(queue) and queue[0][2] == queue[right][2]:
                right += 1
            i, it = 0, 0
            done = list()
            while totalShares > 0:
                i = it % right
                if i in done:
                    it += 1
                    continue
                if queue[i][1] == 0:
                    done.append(i)
                else:
                    queue[i][1] -= 1
                    totalShares -= 1
                touched.add(queue[i][0])
                it += 1
            done.sort(reverse=True)
            for d in done:
                queue.pop(d)
    # print(touched)
    ans = []
    for q in queue:
        if q[0] not in touched:
            ans.append(q[0])
    ans.sort()
    # print(ans)
    return ans


if __name__ == '__main__':

    # bids = [[1,5,5,1], [2,7,8,1], [3,7,5,0], [4,10,3,3]]
    # bids = [[1,2,5,0],[2,1,4,2],[3,5,4,6]]
    bids = [[1,2,4,6208]]
    ans = f(bids, 2)
    print(ans)
