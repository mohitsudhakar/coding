import heapq

def skyline(buildings):

    """
    init max heap
    get building points
    sort building points
    for each building point b
        add building to heap while building start <= b
        remove from heap while building end <= b
        get max from heap
        add to ans
    """

    buildingPoints = []
    for b in buildings:
        buildingPoints.append(b[0])
        buildingPoints.append(b[1])

    buildingPoints.sort()
    i = 0
    ans = []
    heap = []
    prev = -1
    for b in buildingPoints:
        while i < len(buildings) and buildings[i][0] <= b:
            heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
            i += 1
        while heap and heap[0][1] <= b:
            heapq.heappop(heap)
        h = -heap[0][0] if heap else 0
        if h != prev:
            point = [b, h]
            ans.append(point)
            prev = h
    return ans

if __name__ == '__main__':
    # start, end, height
    blist = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]

    print('Skyline is')
    print(skyline(blist))
