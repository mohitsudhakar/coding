
def calcSteps(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    steps = 0
    while x1 < x2 and y1 < y2:
        x1 += 1
        y1 += 1
        steps += 1
    while x1 > x2 and y1 > y2:
        x1 -= 1
        y1 -= 1
        steps += 1
    while x1 < x2 and y1 > y2:
        x1 += 1
        y1 -= 1
        steps += 1
    while x1 > x2 and y1 < y2:
        x1 -= 1
        y1 += 1
        steps += 1
    if y1 == y2:
        steps += abs(x1 - x2)
    if x1 == x2:
        steps += abs(y1 - y2)
    return steps



def infinite_grid(points):
    steps = 0
    for i in range(1, len(points)):
        steps += calcSteps(points[i-1], points[i])
    return steps

if __name__ == '__main__':

    points = [(0, 0), (1, 1), (1, 2)]
    assert infinite_grid([(0, 0), (1, 1), (1, 2)]) == 2
    assert infinite_grid([(0, 0), (1, 1), (1, 2), (3, 4)]) == 4
    assert infinite_grid([(0, 0), (1, 1), (1, 2), (3, 6)]) == 6
